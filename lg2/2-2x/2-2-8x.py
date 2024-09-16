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
	sfx(C() | Grep(r'(^(kalaaleq|qallunaaq)|(Sem/(Fem|Mask|Hprof))).*Abs\+Sg\+UNA\b') | Inv(r'\+INNAQ') | Inv(r'\+(LI|LU)\b'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aallar|ajor|ilinniar|piareer|pikkorip|pizza.*TUR|whisky.*TUR).*Par\+3Sg') | Inv(r'\+(TUQ\+U|MIU|LIRI|INNAQ|PAK\+SUAQ\+QAR\+Sem/have\+LAAR)') | Inv(r'ilinniarnertuunngorniarfik|ilinniartitsisoq') | Inv(r'\+(LI|LU|UNA)\b'), '\t@PRED'),
	])
S.patterns.append([
	sfx(C() | Grep(r'^uanga.*Abs\+1Sg\+UNA\b') | Inv(r'\+INNAQ') | Inv(r'\+(LI|LU)\b'), '\t@SUBJ>'),
	sfx(C() | Grep(r'^(aallar|ajor|ilinniar|piareer|pikkorip|pizza.*TUR|whisky.*TUR).*Par\+1Sg') | Inv(r'\+(TUQ\+U|MIU|LIRI|INNAQ|PAK\+SUAQ\+QAR\+Sem/have\+LAAR)') | Inv(r'ilinniarnertuunngorniarfik|ilinniartitsisoq') | Inv(r'\+(LI|LU|UNA)\b'), '\t@PRED'),
	])

cartesian()

Qs = []
for sentence in S.sentences:
	q = [w.split('\t') for w in sentence]
	Qs.append(q)

for q in Qs:
	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([w[1] for w in q])) + '!'
	print(f'{q}')

write_qs(Qs)
