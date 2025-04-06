#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('6x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'(ippassaq|taamani|ullumi$)') | Inv(r'Sem/dur'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'Sem/Hfam.*Abs\+Sg\+1SgPoss') | Inv(r'(NIQ|INNAQ|SSAQ)'), '\t@OBJ>'),
	sfx(C() | Grep(r'/(Geo|inst)\+Prop\+Lok') | Inv(r'IP'), '\t@ADVL>'),
	sfx(C() | Grep(r'/(allow|comprehend|cross|encounter|leave|listen|remember|say|see|socialize|teach).*Int\+2Sg\+3SgO') | Inv(r'(TAR|NNGIT|SSA)'), '\t@ADVL>'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@CL-ADVL>'],
	['P2\tP2\t@OBJ>'],
	['P3\tP3\t@ADVL>'],
	['P4\tP4\t@PRED'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(ippassaq|taamani|ullumi$)') | Inv(r'Sem/dur'), '\t@CL-ADVL>'),
	sfx(C() | Grep(r'Sem/Hfam.*Abs\+Sg\+1SgPoss') | Inv(r'(NIQ|INNAQ|SSAQ)'), '\t@OBJ>'),
	sfx(C() | Grep(r'/(Geo|inst)\+Prop\+Lok') | Inv(r'IP'), '\t@ADVL>'),
	sfx(C() | Grep(r'/(allow|comprehend|cross|encounter|leave|listen|remember|say|see|socialize|teach).*NNGIT\+V\+Int\+2Sg\+3SgO') | Inv(r'(TAR|SSA|TAQ)'), '\t@ADVL>'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@CL-ADVL>'],
	['P2\tP2\t@OBJ>'],
	['P3\tP3\t@ADVL>'],
	['P4\tP4\t@PRED'],
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
			w = sentence[0].split('\t')
		elif w[0] == 'P2':
			w[0] = sentence[1].split('\t')[0].replace('+1SgPoss', '+2SgPoss')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P3':
			w = sentence[2].split('\t')
		elif w[0] == 'P4':
			w[0] = sentence[3].split('\t')[0].replace('+Int+2Sg', '+Ind+1Sg')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]

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
