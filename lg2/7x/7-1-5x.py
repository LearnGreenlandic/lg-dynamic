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
	sfx(C() | Grep(r'(ippassaq|taamani|ullumi$)') | Inv(r'Lok'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'Sem/(Fem|Mask|Hprof)\+(N|Prop)\+Abs\+Sg') | Inv(r'(Poss|ikiorti)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(inst|Geo).*Lok') | Inv(r'(IP|KKUT|LIR\+TAQ|SSAQ|PAK|INNAQ|meeqqerivik.*Poss|ilinniarnertuunngorniarfik.*Poss)'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(aallar.*QQU|akuere|socialize|ataasinnguaq.*TUR\+QQU|eqqaama|eqqarsatigǝ|ikiortә.*GE|ilagǝ|ilinniartip|malip|naapip|oqarfigǝ|paarǝ|paasi|pizza.*TUR\+QQU|qimap|sammisare|soqutige|taa$|taku|tusar|tutsiuteqqip.*QQU).*Ind\+2Pl\+3SgO') | Inv(r'(LIR\+QQU|TAR|NIQAR|SSA|GIARTUR|INNAQ|PAK|(tusar|paasi).*TAQ|SSAQ.*SSA\+)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi$)') | Inv(r'Lok'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'KKUT\+(N|Prop)\+Abs\+Pl') | Inv(r'(NIQ|LIR\+TAQ|INNAQ|SSAQ|alla|TUQ\+KKUT|Sem/inst)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(inst|Geo).*Lok') | Inv(r'(IP|KKUT|LIR\+TAQ|SSAQ|PAK|INNAQ|meeqqerivik.*Poss|ilinniarnertuunngorniarfik.*Poss)'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(akuere|socialize|eqqaama|eqqarsatigǝ|ikiortә.*GE|ilagǝ|ilinniartip|malip|naapip|oqarfigǝ|paarǝ|paasi|qimap|sammisare|soqutige|taa$|taku|tusar).*SSA(\+NNGIT)?\+V\+Ind\+2Pl\+3PlO') | Inv(r'(LIR\+QQU|TAR|NIQAR|GIARTUR|INNAQ|PAK|(tusar|paasi).*TAQ|SSAQ.*SSA\+)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(ippassaq|taamani|ullumi$)') | Inv(r'Lok'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'Sem/(H|socialize\+TAQ|think\+TAQ|teach\+TAQ).*N\+Abs\+Sg\+2PlPoss') | Inv(r'(NIQ|LIR\+TAQ|INNAQ|SSAQ|alla|eqqumiitsuliortoq|ilinniarnertooq|tusagassiortoq|sakkutooq|kalaaleq|qallunaaq|oqaasilerisoq|nukarleq|kingulleq|inersimasoq|inuusuttoq|ilinniartoq|angajoqqaaq)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(inst|Geo).*Lok') | Inv(r'(IP|KKUT|LIR\+TAQ|SSAQ|PAK|INNAQ|meeqqerivik.*Poss|ilinniarnertuunngorniarfik.*Poss)'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(aallar.*QQU|akuere|socialize|ataasinnguaq.*TUR\+QQU|eqqaama|eqqarsatigǝ|ikiortә.*GE|ilagǝ|ilinniartip|malip|naapip|oqarfigǝ|paarǝ|paasi|pizza.*TUR\+QQU|qimap|sammisare|soqutige|taa$|taku|tusar|tutsiuteqqip.*QQU).*Ind\+2Pl\+3SgO') | Inv(r'(LIR\+QQU|TAR|NIQAR|SSA|GIARTUR|INNAQ|PAK|(tusar|paasi).*TAQ|SSAQ.*SSA\+)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(aappaagu|aasaru|aqagu|aqaguagu|erniinnaq|ullumi$)') | Inv(r'Lok'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'Sem/(H|socialize\+TAQ|think\+TAQ|teach\+TAQ).*N\+Abs\+Pl\+2PlPoss') | Inv(r'(NIQ|LIR\+TAQ|INNAQ|SSAQ|alla|eqqumiitsuliortoq|ilinniarnertooq|tusagassiortoq|sakkutooq|kalaaleq|qallunaaq|oqaasilerisoq|nukarleq|kingulleq|inersimasoq|inuusuttoq|ilinniartoq|nuliaq|ui|aappaq|PAK|kunngi|ataata|anaana)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(inst|Geo).*Lok') | Inv(r'(IP|KKUT|LIR\+TAQ|SSAQ|PAK|INNAQ|meeqqerivik.*Poss|ilinniarnertuunngorniarfik.*Poss)'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(akuere|socialize|eqqaama|eqqarsatigǝ|ikiortә.*GE|ilagǝ|ilinniartip|malip|naapip|oqarfigǝ|paarǝ|paasi|qimap|sammisare|soqutige|taa$|taku|tusar).*SSA(\+NNGIT)?\+V\+Ind\+2Pl\+3PlO') | Inv(r'(LIR\+QQU|TAR|NIQAR|GIARTUR|INNAQ|PAK|(tusar|paasi).*TAQ|SSAQ.*SSA\+)'), '\t@PRED'),
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
