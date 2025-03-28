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
	sfx(C() | Grep(r'Sem/(think|say).*V\+Ind\+1Sg\s') | Inv(r'(QQU|GIARTUR|NIAR|VALLAAR|KAR|IP|QQAAR\+TARIAQAR|LLUAR|NIRU|TAQ|SSA)'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/(Geo|inst).*Trm') | Inv(r'(KKUT|KAR|SSAQ|INNAQ|PAK)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(run|reach).*SSA.*(Cont|ContNeg)\+1Sg') | Inv(r'(KAR|KKUT)'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Mask|Fem).*Abs\+Sg') | Inv(r'(KKUT|KAR|IP|NIQ)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(think|say).*V\+Ind\+3Sg\s') | Inv(r'(QQU|GIARTUR|NIAR|VALLAAR|KAR|IP|QQAAR\+TARIAQAR|LLUAR|NIRU|TAQ|SSA)'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/(Geo|inst).*Trm') | Inv(r'(KKUT|KAR|SSAQ|INNAQ|PAK)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(run|reach).*SSA.*(Cont|ContNeg)\+4Sg') | Inv(r'(KAR|KKUT)'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Mask|Fem).*Abs\+Sg') | Inv(r'(KKUT|KAR|IP|NIQ)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(think|say).*V\+Ind\+3Sg\s') | Inv(r'(QQU|GIARTUR|NIAR|VALLAAR|KAR|IP|QQAAR\+TARIAQAR|LLUAR|NIRU|TAQ|SSA)'), '\t@PRED'),
	sfx(C() | Grep(r'uanga.*Abs\+1Sg\s'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst).*Trm') | Inv(r'(KKUT|KAR|SSAQ|INNAQ|PAK)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(run|reach).*SSA.*Par\+1Sg') | Inv(r'(KAR|KKUT)'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'uanga.*Abs\+1Sg\s'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(think|say).*V\+Ind\+1Sg\s') | Inv(r'(QQU|GIARTUR|NIAR|VALLAAR|KAR|IP|QQAAR\+TARIAQAR|LLUAR|NIRU|TAQ|SSA)'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/(Mask|Fem).*Abs\+Sg') | Inv(r'(KKUT|KAR|IP|NIQ)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst).*Trm') | Inv(r'(KKUT|KAR|SSAQ|INNAQ|PAK)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(run|reach).*SSA.*Par\+3Sg') | Inv(r'(KAR|KKUT)'), '\t@CL-<CIT'),
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
