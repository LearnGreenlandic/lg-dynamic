#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('3x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'^(eqqaama\+Sem/remember|nalu\+Sem/know|nalu\+Sem/know\+NNGIT)\+V\+Int\+2Sg\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'(Sem/(Mask|Fem)\+Sem/Hum\+Prop\+Abs\+Sg|Sem/Hfam\+N\+Abs\+Sg\+1SgPoss)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aqagu|aqaguagu|aasaru|aappaagu)\+Adv'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/Geo\+Prop\+Trm\+Sg'), '\t@ADVL>'),
	sfx(C() | Grep(r'^aallar.*(NIAR\+Sem/plan|SSA|NIAR\+Sem/plan\+NNGIT)\+V\+Par\+3Sg') | Inv(r'\+TAR'), '\t@CL-<CIT'),
	['?\t?\t@CLB'],

	['⇒'],

	['naamik+Interj\tnaamik\t@INTERJ'],
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'^isumaqar\+Sem/think\+GALUAR\+V\+Ind\+1Sg'), '\t@PRED'),
	['aatsaat+Adv\taatsaat\t@ADVL>'],
	['aasaru+Adv\taasaru\t@ADVL>'],
	['P1\tP1\t@ADVL>'],
	['P2\tP2\t@CL-<CIT'],
	['.\t.\t@CLB'],
	])

cartesian()

QAs = []
def qa(sentence):
	Q = []
	A = []
	in_a = False
	for w in sentence:
		if w == '⇒':
			in_a = True
			continue

		w = w.split('\t')
		if w[0] == 'P1':
			w = sentence[3].split('\t')
		elif w[0] == 'P2':
			w = sentence[4].split('\t')

		if not in_a:
			Q.append(w)
		else:
			A.append(w)
	QAs.append([Q, A, trim_ucfirst(' '.join([w[1] for w in Q])), trim_ucfirst(' '.join([w[1] for w in A]))])

for sentence in S.sentences:
	qa(sentence)

for qa in QAs:
	print(f'{qa[2]} ⇒ {qa[3]}')

write_qas(QAs, txt=True)
