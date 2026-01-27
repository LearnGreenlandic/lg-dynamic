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
	sfx(C() | Grep(r'Sem/H.*Abs\+Sg') | Inv(r'^(aappaq|nuliaq|ui).*PlPoss') | Inv(r'^(qallunaaq|tusagassiortoq|arnaq|angut).*Poss') | Inv(r'(^alla\+|4(Sg|Pl)Poss)') | Inv(r'QAR\+Sem/have\+QATE'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(isumaqar|oqar).*Ind\+3Sg\s') | Inv(r'QATE'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/H.*Abs\+Pl') | Inv(r'^(qallunaaq|tusagassiortoq|arnaq|alla|angut).*Poss') | Inv(r'^(anaana|ataata|nuliaq|ui|aappaq).*Pl\+(1|2|3|4)SgPoss') | Inv(r'4PlPoss'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(iluamik|ippassaq|kiisa|maani|massakkut|pavani|taamani|uani|ullumi)\+Adv'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(hurt|politing|watch|chase).*(Cont|ContNeg).*\+3PlO\s'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/H.*Abs\+Sg') | Inv(r'^(aappaq|nuliaq|ui).*PlPoss') | Inv(r'^(qallunaaq|tusagassiortoq|arnaq|angut).*Poss') | Inv(r'(^alla\+|4(Sg|Pl)Poss)') | Inv(r'QAR\+Sem/have\+QATE'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(nalu\+Sem/know\+NNGIT|eqqaama|eqqarsatigǝ|ilimagǝ|paasi).*Ind\+3Sg\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/H.*Abs\+Pl') | Inv(r'^(qallunaaq|tusagassiortoq|arnaq|alla|angut).*Poss') | Inv(r'^(anaana|ataata|nuliaq|ui|aappaq).*Pl\+(1|2|3|4)SgPoss') | Inv(r'3(Sg|Pl)Poss'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(iluamik|ippassaq|kiisa|maani|massakkut|pavani|taamani|uani|ullumi)\+Adv'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(hurt|politing|watch|chase).*(Cont|ContNeg).*\+3SgO\s'), '\t@CL-<CIT'),
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
