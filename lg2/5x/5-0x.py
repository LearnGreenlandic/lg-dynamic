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
	sfx(C() | Grep(r'Sem/((H\b|Hfam)*\+.*Abs\+Sg\+1SgPoss|Fem.*Abs\+Sg)') | Inv(r'(TAR|NIQ|INNAQ|NNGIT|SSAQ|ani|aqqalu|ui)'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Prop\+MIU.*be_copula\+V\+Ind\+3Sg'), '\t@PRED'), # No Sem/Geo at this time
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'Sem/(Hfam|build|Lh).*QAR\+Sem/have\+V\+Cont\+4Sg') | Inv(r'(INNAQ|mittarfik|PAK|SSAQ|NNGUAQ|pisi\+NIAR|nuliaq|naja|aleqa)'), '\t@ADVL>'),
	sfx(C() | Grep(r'suli\+Adv'), '\t@ADVL>'),
	['P1\tP1\t@ADVL>'],
	sfx(C() | Grep(r'najugaq\+QAR\+Sem/lodge\+V\+Ind\+3Sg'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'Prop\+MIU\+Sem/Hnat\+U\+Sem/be_copula\+NNGIT\+GALUAR\+V\+Ind\+1Sg'), '\t@PRED'), # No Sem/Geo at this time
	['.\t.\t@CLB'],
	['kisianni+Conj\tkisianni\t@CONJ'],
	['P2\tP2\t@i->N'],
	sfx(C() | Grep(r'Sem/Hfam.*QAR\+Sem/have\+V\+Cont\+1Sg') | Inv(r'(INNAQ|PAK|SSAQ|NNGUAQ)'), '\t@ADVL>'),
	['P3\tP3\t@i->N'],
	sfx(C() | Grep(r'(najugaq\+QAR\+Sem/lodge|nuna\+Sem/Lciv\+QAR\+Sem/have|suliffik\+Sem/Lh\+QAR\+Sem/have)\+V\+Ind\+1Sg'), '\t@PRED'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	sfx(C() | Grep(r'((nuliaq|ui)\+Sem/Hfam\+SSAQ|(nuliaq|ui)\+Sem/Hfam|nalu\+Sem/know\+NNGIT\+TAQ)\+N\+Abs\+Sg\+1SgPoss'), '\t@SUBJ>'),
	sfx(C() | Grep(r'Prop\+MIU.*be_copula\+V\+Ind\+3Sg'), '\t@PRED'), # No Sem/Geo at this time
	['.\t.\t@CLB'],
	sfx(C() | Grep(r'(pisi\+NIAR\+VIK|mittarfik)\+Sem/Lh\+N\+Lok\+Sg\s'), '\t@ADVL>'),
	sfx(C() | Grep(r'(suliffik\+Sem/Lh\+QAR\+Sem/have|suli\+Sem/work)(\+TAR)?\+V\+Cont\+4Sg'), '\t@ADVL>'),
	['P1\tP1\t@ADVL>'],
	sfx(C() | Grep(r'najugaq\+QAR\+Sem/lodge\+V\+Ind\+3Sg'), '\t@PRED'),
	['.\t.\t@CLB'],
	])

cartesian()

Qs = []
def q(sentence):
	Q = []
	for w in sentence:
		w = w.split('\t')

		if w[0] == 'P1':
			w[0] = re.sub(r'\+MIU.*$', r'', sentence[1].split('\t')[0].replace('+Prop', '+Sem/Geo+Prop')) + '+Lok+Sg'
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P2':
			w[0] = re.sub(r'\+MIU.*$', '+MIU+Sem/Hnat+N+Ins+Sg', sentence[0].split('\t')[0])
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]
		elif w[0] == 'P3':
			w[0] = re.sub(r'\+MIU.*$', r'', sentence[0].split('\t')[0].replace('+Prop', '+Sem/Geo+Prop')) + '+Lok+Sg'
			if w[0] not in S.corpus_kv:
				return
			w[1] = S.corpus_kv[w[0]]

		Q.append(w)
	Qs.append([Q, trim_ucfirst(' '.join([w[1] for w in Q]))])

for sentence in S.sentences:
	q(sentence)

for q in Qs:
	print(f'{q[1]}')

write_qs(Qs, txt=True)
