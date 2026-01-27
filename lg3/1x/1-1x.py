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
	sfx(C() | Grep(r'Sem/H.*Abs\+Sg') | Inv(r'^(aappaq|nuliaq|ui).*PlPoss') | Inv(r'^(qallunaaq|tusagassiortoq|arnaq|angut).*Poss') | Inv(r'(alla\+|4(Sg|Pl)Poss)'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(iluamik|ippassaq|kiisa|maani|massakkut|pavani|taamani|uani|ullumi)\+Adv'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(hurt|politing|watch|chase).*Ind\+(1Sg|2Sg|1Pl|2Pl)\+3SgO\s') | Inv(r'(SSA|TAR)\+'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'KKUT\+Prop\+Rel\+Pl') | Inv(r'Sem/inst'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/H.*Abs\+Pl') | Inv(r'^(qallunaaq|tusagassiortoq|arnaq|angut).*Poss') | Inv(r'^(anaana|ataata|nuliaq|ui|aappaq).*Pl\+(1|2|3|4)SgPoss') | Inv(r'3(Sg|Pl)Poss'), '\t@OBJ>'),
	sfx(C() | Grep(r'(kingusiinnaq|tamatigut|upernaaq\+Sem/per\+N\+Via|aasaq\+Sem/temp\+N\+Via|ukioq\+Sem/dur\+N\+Via).*'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(hurt|politing|watch|chase).*TAR\+V\+Ind\+3Pl\+3PlO\s'), '\t@PRED'),
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
