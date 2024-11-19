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
	sfx(C() | Grep(r'Sem/Fem.*Rel\+Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'MIU\+Sem/Hnat\+N\+Abs\+Sg') | Inv(r'Danmark'), '\t@OBJ>'),
	sfx(C() | Grep(r'Gram/Dem.*Sg'), '\t@N<'),
	sfx(C() | Grep(r'^(ui\+|ataata\+|qatanngut\+|ani\+|aqqalu\+|nuka\+|angaju\+).*GE\+Sem/have\+V\+Ind\+3Sg\+3SgO') | Inv(r'INNAQ|PAK|NNGUAQ'), '\t@PRED'),
	['?\t?\t@CLB'],

	['⇒'],

	['Aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@SUBJ>'],
	['P2\tP2\t@OBJ>'],
	['P3\tP3\t@N<'],
	['P4\tP4\t@PRED'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/Fem.*Rel\+Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'MIU\+Sem/Hnat\+N\+Abs\+Sg') | Inv(r'Danmark'), '\t@OBJ>'),
	sfx(C() | Grep(r'Gram/Dem.*Sg'), '\t@N<'),
	sfx(C() | Grep(r'^(ui\+|ataata\+|qatanngut\+|ani\+|aqqalu\+|nuka\+|angaju\+).*GE\+Sem/have\+NNGIT\+V\+Ind\+3Sg\+3SgO') | Inv(r'INNAQ|PAK|NNGUAQ'), '\t@PRED'),
	['?\t?\t@CLB'],

	['⇒'],

	['Aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@SUBJ>'],
	['P2\tP2\t@OBJ>'],
	['P3\tP3\t@N<'],
	['P4\tP4\t@PRED'],
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
			w = sentence[0]
		elif w[0] == 'P2':
			w = sentence[1]
		elif w[0] == 'P3':
			w = sentence[2]
		elif w[0] == 'P4':
			w = sentence[3]

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
