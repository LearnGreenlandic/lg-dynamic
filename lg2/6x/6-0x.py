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
	sfx(C() | Grep(r'Sem/(Geo|inst).*Lok.*IP\+V\+Cau\+1(Sg|Pl)') | Inv(r'(INNAQ|KKUT|SSAQ)'), '\t@CAU>'),
	sfx(C() | Grep(r'Sem/(Mask|Fem).*KKUT.*Abs\+Pl') | Inv(r'(Sem/Geo\+Prop|Sem/inst\+Sem/Hum\+KKUT)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(socialize|remember|teach|encounter|comprehend|mind|see|listen).*Ind\+1Sg\+3PlO'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Geo|inst).*Lok') | Inv(r'(IP|INNAQ|KKUT|SSAQ|NNGUAQ|ilinniarnertuunngorniarfik.*3PlPoss)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(persist|work|perform|learn|do_leisure)\+V\+Cau\+1(Sg|Pl)') | Inv(r'sammisare'), '\t@CAU>'),
	sfx(C() | Grep(r'Sem/(Fem\+Prop\+Rel\+Sg|Mask\+Prop\+Rel\+Sg|Hfam\+N\+Rel\+Sg\+1SgPoss)') | Inv(r'(angajoqqaaq|marluliaq)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(remember|teach|encounter|comprehend|mind|see|listen).*TAR.*Ind\+3Sg\+1SgO') | Inv(r'(TAQ|QQAAR\+TARIAQAR)'), '\t@PRED'),
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
