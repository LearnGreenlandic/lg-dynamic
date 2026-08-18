#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('0xx-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'(Sem/Geo|Sem/Hum|Sem/inst).*(Trm|Abl)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(tikip|aallar).*Ind.*(1Sg|1Pl)\s') | Inv(r'TUQ\+U\+Sem/copula'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(Sem/Hnat|Sem/Mask|Sem/Fem).*(N|Prop)\+Abs\+Sg') | Inv(r'(QAR|LI|LU|UNA|1SgPoss)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(ullumi|ippassaq)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(Sem/Geo|Sem/Hum|Sem/inst).*(Trm|Abl)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(tikip|aallar).*Ind.*3Sg') | Inv(r'TUQ\+U\+Sem/copula') | Inv(r'(SSA|TAR)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(Sem/Hnat|Sem/Mask|Sem/Fem).*(N|Prop)\+Abs\+Sg') | Inv(r'(QAR|LI|LU|UNA|1SgPoss)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(ullumi|aqagu|aqaguagu)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(Sem/Geo|Sem/Hum|Sem/inst).*(Trm|Abl)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(tikip|aallar).*SSA.*Ind.*3Sg') | Inv(r'TUQ\+U\+Sem/copula') | Inv(r'TAR'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(ullumi|aqagu|aqaguagu)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(Sem/Geo|Sem/Hum|Sem/inst).*Lok') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(ajor|allap|atuar|ilinniar|pikkorip|oqalup|suli).*SSA.*Ind.*(1Sg|1Pl)') | Inv(r'TUQ\+U\+Sem/copula') | Inv(r'(TAR|LI|LU|SgO|PlO)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(Sem/Hnat|Sem/Mask|Sem/Fem).*(N|Prop)\+Abs\+Sg') | Inv(r'(QAR|LI|LU|UNA|1SgPoss)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(ullumi|ippassaq)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(Sem/Geo|Sem/Hum|Sem/inst).*Lok') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(ajor|allap|atuar|ilinniar|pikkorip|oqalup|suli).*Ind.*3Sg') | Inv(r'TUQ\+U\+Sem/copula') | Inv(r'(TAR|SSA|LI|LU|SgO|PlO)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(Sem/Hnat|Sem/Mask|Sem/Fem).*(N|Prop)\+Abs\+Sg') | Inv(r'(QAR|LI|LU|UNA|1SgPoss)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(ullumi|ippassaq)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(Sem/Geo|Sem/Hum|Sem/inst).*Lok') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(eqqaama|asa|ilinniartip|naapip|taku).*Ind.*3SgO') | Inv(r'TUQ\+U\+Sem/copula') | Inv(r'(TAR|SSA|LI|LU)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(ullumi|ippassaq)') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(Sem/Geo|Sem/Hum|Sem/inst).*Lok') | Inv(r'(LI|LU|UNA)'), '\t@ADVL>'),
	sfx(C() | Grep(r'(eqqaama|asa|ilinniartip|naapip|taku).*Ind.*2PlO') | Inv(r'TUQ\+U\+Sem/copula') | Inv(r'(TAR|SSA|LI|LU)'), '\t@PRED'),
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
