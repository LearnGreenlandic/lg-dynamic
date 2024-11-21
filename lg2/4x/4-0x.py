#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('4x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'^(aappaagu|aasaru|aqagu|aqaguagu|ullumi)\+Adv'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'\+Pron\+Rel\+1Sg'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Abs\+2Pl\s'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst|Lh).*Lok\+Sg') | Inv(r'IP|INNAQ|najugaq') | Inv(r'Sem/(Lh|inst).*3PlPoss'), '\t@ADVL>'),
	sfx(C() | Grep(r'(SSA|NIAR)+.*1Sg\+2PlO\s') | Inv(r'(GE|TAR)'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(anaana|angajulleq|angut|arnaq|eqqumiitsuliortoq|ilinniarnertooq|ilinniartoq\+Sem/Hprof|inuk|kalaaleq|meeraq|nalu\+Sem/know\+NNGIT\+TAQ|nukappiaraq|nukarleq|oqaasilerisoq|ilinniartitsisoq|qallunaaq).*Abs\+Pl\s'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst|Lh).*Trm') | Inv(r'IP|INNAQ|najugaq|KAR|PAK') | Inv(r'Sem/(Lh|inst).*3PlPoss'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(ippassaq|massakkut|taamani|ullumi)\+Adv'), '\t@ADVL>'),
	sfx(C() | Grep(r'(\+TUR\+GIARTUR|aallar)\+.*Ind\+3Pl\s') | Inv(r'SSA|TAR'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Geo|inst|Lh).*Abl') | Inv(r'Sem/(Lh|inst).*3PlPoss'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/reach.*Ind\+(1Sg|2Sg|1Pl|2Pl)'), '\t@PRED'),
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
