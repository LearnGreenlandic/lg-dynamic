#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('2-1x-corpus.txt')

S.patterns.append([
	['-\t{t:obj-def}:'],
	C() | Grep(r'Sem/(Hnat|H\+|Hprof).*Abs') | Inv(r'^(eqqumiitsuliortoq|kalaaleq|oqaasilerisoq|qallunaaq).*(1SgPoss)') | Inv(r'\+(LI|LU|NNGIT|QAR)\b'),
	C() | Grep(r'Sem/(socialize|teach|encounter|see).*Ind\+1Sg\+3SgO')| Inv(r'\+(NNGIT|SSA|LI|LU)\b'),
	])

cartesian()

QAs = []
def q(sentence):
	global Qs
	Q = []
	A = [['-', '<br>{t:obj-idf}:']]
	for w in sentence:
		w = w.split('\t')
		Q.append(w)
		if w[0] == '-':
			continue
		w[0] = w[0].replace('+Abs', '+Ins')
		w[0] = w[0].replace('+V+Ind+1Sg+3SgO', '+TAQ+QAR+V+Ind+1Sg')
		if w[0] not in S.corpus_kv:
			return
		A.append([w[0], S.corpus_kv[w[0]]])

	QAs.append([Q, A])

for sentence in S.sentences:
	q(sentence)

for qa in QAs:
	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([s[1] for s in qa[0]]))
	a = ucfirst(' '.join([s[1] for s in qa[1]]))
	print(f'{q} => {a}')

write_qas(QAs)
