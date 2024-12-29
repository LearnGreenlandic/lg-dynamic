#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('5x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'Sem/H.*Abs\+Sg\s') | Inv(r'\+(NIQ|IP|KAR|PAK|INNAQ|GE|QAR|Sem/inst)') | Inv(r'^(nukarleq|qallunaaq|nukappiaraq|nuka|naja|kalaaleq|inuk|arnaq|aqqalu|angut).*SSAQ'), '\t@OBJ>'),
	# sfx(C() | Grep(r'Int\+2Sg\+3SgO') | Inv(r'(naammassi|GALUAR|ulloq|ukioq|illu|TAR\+TAQ|GE\+Sem/have\+TAR|LIR\+QQU|Sem/drink.*GE)'), '\t@PRED'), # Assume copy/paste error
	sfx(C() | Grep(r'Sem/(start|socialize|remember|teach|encounter|know|say|comprehend|mind|name|see).*Int\+2Sg\+3SgO') | Inv(r'GALUAR'), '\t@PRED'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@PRED'],
	sfx(C() | Grep(r'kisianni\+Conj'), '\t@CONJ'),
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Geo|inst).*Trm.*KAR\+V\+Int\+2Sg') | Inv(r'\+(PAK|SSAQ|NNGUAQ|INNAQ|3PlPoss)') | Inv(r'inst\+SSAQ'), '\t@PRED'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P2\tP2\t@PRED'],
	sfx(C() | Grep(r'kisianni\+Conj'), '\t@CONJ'),
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Geo|inst).*Trm') | Inv(r'\+(PAK|SSAQ|NNGUAQ|INNAQ|KAR|3PlPoss)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(run|reach|stop).*\+V\+Int\+2Sg'), '\t@PRED'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@PRED'],
	sfx(C() | Grep(r'kisianni\+Conj'), '\t@CONJ'),
	])

cartesian()

QAs = []
def qa(sentence):
	Q = []
	A = []
	in_a = False
	for w in sentence:
		if w == '⇒':
			in_a = True
			continue

		w = w.split('\t')
		if w[0] == 'P1':
			w[0] = sentence[1].split('\t')[0].replace('+V+Int+2Sg', '+GALUAR+V+Ind+1Sg')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P2':
			w[0] = sentence[0].split('\t')[0].replace('+V+Int+2Sg', '+GALUAR+V+Ind+1Sg')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]

		if not in_a:
			Q.append(w)
		else:
			A.append(w)
	QAs.append([Q, A, trim_ucfirst(' '.join([w[1] for w in Q])), trim_ucfirst(' '.join([w[1] for w in A]))])

for sentence in S.sentences:
	qa(sentence)

for qa in QAs:
	print(f'{qa[2]} ⇒ {qa[3]}')

write_qas(QAs, txt=True)
