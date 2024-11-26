#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('4x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'Sem/Mask.*Abs\+Sg') | Inv(r'\+(IP|NIQ|U)'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(angaju|qatanngut|nuliaq|aleqa|naja|anaana|ui)\+Sem/Hfam\+GE\+Sem/have\+NNGIT\+V\+Ind\+1Sg\+3SgO'), '\t@PRED'),
	['.\t.\t@CLB'],

	['⇒'],

	sfx(C() | Grep(r'oqar\+Sem/say\+V\+Ind\+1Sg'), '\t@PRED'),
	['P1\tP1\t@OBJ>'],
	['P2\tP2\t@CL-<CIT'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/Mask.*Prop\+Rel\+Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/Fem.*Abs\+Sg') | Inv(r'\+(IP|NIQ|U)'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(qatanngut|nuliaq|aleqa|naja|anaana)\+Sem/Hfam\+GE\+Sem/have\+NNGIT\+V\+Ind\+3Sg\+3SgO'), '\t@PRED'),
	['.\t.\t@CLB'],

	['⇒'],

	['P3\tP3\t@SUBJ>'],
	sfx(C() | Grep(r'oqar\+Sem/say\+V\+Ind\+3Sg'), '\t@PRED'),
	['P4\tP4\t@OBJ>'],
	['P5\tP5\t@CL-<CIT'],
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
			w = sentence[0].split('\t')
		elif w[0] == 'P2':
			w[0] = sentence[1].split('\t')[0].replace('+NNGIT+V+Ind+1Sg+3SgO', '+V+ContNeg+3SgO')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P3':
			w[0] = sentence[0].split('\t')[0].replace('+Rel+Sg', '+Abs+Sg')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P4':
			w = sentence[1].split('\t')
		elif w[0] == 'P5':
			w[0] = sentence[2].split('\t')[0].replace('+NNGIT+V+Ind+3Sg+3SgO', '+V+ContNeg+3SgO')
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
