#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('9x-corpus.txt')

S.patterns.append([ # 1.1.1
	sfx(C() | Grep(r'^(oqar|isumaqar)\+Sem/(think|say)(\+NNGIT)?\+V\+Ind\+1Sg'), '\t@PRED'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+Cont\+1Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 1.1.2
	sfx(C() | Grep(r'^(oqar|isumaqar)\+Sem/(think|say)\+V\+Ind\+1Sg'), '\t@PRED'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+(Cont|ContNeg)\+1Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 1.2
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)(\+NNGIT)?\+V\+Ind\+1Sg\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+Cont\+1Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 2.1.1
	sfx(C() | Grep(r'^(oqar|isumaqar)\+Sem/(think|say)(\+NNGIT)?\+V\+Ind\+1(Sg|Pl)'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s|(Mask|Fem)\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+Par\+3Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 2.1.2
	sfx(C() | Grep(r'^(oqar|isumaqar)\+Sem/(think|say)\+V\+Ind\+1(Sg|Pl)'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s|(Mask|Fem)\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)(\+NNGIT)?\+V\+Par\+3Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 2.2.1
	sfx(C() | Grep(r'^(oqar|isumaqar)\+Sem/(think|say)(\+NNGIT)?\+V\+Ind\+1(Sg|Pl)'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)\+KKUT\+N\+Abs\+Pl|(Mask|Fem)\+KKUT\+Prop\+Abs)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+Par\+3Pl'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 2.2.2
	sfx(C() | Grep(r'^(oqar|isumaqar)\+Sem/(think|say)\+V\+Ind\+1(Sg|Pl)'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)\+KKUT\+N\+Abs\+Pl|(Mask|Fem)\+KKUT\+Prop\+Abs)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)(\+NNGIT)?\+V\+Par\+3Pl'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 2.3.1
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)(\+NNGIT)?\+V\+Ind\+1(Sg|Pl)\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s|(Mask|Fem)\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+Par\+3Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 2.3.2
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)\+V\+Ind\+1(Sg|Pl)\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s|(Mask|Fem)\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)(\+NNGIT)?\+V\+Par\+3Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 3.1.1
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s|(Mask|Fem)\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(oqar|isumaqar)\+Sem/(think|say)(\+NNGIT)?\+V\+Ind\+3Sg'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+Cont\+4Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 3.1.2
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Sg\+1SgPoss\s|(Mask|Fem)\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(oqar|isumaqar)\+Sem/(think|say)\+V\+Ind\+3Sg'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+(Cont|ContNeg)\+4Sg'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 3.2.1
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)\+KKUT\+N\+Rel\+Pl|(Mask|Fem)\+KKUT\+Prop\+Rel)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)(\+NNGIT)?\+V\+Ind\+3Pl\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+Cont\+4Pl'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 3.2.2
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)\+KKUT\+N\+Rel\+Pl|(Mask|Fem)\+KKUT\+Prop\+Rel)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)\+V\+Ind\+3Pl\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)\+V\+(Cont|ContNeg)\+4Pl'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([ # 3.3
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)\+KKUT\+N\+Rel\+Pl|(Mask|Fem)\+KKUT\+Prop\+Rel)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)\+V\+Ind\+3Pl\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/Geo.*KAR\+(SSA|NIAR\+Sem/plan)(\+NNGIT)?\+V\+Par\+2Sg'), '\t@CL-<CIT'),
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
