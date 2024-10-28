#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('2-3x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'^uanga\+Pron\+Abs\+1Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^ilissi\+Pron\+Abs\+2Pl'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst|Lh).*Lok\+Sg') | Inv(r'(IP|INNAQ|najugaq)') | Inv(r'Sem/(Lh|inst).*3PlPoss'), '\t@ADVL>'),
	sfx(C() | Grep(r'Ind\+1Sg\+2PlO') | Inv(r'(pi|SSA|Sem/create-semantic|nalu.*(NIAR|TARIAQAR|TAR))'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Geo|inst|Lh).*Lok\+Sg') | Inv(r'(IP|INNAQ|najugaq)') | Inv(r'Sem/(Lh|inst).*3PlPoss'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'^(anaana|angut|arnaq|ilinniartoq\+Sem/Hprof|kalaaleq|meeraq|nalu\+Sem/know\+NNGIT\+TAQ|oqaasilerisoq|ilinniartitsisoq|qallunaaq).*Rel\+Pl'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^tamaq\+N\+Nom\+4Pl'), '\t@N<'),
	sfx(C() | Grep(r'Ind\+3Pl\+1SgO') | Inv(r'(pi|SSA|Sem/create-semantic|nalu.*(NIAR|TARIAQAR|TAR))'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'^(anaana|angut|arnaq|ilinniartoq\+Sem/Hprof|kalaaleq|meeraq|nalu\+Sem/know\+NNGIT\+TAQ|oqaasilerisoq|ilinniartitsisoq|qallunaaq).*Rel\+Pl'), '\t@SUBJ>'),
	sfx(C() | Grep(r'(Sem/Hfam|ilinniartitsisoq).*Abs\+Sg\+1SgPoss') | Inv(r'(NIQ|INNAQ)'), '\t@OBJ>'),
	sfx(C() | Grep(r'Ind\+3Pl\+3SgO') | Inv(r'(pi|SSA|Sem/create-semantic|nalu.*(NIAR|TARIAQAR|TAR))'), '\t@PRED'),
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

write_qs(Qs)
