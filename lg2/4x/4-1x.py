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
	sfx(C() | Grep(r'Sem/Fem.*Abs\+Sg') | Inv(r'NIQ'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(nuliaq|anaana|qatanngut|aleqa|naja|nuka\+|angaju\+).*GE\+Sem/have\+V\+Int\+2Sg\+3SgO') | Inv(r'INNAQ|PAK'), '\t@PRED'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@OBJ>'],
	['P2\tP2\t@PRED'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/Mask.*Abs\+Sg') | Inv(r'NIQ'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(ui\+|ataata\+|qatanngut\+|ani\+|aqqalu\+|nuka\+|angaju\+).*GE\+Sem/have\+V\+Int\+2Sg\+3SgO') | Inv(r'INNAQ|PAK'), '\t@PRED'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@OBJ>'],
	['P2\tP2\t@PRED'],
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
			w[0] = sentence[1].split('\t')[0].replace('+V+Int+2Sg+3SgO', '+V+Ind+1Sg+3SgO')
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
