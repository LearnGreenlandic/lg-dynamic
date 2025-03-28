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
	sfx(C() | Grep(r'(ippassaq|taamani|ullumi$)') | Inv(r'Sem/dur'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(Geo|inst).*IP\+V\+Cau\+1Sg') | Inv(r'Sem/inst.*(KKUT|SSAQ|INNAQ|PAK)'), '\t@CAU>'),
	sfx(C() | Grep(r'Sem/(Fem|Mask)\+Prop\+(Abs|Rel)\+Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(encounter|cross|leave).*Ind\+3Sg\+1SgO') | Inv(r'(TAQ|TAR|VALLAAR|SSA|NIQAR)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(ippassaq|taamani|ullumi$)') | Inv(r'Sem/dur'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(Geo|inst).*IP\+NNGIT\+V\+Cau\+1Sg') | Inv(r'Sem/inst.*(KKUT|SSAQ|INNAQ|PAK)'), '\t@CAU>'),
	sfx(C() | Grep(r'Sem/(Fem|Mask)\+Prop\+Rel\+Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(encounter|cross|leave).*NNGIT\+V\+Ind\+3Sg\+1SgO') | Inv(r'(TAQ|TAR|VALLAAR|SSA|NIQAR)'), '\t@PRED'),
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
