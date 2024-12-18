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
	sfx(C() | Grep(r'^(eqqaama\+Sem/remember|nalu\+Sem/know|nalu\+Sem/know\+NNGIT)\+V\+Int\+2Sg\+3Sg'), '\t@PRED'),
	sfx(C() | Grep(r'TA\+manna\+Pron\+Abs\+Sg'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(sammisare\+Sem/work|ator\+Sem/use|allap\+Sem/create-semantic)\+(SSA|TARIAQAR\+Sem/must)\+V\+Cont\+3SgO'), '\t@CL-<CIT'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap+Interj\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P1\tP1\t@PRED'],
	sfx(C() | Grep(r'TA\+manna\+Pron\+Abs\+Sg'), '\t@OBJ>'),
	['P2\tP2\t@CL-<CIT'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'^(arnaq|angut|meeraq|nukappiaraq)\+Sem/H\+N\+Rel\+Pl'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(eqqaama\+Sem/remember|eqqaama\+Sem/remember\+NNGIT|eqqaama\+Sem/remember\+TARIAQAR\+Sem/must|eqqaama\+Sem/remember\+TARIAQAR\+Sem/must\+NNGIT|nalu\+Sem/know|nalu\+Sem/know\+NNGIT)\+V\+Ind\+3Pl\+3SgO'), '\t@PRED'),
	sfx(C() | Grep(r'TA\+manna\+Pron\+Abs\+Sg'), '\t@OBJ>'),
	sfx(C() | Grep(r'^(sammisare\+Sem/work|ator\+Sem/use|allap\+Sem/create-semantic)\+(SSA|TARIAQAR\+Sem/must)\+V\+Cont\+3SgO'), '\t@CL-<CIT'),
	['?\t?\t@CLB'],

	['⇒'],

	['aap+Interj\taap\t@INTERJ'],
	[',\t,\t@COMMA'],
	['P3\tP3\t@SUBJ>'],
	['P4\tP4\t@PRED'],
	sfx(C() | Grep(r'TA\+manna\+Pron\+Abs\+Sg'), '\t@OBJ>'),
	['P5\tP5\t@CL-<CIT'],
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
			w[0] = sentence[0].split('\t')[0].replace('+Int+2Sg+3Sg', '+Ind+1Sg+3Sg')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P2':
			w = sentence[2].split('\t')
		elif w[0] == 'P3':
			w = sentence[0].split('\t')
		elif w[0] == 'P4':
			w = sentence[1].split('\t')
		elif w[0] == 'P5':
			w = sentence[3].split('\t')

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
