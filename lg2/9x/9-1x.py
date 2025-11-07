#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('9x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Prop\+Lok\+(Sg|Pl)\s') | Inv(r'Sem/inst\+KKUT') | Inv(r'(Tusagassiornermik|Ilisimatusarfik).*Pl\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(require|socialize|teach|chase|encounter|serve|cross|say|see)\+(SSA|NIAR\+Sem/plan)(\+NNGIT)?\+V\+Ind\+1(Sg|Pl)\+3SgO') | Inv(r'^asa'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(Mask|Fem)\+Prop\+Rel\+Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Prop\+Lok\+(Sg|Pl)\s') | Inv(r'Sem/inst\+KKUT') | Inv(r'(Tusagassiornermik|Ilisimatusarfik).*Pl\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(require|socialize|teach|chase|encounter|serve|cross|say|see)\+(SSA|NIAR\+Sem/plan)(\+NNGIT)?\+V\+Ind\+3Sg\+3SgO') | Inv(r'^asa'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(Mask|Fem)\+KKUT\+Prop\+Rel\+Pl'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Prop\+Lok\+(Sg|Pl)\s') | Inv(r'Sem/inst\+KKUT') | Inv(r'(Tusagassiornermik|Ilisimatusarfik).*Pl\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(require|socialize|teach|chase|encounter|serve|cross|say|see)\+(SSA|NIAR\+Sem/plan)(\+NNGIT)?\+V\+Ind\+3Pl\+3SgO') | Inv(r'^asa'), '\t@PRED'),
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
