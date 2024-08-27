#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../_lib')
from shared import *
import shared as S

load_corpus('2-1x-corpus.txt')

S.patterns.append([
	C() | Grep(r'Sem/(remember|know|think).*\+Ind\+1Sg') | Inv(r'\+(LI|LU|2PlO|TAQ|GUSUP|TUQ)\b') | Inv(r'^eqqaama.*NNGIT'),
	C() | Grep(r'^illit.*Abs')| Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'(Sem/(Geo|inst|Lh).*\+Lok)|(Pron\+Lok\+(2Sg|2Pl))')| Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/(work|learn).*\+Par\+2Sg')| Inv(r'\+(LI|LU)\b'),
	])
S.patterns.append([
	C() | Grep(r'Sem/(remember|know|think).*\+Ind\+1Sg') | Inv(r'\+(LI|LU|2PlO|TAQ|GUSUP|TUQ)\b') | Inv(r'^eqqaama.*NNGIT'),
	C() | Grep(r'Sem/(Fem|Mask).*Abs')| Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'(Sem/(Geo|inst|Lh).*\+Lok)|(Pron\+Lok\+(2Sg|2Pl))')| Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/(work|learn).*\+Par\+3Sg')| Inv(r'\+(LI|LU)\b'),
	])
S.patterns.append([
	C() | Grep(r'Sem/remember.*\+Int\+2Sg\+3SgO') | Inv(r'\+(LI|LU|GUSUP)\b'),
	C() | Grep(r'^uanga.*Abs')| Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'(Sem/(Geo|inst|Lh).*\+Lok)|(Pron\+Lok\+(2Sg|2Pl))')| Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/(work|learn).*\+Par\+1Sg')| Inv(r'\+(LI|LU)\b'),
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
