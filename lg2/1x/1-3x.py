#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('1x-corpus.txt')

S.patterns.append([
	['ippassaq+Adv\tippassaq'],
	C() | Grep(r'Sem/(Geo|inst)\+.*Lok') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'\+Int\+2Sg\t') | Grep(r'\+Sem/(be_attribute|learn|lodge|refuse|work|speak_emot)\+') | Grep(r'\+NNGIT') | Inv(r'\+(GALUAR|SSA|LI|LU)\b'),
	])
S.patterns.append([
	['aqaguagu+Adv\taqaguagu'],
	C() | Grep(r'Sem/(Geo|inst)\+.*Lok') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'\+SSA\b.*\+Ind\+1Sg\t') | Grep(r'\+Sem/(be_attribute|learn|lodge|refuse|work|speak_emot)\+') | Grep(r'\+NNGIT') | Inv(r'\+(GALUAR|LI|LU)\b'),
	])
S.patterns.append([
	['ippassaq+Adv\tippassaq'],
	C() | Grep(r'Sem/(Geo|inst)\+.*(Abl|Trm)') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'\+Int\+2Sg\t') | Grep(r'\+Sem/(run|reach)\+') | Grep(r'\+NNGIT') | Inv(r'\+(GALUAR|SSA|LI|LU)\b'),
	])
S.patterns.append([
	['aqaguagu+Adv\taqaguagu'],
	C() | Grep(r'Sem/(Geo|inst)\+.*(Abl|Trm)') | Inv(r'\+(LI|LU)\b'),
	C() | Grep(r'\+SSA\b.*\+Ind\+1Sg\t') | Grep(r'\+Sem/(run|reach)\+') | Grep(r'\+NNGIT') | Inv(r'\+(GALUAR|LI|LU)\b'),
	])

cartesian()

QAs = []
def qa(sentence):
	global QAs
	Q = []
	A = [['', 'Naamik,']]
	inv = False
	for w in sentence:
		w = w.split('\t')
		# If the question starts with "aqaguagu", it's actually the answer, since it's otherwise impossible to know where +NNGIT goes. So invert question and answer logic.
		if w[1] == 'aqaguagu':
			inv = True
		if '+NNGIT+' in w[0] and inv:
			q0 = w[0].replace('+NNGIT+', '+').replace('+Ind+1Sg', '+Int+2Sg')
			if q0 not in S.corpus_kv:
				return
			Q.append([q0, S.corpus_kv[q0]])
		else:
			Q.append(w)
			w[0] = w[0].replace('+Int+2Sg', '+Ind+1Sg').replace('+NNGIT+', '+')

		if w[0] not in S.corpus_kv:
			if '+Adv' not in w[0]:
				return
			A.append(w)
		else:
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
