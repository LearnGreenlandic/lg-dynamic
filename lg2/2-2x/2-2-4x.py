#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('2-2x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'(Sem/think.*Ind\+1Sg)|(^nalu.*NNGIT.*Ind\+1Sg\+3SgO)|(^eqqaama.*1Sg\+3SgO)') | Inv(r'(TUQ\+U)|(GUSUP.*TAR\+)') | Inv(r'\+(LI|LU|UNA)\b'), '\t@PRED'),
	#['(nil)\t(nil)\t@SUBJ>'],
	sfx(C() | Grep(r'^(aasaru|aqagu|aqaguagu)\+') | Inv(r'\+(LI|LU|UNA)\b'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*(Trm|Abl)') | Inv(r'\+(LI|LU|UNA)\b'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(aallar|tikip).*SSA\+V\+Cont\+1Sg') | Inv(r'NNGIT|TUQ\+U') | Inv(r'\+(LI|LU|UNA)\b'), '\t@CL-<CIT'),
	])
S.patterns.append([
	sfx(C() | Grep(r'(Sem/think.*Ind\+1Sg)|(^nalu.*NNGIT.*Ind\+1Sg\+3SgO)|(^eqqaama.*1Sg\+3SgO)') | Inv(r'(TUQ\+U)|(GUSUP.*TAR\+)') | Inv(r'\+(LI|LU|UNA)\b'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Fem|Mask).*Abs)|(Sem/Hfam\+N\+Abs.*1SgPoss)') | Inv(r'\+(QAR|INNAQ|NIQ|LIRI|PAK)') | Inv(r'\+(LI|LU|UNA)\b'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aasaru|aqagu|aqaguagu)\+') | Inv(r'\+(LI|LU|UNA)\b'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo.*(Trm|Abl)') | Inv(r'\+(LI|LU|UNA)\b'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(aallar|tikip).*SSA\+V\+Par\+3Sg') | Inv(r'\+(NNGIT|TUQ\+U|TAR)\+') | Inv(r'\+(LI|LU|UNA)\b'), '\t@CL-<CIT'),
	])

cartesian()

Qs = []
for sentence in S.sentences:
	q = [w.split('\t') for w in sentence]
	Qs.append(q)

for q in Qs:
	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([w[1] for w in q]))
	print(f'{q}')

write_qs(Qs)
