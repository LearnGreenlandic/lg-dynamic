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
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)\+V\+Ind\+1(Sg|Pl)\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Pl\+1SgPoss\s|(Mask|Fem)\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Prop\+Lok\+(Sg|Pl)\s') | Inv(r'Sem/inst\+KKUT') | Inv(r'(Tusagassiornermik|Ilisimatusarfik).*Pl\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(cross|require|socialize|teach|encounter|serve|see)\+(SSA|NIAR\+Sem/plan).*(Cont|ContNeg)\+3SgO') | Inv(r'GALUAR'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'^(.*Sem/(Fem|Mask)\+Prop|ilinniarnertooq\+Sem/Hprof\+N|ilinniartoq\+Sem/Hprof\+N|oqaasilerisoq\+Sem/Hprof\+N|sakkutooq\+Sem/Hprof\+N|tusagassiortoq\+Sem/Hprof\+N|eqqumiitsuliortoq\+Sem/Hprof\+N)\+Rel\+Sg') | Inv(r'Poss'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)\+V\+Ind\+3Sg\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Pl\+1SgPoss\s|(Mask|Fem)\+KKUT\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq|aappaq|ui|marluliaq|kunngi|ataata|anaana)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Prop\+Lok\+(Sg|Pl)\s') | Inv(r'Sem/inst\+KKUT') | Inv(r'(Tusagassiornermik|Ilisimatusarfik).*Pl\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(cross|require|socialize|teach|encounter|serve|see)\+(SSA|NIAR\+Sem/plan).*(Cont|ContNeg)\+3PlO') | Inv(r'GALUAR'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)\+KKUT\+N\+Rel\+Pl|(Mask|Fem)\+KKUT\+Prop\+Rel)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)\+V\+Ind\+3Pl\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Pl\+1SgPoss\s|(Mask|Fem)\+KKUT\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq|aappaq|ui|marluliaq|kunngi|ataata|anaana)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Prop\+Lok\+(Sg|Pl)\s') | Inv(r'Sem/inst\+KKUT') | Inv(r'(Tusagassiornermik|Ilisimatusarfik).*Pl\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(cross|require|socialize|teach|encounter|serve|see)\+(SSA|NIAR\+Sem/plan).*(Cont|ContNeg)\+3PlO') | Inv(r'GALUAR'), '\t@CL-<CIT'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(remember|think|assume|say|comprehend)\+V\+Ind\+1(Sg|Pl)\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'illit\+Pron\+Rel\+2Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi)'), '\t@ADVL>'),
	sfx(C() | Grep(r'Prop\+Lok\+(Sg|Pl)\s') | Inv(r'Sem/inst\+KKUT') | Inv(r'(Tusagassiornermik|Ilisimatusarfik).*Pl\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'(Sem/(Hfam|Hprof)(\+KU)?\+N\+Abs\+Pl\+1SgPoss\s|(Mask|Fem)\+KKUT\+Prop\+Abs)') | Inv(r'(angajoqqaaq|ilinniarnertooq|ilinniartoq|oqaasilerisoq|sakkutooq|tusagassiortoq|eqqumiitsuliortoq|aappaq|ui|marluliaq|kunngi|ataata|anaana)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(cross|require|socialize|teach|encounter|serve|see)\+(SSA|NIAR\+Sem/plan).*Par\+2Sg\+3PlO') | Inv(r'GALUAR'), '\t@CL-<CIT'),
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
