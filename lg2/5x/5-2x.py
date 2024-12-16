#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('5x-corpus.txt')

S.patterns.append([
	sfx(C() | Grep(r'Sem/(Geo|inst\+Sem/Hum).*\+Lok') | Inv(r'IP'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(aallartip|allap|ator|naammassi|paasi|sammisare).*TAQ\+SSAQ\+QAR\+Sem/have\+V\+Ind\+1Sg') | Inv(r'\+NNGIT'), '\t@PRED'),
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'(aappaagu|aasaru|aqagu|aqaguagu|ullumi)\+Adv'), '\t@CL-ADVL>'),
	['P1\tP1\t@ADVL>'],
	sfx(C() | Grep(r'^(aallartip|allap|ator|naammassi|paasi|sammisare).*GIARTUR\+SSA\+V\+Ind\+1Sg\+3'), '\tP2'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Sem/Hfam.*Abs\+Sg\+1SgPoss') | Inv(r'(TAR|NIQ|INNAQ|NNGIT|SSAQ)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst\+Sem/Hum).*\+Lok') | Inv(r'IP'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(aallartip|allap|ator|naammassi|paasi|sammisare).*TAQ\+SSAQ\+QAR\+Sem/have\+V\+Ind\+3Sg') | Inv(r'\+NNGIT'), '\t@PRED'),
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'(aappaagu|aasaru|aqagu|aqaguagu|ullumi)\+Adv'), '\t@CL-ADVL>'),
	['P3\tP3\t@SUBJ>'],
	['P4\tP4\t@ADVL>'],
	sfx(C() | Grep(r'^(aallartip|allap|ator|naammassi|paasi|sammisare).*GIARTUR\+SSA\+V\+Ind\+1Sg\+3'), '\tP5'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'(Fem|Mask).*Abs\+Sg') | Inv(r'(TAR|NIQ|INNAQ|NNGIT|SSAQ)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Sem/(Geo|inst\+Sem/Hum).*\+Lok') | Inv(r'IP'), '\t@ADVL>'),
	sfx(C() | Grep(r'^(aallartip|allap|ator|naammassi|paasi|sammisare).*TAQ\+SSAQ\+QAR\+Sem/have\+V\+Ind\+3Sg') | Inv(r'\+NNGIT'), '\t@PRED'),
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'(aappaagu|aasaru|aqagu|aqaguagu|ullumi)\+Adv'), '\t@CL-ADVL>'),
	['P3\tP3\t@SUBJ>'],
	['P4\tP4\t@ADVL>'],
	sfx(C() | Grep(r'^(aallartip|allap|ator|naammassi|paasi|sammisare).*GIARTUR\+SSA\+V\+Ind\+1Sg\+3'), '\tP5'),
	['.\t.\t@CLB'],
	])

cartesian()

Qs = []
def q(sentence):
	Q = []
	for w in sentence:
		w = w.split('\t')

		if w[0] == 'P1':
			w[0] = sentence[0].split('\t')[0].replace('+Lok', '+Trm')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[2] == 'P2':
			# Test if the root is the same
			if w[0].split('+')[0] != sentence[1].split('\t')[0].split('+')[0]:
				return
			w[2] = '@PRED'
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P3':
			w[0] = sentence[0].split('\t')[0].replace('+Abs+', '+Rel+')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P4':
			w[0] = sentence[1].split('\t')[0].replace('+Lok', '+Trm')
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[2] == 'P5':
			# Test if the root is the same
			if w[0].split('+')[0] != sentence[2].split('\t')[0].split('+')[0]:
				return
			w[2] = '@PRED'
			w[1] = S.corpus_kv[w[0]]

		Q.append(w)
	Qs.append([Q, trim_ucfirst(' '.join([w[1] for w in Q]))])

for sentence in S.sentences:
	q(sentence)

for q in Qs:
	print(f'{q[1]}')

write_qs(Qs, txt=True)
