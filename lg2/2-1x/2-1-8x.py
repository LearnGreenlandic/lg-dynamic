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
	C() | Grep(r'Sem/(inst|Geo).*Lok') | Inv(r'\+(MIU|LI|LU)\b'),
	C() | Grep(r'\+TAQ\+QAR.*Ind')| Inv(r'\+(GALUAR|LI|LU)\b'),
	])

cartesian()

Qs = []
for sentence in S.sentences:
	q = [w.split('\t') for w in sentence]
	Qs.append(q)

for q in Qs:
	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([w[1] for w in q]))
	print(f'{q}')

write_qs(Qs)
