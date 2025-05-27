#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('7x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'Sem/(H|socialize\+TAQ|think\+TAQ|teach\+TAQ).*N\+Abs\+Sg\+1SgPoss') | Inv(r'(NIQ|LIR\+TAQ|INNAQ|SSAQ|alla|eqqumiitsuliortoq|ilinniarnertooq|tusagassiortoq|sakkutooq|kalaaleq|qallunaaq|oqaasilerisoq|nukarleq|kingulleq|inersimasoq|inuusuttoq|ilinniartoq|angajoqqaaq)'), '\t@OBJ>'),
	sfx(C() | Grep(r'^oqarfigǝ.*Ind\+1Sg\+3SgO') | Inv(r'(TAQ|TIP|QQU)'), '\t@PRED'),
	sfx(C() | Grep(r'Sem/(Fem|Mask)\+KKUT\+Prop\+Rel\+Pl'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(qallunaaq|kalaaleq|MIU).*\+Rel\+Pl') | Inv(r'(Poss|QAR|SSAQ|LIR|PAK)'), '\t@POSS>'),
	sfx(C() | Grep(r'Sem/(H|socialize\+TAQ|think\+TAQ|teach\+TAQ).*N\+Abs\+Pl\+3PlPoss') | Inv(r'(NIQ|LIR\+TAQ|INNAQ|SSAQ|alla|eqqumiitsuliortoq|ilinniarnertooq|tusagassiortoq|sakkutooq|kalaaleq|qallunaaq|oqaasilerisoq|nukarleq|kingulleq|inersimasoq|inuusuttoq|ilinniartoq|PAK|kunngi|angajulleq)'), '\t@OBJ>'),
	sfx(C() | Grep(r'(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi$)') | Inv(r'Lok'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'Sem/(inst|Geo).*Lok') | Inv(r'(IP|KKUT|LIR\+TAQ|SSAQ|PAK|INNAQ|meeqqerivik.*Poss|ilinniarnertuunngorniarfik.*Poss)'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(akuere|socialize|avip|eqqaama|eqqarsatigǝ|ikiortә.*GE|ilagǝ|ilinniartip|malip|naapip|oqarfigǝ|paarǝ|paasi|qimap|sammisare|soqutige|taa$|taku|tusar).*SSA(\+NNGIT)?\+V\+Par\+3Pl\+3PlO') | Inv(r'(LIR\+QQU|TAR|NIQAR|GIARTUR|INNAQ|PAK|(tusar|paasi).*TAQ|SSAQ.*SSA\+)'), '\t@CL-<CIT'),
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
