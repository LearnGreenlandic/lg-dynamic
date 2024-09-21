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
	sfx(C() | Grep(r'Sem/inst.*Lok') | Inv(r'\+(INNAQ|3PlPoss)') | Inv(r'\+(LI|LU|UNA)\b'), '\t@ADVL>'),
	sfx(C() | Grep(r'(^(ilinniar\+|suli)|(Sem/(food|drink-h|drink)\+TUR)).*Ind\+1Sg') | Inv(r'\+(LI|LU|UNA)\b'), '\t@PRED'),
	['⇒\t⇒\t⇒'], # '⇒' is U+21D2 Rightwards Double Arrow
	['P1\tP1\t@ADVL>'],
	['P2\tP2\t@OBJ>'],
	sfx(C() | Grep(r'^TA\+una\+Pron\+Abs\+Sg') | Inv(r'\+(LI|LU|UNA)\b'), '\t@N<'),
	sfx(C() | Grep(r'^(pi\+Sem/relate\+V\+|eqqaama\+).*Ind\+1Sg\+3SgO') | Inv(r'\+(TAR|SSA|TARIAQAR)\+') | Inv(r'\+(LI|LU|UNA)\b'), '\t@PRED'),
	])

cartesian()

Qs = []
def q(sentence):
	Q = []
	for w in sentence:
		w = w.split('\t')
		if w[0] == 'P1':
			w = sentence[0].split('\t')
		elif w[0] == 'P2':
			w[0] = sentence[1].split('\t')[0].replace('+V+Ind+1Sg', '+NIQ+N+Abs+Sg+1SgPoss')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		Q.append(w)
	Qs.append(Q)

for sentence in S.sentences:
	q(sentence)

for q in Qs:
	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([w[1] for w in q])) + '.'
	print(f'{q}')

write_qs(Qs)
