#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('2x-corpus.txt')

S.patterns.append([
	C() | Grep(r'(Sem/(Fem|Mask).*Abs)') | Inv(r'\+(QAR|INNAQ|NIQ|LIRI|PAK)\+') | Inv(r'\+(LI|LU|UNA)\b'),
	C() | Grep(r'^(asa|ilinniartip|naapip|sammisare|taku).*\+LAAR\+NNGIT\+.*1Sg\+3SgO') | Inv(r'\+(LI|LU|UNA)\b'),
	])

cartesian()

QAs = []
def qa(sentence):
	global QAs
	Q = []
	A = [['', 'Naamik,']]
	for w in sentence:
		w = w.split('\t')
		# Inverted logic, as we find +LAAR+NNGIT and turn it into the question
		A.append(w)
		w[0] = w[0].replace('+LAAR+NNGIT+', '+').replace('+Ind+1Sg+3SgO', '+Int+2Sg+3SgO')
		if w[0] not in S.corpus_kv:
			return
		Q.append([w[0], S.corpus_kv[w[0]]])

	QAs.append([Q, A])

for sentence in S.sentences:
	qa(sentence)

QA_good = []
for qa in QAs:
	QA_good.append(qa)

	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([s[1] for s in qa[0]])) + '?'
	a = ucfirst(' '.join([s[1] for s in qa[1]])) + '.'
	print(f'{q} => {a}')

write_qas(QA_good)
