#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('2-3x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'uanga\+Pron\+Abs\+1Pl'), '\t@SUBJ>'),
	sfx(C() | Grep(r'marluk\+N\+Ins\+Pl'), '\t@i->N'),
	sfx(C() | Grep(r'^(naja|aleqa)\+Sem/Hfam\+QAR\+Sem/have\+V\+Ind\+1Pl'), '\t@PRED'),
	['.\t.\t@CLB'],

	sfx(C() | Grep(r'^illit\+Pron\+Abs\+2Sg'), '\t@SUBJ>'),
	['P1\tP1\t@PRED'],
	['?\t?\t@CLB'],

	['⇒'],

	['Aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	sfx(C() | Grep(r'ataaseq\+N\+Ins\+Sg'), '\t@i->N'),
	['P2\tP2\t@PRED'],
	['.\t.\t@CLB'],

	['P3\tP3\t@SUBJ>'],
	sfx(C() | Grep(r'^Lene\+Sem/Fem\+Sem/Hum\+Prop\+Ins\+Sg'), '\t@i->N'),
	sfx(C() | Grep(r'^ateq\+QAR\+Sem/be_name\+V\+Ind\+3Sg'), '\t@PRED'),
	['.\t.\t@CLB'],
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
			w[0] = sentence[2].split('\t')[0].replace('+V+Ind+1Pl', '+V+Int+2Sg')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P2':
			w = sentence[2].split('\t')
		elif w[0] == 'P3':
			w[0] = sentence[2].split('\t')[0].replace('+QAR+Sem/have+V+Ind+1Sg', '+N+Abs+Sg+1SgPoss')
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

write_qas(QAs)
