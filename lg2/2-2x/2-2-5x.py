#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('2-2x-corpus.txt')

S.patterns.append([
	C() | Grep(r'Sem/Geo\+.*Lok') | Inv(r'\+MIU') | Inv(r'\+(LI|LU|UNA)\b'),
	C() | Grep(r'^(nuliaq|anaana|ataata|ila|meeraq).*\+QAR\+Sem/have\+V.*Ind\+1Sg') | Inv(r'\+(INNAQ|PAK\+SUAQ)') | Inv(r'\+(LI|LU|UNA)\b'),
	['.\t.'],
	['LU\tLU'],
	C() | Grep(r'^(nuup|aallar).*\+(SSA|TARIAQAR).*Ind\+1Sg') | Inv(r'\+(TAR|NNGIT|TUQ\+U)\+') | Inv(r'\+(LI|LU|UNA)\b'),
	])

cartesian()

QAs = []
def qa(sentence):
	global QAs
	Q = []
	A = []
	for i,w in enumerate(sentence):
		w = w.split('\t')
		if w[0] == 'LU':
			# In the question, substitute the placeholder for the first word in Trm
			w[0] = sentence[0].split('\t')[0].replace('+Lok', '+Trm')
			if w[0] not in S.corpus_kv:
				return
			Q.append([w[0], S.corpus_kv[w[0]]])

			# In the answer, substitute the placeholder with the Trm'ed word plus LU
			w[0] = w[0] + '+LU'
			if w[0] not in S.corpus_kv:
				return
			A.append([w[0], S.corpus_kv[w[0]]])
		else:
			Q.append(w)
			if i == 4:
				w[0] = w[0].replace('+Ind+', '+Cont+')
				if w[0] not in S.corpus_kv:
					return
			if w[0] != '.':
				A.append([w[0], S.corpus_kv[w[0]]])

	QAs.append([Q, A])

for sentence in S.sentences:
	qa(sentence)

QA_good = []
for qa in QAs:
	QA_good.append(qa)

	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([s[1] for s in qa[0]])) + '.'
	a = ucfirst(' '.join([s[1] for s in qa[1]])) + '.'
	print(f'{q} => {a}')

write_qas(QA_good)
