#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('6x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'ilagǝ\+Sem/socialize\+V\+Ind\+3Sg\+1SgO'), '\t@PRED'),
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'Sem/(Geo|inst)\+Prop\+(Trm|Abl)') | Inv(r'KAR'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(run|reach|leave|continue).*Ind\+3Sg') | Inv(r'(QQU|NIRU|SgO|PlO|IP|KAR)'), '\t@PRED'),
	['.\t.\t@CLB'],

	['⇒'],

	sfx(C() | Grep(r'ilagǝ\+Sem/socialize\+V\+Cont\+1SgO'), '\t@ADVL>'),
	['P1\tP1\t@ADVL>'],
	['P2\tP2\t@PRED'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Mask|Fem)\+KKUT\+Prop\+Abs'), '\t@OBJ>'),
	sfx(C() | Grep(r'ilagǝ\+Sem/socialize\+V\+Ind\+1Pl\+3PlO\s'), '\t@PRED'),
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'Sem/(Geo|inst)\+Prop\+(Trm|Abl)') | Inv(r'KAR'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(run|reach|leave|continue).*Ind\+1Pl') | Inv(r'(QQU|NIRU|SgO|PlO|IP|KAR|TAQ|GIARTUR\+SINNAA|nangip\+Sem/continue\+NIQAR)'), '\t@PRED'),
	['.\t.\t@CLB'],

	['⇒'],

	['P3\tP3\t@OBJ>'],
	sfx(C() | Grep(r'ilagǝ\+Sem/socialize\+V\+Cont\+3PlO'), '\t@ADVL>'),
	['P4\tP4\t@ADVL>'],
	['P5\tP5\t@PRED'],
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
			w = sentence[2].split('\t')
		elif w[0] == 'P2':
			w = sentence[3].split('\t')
		elif w[0] == 'P3':
			w = sentence[0].split('\t')
		elif w[0] == 'P4':
			w = sentence[3].split('\t')
		elif w[0] == 'P5':
			w = sentence[4].split('\t')

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
