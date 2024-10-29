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
	['ippassaq+Adv\tippassaq\t@CL-ADVL>'],
	sfx(C() | Grep(r'Sem/(Mask|Fem|Hnat).*Abs\+Sg|Sem/Hfam\+N\+Abs\+Sg\+1SgPoss') | Inv(r'INNAQ|TUQ|NIQ') | Inv(r'Hnat.*Poss'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst).*(N|Prop)\+Lok\+Sg') | Inv(r'IP|INNAQ|N\+Lok\+Sg\+3PlPoss'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(asa\+Sem/socialize|ilinniartip\+Sem/teach|naapip\+Sem/encounter|taa\+Sem/name|taku\+Sem/see).*\+Int\+2Sg\+3SgO') | Inv(r'TAR|SSA|NNGIT'), '\t@ADVL>'),
	['?\t?\t@CLB'],

	['⇒'],

	['naamik\tnaamik\t@INTERJ'],
	[',\t,\t@COMMA'],
	['ippassaq+Adv\tippassaq\t@CL-ADVL>'],
	['P1\tP1\t@OBJ>'],
	['P3\tP3\t@ADVL>'],
	['P2\tP2\t@PRED'],
	['.\t.\t@CLB'],
	['kisianni\tkisianni\t@CONJ'],
	['aqagu+Adv\taqagu\t@ADVL>'],
	['P3\tP3\t@ADVL>'],
	['P4\tP4\t@PRED'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['ippassaq+Adv\tippassaq\t@CL-ADVL>'],
	sfx(C() | Grep(r'Sem/(Mask|Fem|Hnat).*Abs\+Sg|Sem/Hfam\+N\+Abs\+Sg\+1SgPoss') | Inv(r'INNAQ|TUQ|NIQ') | Inv(r'Hnat.*Poss'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst).*(N|Prop)\+Lok\+Sg') | Inv(r'IP|INNAQ|N\+Lok\+Sg\+3PlPoss'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(asa\+Sem/socialize|ilinniartip\+Sem/teach|naapip\+Sem/encounter|taa\+Sem/name|taku\+Sem/see).*\+NNGIT\+V\+Int\+2Sg\+3SgO') | Inv(r'TAR|SSA'), '\t@ADVL>'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['ippassaq+Adv\tippassaq\t@CL-ADVL>'],
	['P1\tP1\t@OBJ>'],
	['P3\tP3\t@ADVL>'],
	['P5\tP5\t@PRED'],
	['.\t.\t@CLB'],
	['kisianni\tkisianni\t@CONJ'],
	['aqagu+Adv\taqagu\t@ADVL>'],
	['P3\tP3\t@ADVL>'],
	['P6\tP6\t@PRED'],
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
			w[0] = sentence[1].split('\t')[0]
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P2':
			w[0] = sentence[3].split('\t')[0].replace('+V+Int+2Sg+3SgO', '+NNGIT+V+Ind+1Sg+3SgO')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P3':
			w = sentence[2].split('\t')
		elif w[0] == 'P4':
			w[0] = sentence[3].split('\t')[0].replace('+V+Int+2Sg+3SgO', '+SSA+V+Ind+1Sg+3SgO')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P5':
			w = sentence[3].split('\t')
		elif w[0] == 'P6':
			w[0] = sentence[3].split('\t')[0].replace('+NNGIT+V+Int+2Sg+3SgO', '+SSA+V+Ind+1Sg+3SgO')
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
