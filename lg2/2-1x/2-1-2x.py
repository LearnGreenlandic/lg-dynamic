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
	['ippassaq+Adv\tippassaq'],
	C() | Grep(r'Sem/(Geo|inst)\+.*Lok') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/(Fem|Mask)\+.*Abs') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'\+Int\+2Sg\+3SgO\t') | Grep(r'\+Sem/(socialize|teach|encounter|see)\+') | Inv(r'\+(SSA|LI|LU)\b'),
	])
S.patterns.append([
	['aqaguagu+Adv\taqaguagu'],
	C() | Grep(r'Sem/(Geo|inst)\+.*Lok') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'Sem/(Fem|Mask)\+.*Abs') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'\+SSA\b.*\+Int\+2Sg\+3SgO\t') | Grep(r'\+Sem/(socialize|teach|encounter|see)\+') | Inv(r'\+(LI|LU)\b'),
	])

cartesian()

QAs = []
def qa(sentence):
	global QAs
	Q = []
	A = [['', 'Aap,']]
	for w in sentence:
		w = w.split('\t')
		Q.append(w)
		w[0] = w[0].replace('+Int+2Sg', '+Ind+1Sg')
		if w[0] not in S.corpus_kv and '+Adv' not in w[0]:
			return
		A.append([w[0], S.corpus_kv[w[0]]])

	QAs.append([Q, A])

for sentence in S.sentences:
	qa(sentence)

QA_good = []
for qa in QAs:
	if re.match(r'ippassaq|aqagu|aqaguagu', qa[0][0][1]) and '+TAR+' in qa[0][-1][0]:
		#print('DISCARDED ' + str(qa))
		continue
	QA_good.append(qa)

	# Human-readable debug print of generated sentences
	q = ucfirst(' '.join([s[1] for s in qa[0]])) + '?'
	a = ucfirst(' '.join([s[1] for s in qa[1]])) + '.'
	print(f'{q} => {a}')

write_qas(QA_good)
