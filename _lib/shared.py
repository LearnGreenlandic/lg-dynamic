import itertools
import json
import math
import os
import random
import regex as re
import sqlite3
import subprocess
import sys
from pathlib import Path

dir = os.path.dirname(os.path.abspath(__file__))
name = re.search(r'([^/]+)\.py$', sys.argv[0])[1]
patterns = []
sentences = []
corpus = []
corpus_kv = {}

seed = 1177320980
random.seed(seed)

class Lit:
	def __init__(self, ws):
		if not isinstance(ws, list):
			ws = [ws]
		self.ws = ws

class Grep:
	def __init__(self, rx):
		self.rx = rx

class Inv:
	def __init__(self, rx):
		self.rx = rx

class C:
	def __init__(self):
		self.c = corpus.copy()

	def __or__(self, o):
		if isinstance(o, Grep):
			self.c = [i for i in self.c if re.search(o.rx, i)]
		elif isinstance(o, Inv):
			self.c = [i for i in self.c if not re.search(o.rx, i)]
		elif isinstance(o, Lit):
			self.c = o.ws
		return self

	def __iter__(self):
		return self.c.__iter__()

def ucfirst(s):
	return s[0].upper() + s[1:]

def _trim_ucfirst(s):
	return s.group(1) + ' ' + ucfirst(s.group(2))

def trim_ucfirst(s):
	s = re.sub(r' ([.?!:]) ([^.])', _trim_ucfirst, s)
	s = re.sub(r'( ⇒) ([^.])', _trim_ucfirst, s)
	s = re.sub(r' ([.?!:,;])', r'\1', s)
	return ucfirst(s)

def load_corpus(fn):
	global corpus, corpus_kv
	seen = set()
	corpus = []
	corpus_kv = {}
	ls = Path(fn).read_text()
	ls = re.sub(r'\s*#[^\n]+', '', ls)
	ls = ls.strip().splitlines()
	for l in ls:
		l2 = l.split('\t')
		if l2[0] in seen:
			continue
		seen.add(l2[0])
		corpus_kv[l2[0]] = l2[1]
		l = l.strip()
		corpus.append(l)

def sfx(lst, s):
	return [e + s for e in list(lst)]

def instantiate():
	global patterns
	nps = []
	for pattern in patterns:
		np = []
		for w in pattern:
			ws = corpus.copy()
			if not isinstance(w, list):
				w = [w]

			for s in w:
				if isinstance(s, Lit):
					ws = s.ws
				elif isinstance(s, Grep):
					ws = [i for i in ws if re.search(s.rx, i)]
				elif isinstance(s, Inv):
					ws = [i for i in ws if not re.search(s.rx, i)]
				else:
					raise Exception('Unknown type for list')
			np.append(ws)
		nps.append(np)
	patterns = nps

def cartesian(n=10000):
	global sentences
	for i,p in enumerate(patterns):
		for j,w in enumerate(patterns[i]):
			patterns[i][j] = list(patterns[i][j])
			random.seed(seed)
			random.shuffle(patterns[i][j])
		ss = []
		for s in itertools.product(*patterns[i]):
			ss.append(s)
			if (len(ss) >= 10000000):
				break
		random.seed(seed)
		random.shuffle(ss)
		sentences.extend(ss[0:math.ceil(n/len(patterns))])
	random.seed(seed)
	random.shuffle(sentences)
	sentences = sentences[0:n]

def write_qas(QAs, txt=False):
	subprocess.run(['rm', '-f', f'{name}.sqlite.new'])
	subprocess.run(['sqlite3', f'{name}.sqlite.new', '-init', f'{dir}/schema.sql'], input='', stdout=subprocess.PIPE)
	con = sqlite3.connect(f'{name}.sqlite.new')
	db = con.cursor()
	for qa in QAs:
		if not txt:
			db.execute("INSERT INTO qas (qa_q, qa_a) VALUES (?, ?)", [json.dumps(qa[0]), json.dumps(qa[1])])
		else:
			db.execute("INSERT INTO qas (qa_q, qa_a, qa_q_txt, qa_a_txt) VALUES (?, ?, ?, ?)", [json.dumps(qa[0]), json.dumps(qa[1]), qa[2], qa[3]])
	con.commit()

	os.rename(f'{name}.sqlite.new', f'{name}.sqlite')

def write_qs(Qs, txt=False):
	subprocess.run(['rm', '-f', f'{name}.sqlite.new'])
	subprocess.run(['sqlite3', f'{name}.sqlite.new', '-init', f'{dir}/schema.sql'], input='', stdout=subprocess.PIPE)
	con = sqlite3.connect(f'{name}.sqlite.new')
	db = con.cursor()
	for q in Qs:
		if not txt:
			db.execute("INSERT INTO qs (q) VALUES (?)", [json.dumps(q)])
		else:
			db.execute("INSERT INTO qs (q, q_txt) VALUES (?, ?)", [json.dumps(q[0]), q[1]])
	con.commit()

	db.execute("VACUUM")
	con.commit()

	os.rename(f'{name}.sqlite.new', f'{name}.sqlite')
