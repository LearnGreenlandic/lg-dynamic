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
	C() | Grep(r'^(isumaqar|eqqaama|nalu\+Sem/know\+NNGIT).*\+Int\+2Sg') | Inv(r'\+(LI|LU|2PlO|TAQ|GUSUP|TUQ)\b'),
	C() | Grep(r'^uanga.*Abs') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'(Sem/(Geo|inst|Lh).*\+Lok)|(Pron\+Lok\+(2Sg|2Pl))') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/(work|learn).*\+Par\+1Sg') | Inv(r'\+(LI|LU)\b'),
	])
S.patterns.append([
	C() | Grep(r'^(isumaqar|eqqaama|nalu\+Sem/know\+NNGIT).*\+Int\+2Sg') | Inv(r'\+(LI|LU|2PlO|TAQ|GUSUP|TUQ)\b'),
	C() | Grep(r'Sem/(Fem|Mask).*Abs') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'(Sem/(Geo|inst|Lh).*\+Lok)|(Pron\+Lok\+(2Sg|2Pl))') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/(work|learn).*\+Par\+3Sg') | Inv(r'\+(LI|LU)\b'),
	])
S.patterns.append([
	C() | Grep(r'^(isumaqar|eqqaama|nalu\+Sem/know\+NNGIT).*\+Int\+2Sg') | Inv(r'\+(LI|LU|2PlO|TAQ|GUSUP|TUQ)\b'),
	C() | Grep(r'^uanga.*Abs') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/Geo.*(Abl|Trm)') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/(reach|run).*\+Par\+1Sg') | Inv(r'\+(LI|LU)\b'),
	])

cartesian()

QAs = []
def qa(sentence):
	global QAs
	Q = []
	A = [['', 'Aap,']]
	for i,w in enumerate(sentence):
		w = w.split('\t')
		Q.append(w)
		w[0] = w[0].replace('+Int+2Sg', '+Ind+1Sg')
		w[0] = w[0].replace('+Par+1Sg', '+Par+2Sg')
		if w[0].startswith('uanga'):
			w = ['illit+Pron+Abs+2Sg', 'illit']
		if w[0] not in S.corpus_kv:
			return
		A.append([w[0], S.corpus_kv[w[0]]])

	QAs.append([Q, A])

for sentence in S.sentences:
	qa(sentence)

for qa in QAs:
	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([s[1] for s in qa[0]])) + '?'
	a = ucfirst(' '.join([s[1] for s in qa[1]])) + '.'
	print(f'{q} => {a}')

write_qas(QAs)
