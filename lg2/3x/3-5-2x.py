#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('3x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'^(ippassaq|ullumi|taamani|aatsaat)\+Adv'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'Sem/Hfam\+N\+Abs\+Sg\+1SgPoss'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(angerlar\+Sem/reach|angerlar\+Sem/reach\+NIAR\+Sem/plan)\+V\+Cont\+4Sg'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo\+Prop\+Trm\+Sg'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(aallar).*Ind\+3Sg') | Inv(r'(TAR|SSA|NIAR)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'^(aqagu|aqaguagu|aasaru|aappaagu)\+Adv'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'^(arnaq|angut|qallunaaq|kalaaleq)\+Sem/(H|Hnat)\+N\+Abs\+Pl') | Inv(r'3SgPoss'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(angerlar\+Sem/reach|angerlar\+Sem/reach\+NIAR\+Sem/plan)\+V\+Cont\+4Pl'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo\+Prop\+Trm\+Sg'), '\t@ADVL>'),
	sfx(C() | Grep(r'^aallar.*(NIAR\+Sem/plan|SSA|NIAR\+Sem/plan\+NNGIT)\+V\+Par\+3Pl') | Inv(r'\+TAR'), '\t@CL-CIT>'),
	sfx(C() | Grep(r'isumaqar\+Sem/think\+V\+Ind\+1Sg'), '\t@PRED'),
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
