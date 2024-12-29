#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('5x-corpus.txt')
'''
S.patterns.append([
	sfx(C() | Grep(r'Sem/(Geo|inst\+Sem/Hum).*\+Lok') | Inv(r'\+IP'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(teach|socialize|use|complete_process|encounter|know|work|mind|see)\+TAQ.*QAR\+V\+Ind\+1Sg') | Inv(r'(LIR|QQAAR|know\+TAQ\+SSAQ|socialize\+TAQ\+SSAQ)'), '\t@PRED'),
	['.\t.\t@CLB'],
	['P1\tP1\t@PRED'],
	['.\t.\t@CLB'],

	['⇒'],

	['P2\tP2\t@ADVL>'],
	['P3\tP3\t@CAU>'],
	['P4\tP4\t@PRED'],
	['.\t.\t@CLB'],
	])
'''
S.patterns.append([
	sfx(C() | Grep(r'Sem/Hfam\+N\+Abs\+Sg\+1SgPoss'), '\t@OBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst\+Sem/Hum).*\+Lok') | Inv(r'\+IP'), '\t@ADVL>'),
	sfx(C() | Grep(r'Sem/(teach|socialize|encounter|see).*SSA\+V\+\Ind\+1Sg\+3SgO'), '\t@PRED'),
	['.\t.\t@CLB'],
	['P5\tP5\t@PRED'],
	['.\t.\t@CLB'],

	['⇒'],

	['P6\tP6\t@OBJ>'],
	['P7\tP7\t@ADVL>'],
	['P8\tP8\t@CAU>'],
	['P9\tP9\t@PRED'],
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
			w[0] = sentence[0].split('\t')[0].replace('+Lok', '+Trm') + '+KAR+V+Ind+1Sg'
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P2':
			w = sentence[0].split('\t')
		elif w[0] == 'P3':
			w[0] = sentence[1].split('\t')[0].replace('+Ind', '+Cau')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P4':
			w = Q[3]
		elif w[0] == 'P5':
			w[0] = sentence[1].split('\t')[0].replace('+Lok', '+Trm') + '+KAR+SSA+V+Ind+1Sg'
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P6':
			w = sentence[0].split('\t')
		elif w[0] == 'P7':
			w = sentence[1].split('\t')
		elif w[0] == 'P8':
			w[0] = sentence[2].split('\t')[0].replace('+Ind', '+Cau')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P9':
			w = Q[4]

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