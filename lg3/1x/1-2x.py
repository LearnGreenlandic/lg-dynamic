#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('1x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'TA\+manna\+Pron\+Abs\+Sg\s'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(nalunar|nalә\+Sem/L\+QAR).*(V\+Ind\+3Sg|V\+Cau\+4Sg)\s'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(Geo|Sem/(Hfam|Fem|Mask)\+KKUT).*\+Trm'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(run\+|reach|leave).*(V\+Ind\+(1Sg|2Sg|1Pl|2Pl))\s'), '\t@PRED'),
	['.\t.\t@CLB'],
	])

cartesian()

Qs = []
def q(sentence):
	Q = []
	for w in sentence:
		w = w.split('\t')
		Q.append(w)
	Qs.append([Q, trim_ucfirst(' '.join([w[1] for w in Q]))])

for sentence in S.sentences:
	q(sentence)

for q in Qs:
	print(f'{q[1]}')

write_qs(Qs, txt=True)
