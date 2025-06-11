#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('8x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/Geo\+Prop\+Lok\+(Sg|Pl)\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(learn|work)(\+LIR)?\+V\+Ind\+3Sg\s'), '\t@PRED'),
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'Sem/(Fem|Mask).*Prop\+Rel\+Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(require|socialize|teach|chase|encounter|serve)\+(SSA|NIAR\+Sem/plan)\+V\+Cau\+4Sg\+3SgO') | Inv(r'^asa'), '\t@CAU>'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo\+Prop\+Trm\+Sg\+KAR\+(SSA|GUSUP\+Sem/wish|NIAR\+Sem/plan)\+V\+Ind\+3Sg'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Pl\+1SgPoss\s') | Inv(r'(aappaq|anaana|ataata|ilinniarnertooq|ilinniartoq|kunngi|marluliaq|sakkutooq|tusagassiortoq|ui)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/inst\+Prop\+Lok\+(Sg|Pl)\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(learn|work)(\+LIR)?\+V\+Ind\+3Pl\s'), '\t@PRED'),
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'Sem/(Fem|Mask).*Prop\+Rel\+Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(require|socialize|teach|chase|encounter|serve)(\+NIAR\+Sem/plan)?\+V\+Cau\+4Sg\+3PlO') | Inv(r'^asa'), '\t@CAU>'),
	sfx(C() | Grep(r'(ippassaq|ullumi|aatsaat|massakkut)') | Inv(r'\+N'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/inst\+Prop\+(Trm.*\+KAR|Lok.*IP)(\+(GUSUP\+Sem/wish|NIAR\+Sem/plan))?\+V\+Ind\+3Sg'), '\t@PRED'),
	['.\t.\t@CLB'],
	])

cartesian()

Qs = []
def q(sentence):
	Q = []
	prop = None
	for i,w in enumerate(sentence):
		w = w.split('\t')
		if i == 1:
			prop = re.sub(r'\+Lok.*$', '', w[0])
		if i == 7 and not w[0].startswith(prop):
			return
		Q.append(w)
	Qs.append([Q, trim_ucfirst(' '.join([w[1] for w in Q]))])

for sentence in S.sentences:
	q(sentence)

for q in Qs:
	print(f'{q[1]}')

write_qs(Qs, txt=True)
