#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

load_corpus('0xx-corpus.txt')

S.patterns.append([
	C() | Grep(r'\silinniartitsisoq$'),
	['-\tHans Jensen'],
	C() | Grep(r'\sDanmarkimi$'),
	C() | Grep(r'\snunaqarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tHvidovremi'],
	C() | Grep(r'\silinniartitsisuuvoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	C() | Grep(r'\sukioq$'),
	C() | Grep(r'\sataaseq$'),
	C() | Grep(r'\skalaallisut$'),
	C() | Grep(r'\silinniarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	C() | Grep(r'\skalaallisut$'),
	C() | Grep(r'\soqalulaartarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tJensen'],
	C() | Grep(r'\saasaq$'),
	['-\tmanna'],
	C() | Grep(r'\sKalaallit Nunaannut$'),
	C() | Grep(r'\saallassaaq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tHans Jensen'],
	C() | Grep(r'\snuliaqarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	C() | Grep(r'\staanna$'),
	['-\tElsemik'],
	C() | Grep(r'\sateqarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tElse'],
	C() | Grep(r'\speqqissaasuuvoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	C() | Grep(r'\snapparsimmavimmi$'),
	C() | Grep(r'\ssulisarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tHans Jensenikkut'],
	C() | Grep(r'\smarlunnik$'),
	['-\tmeeraqarput'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tpaniat'],
	['-\tLenemik'],
	C() | Grep(r'\sateqarpoq$'),
	[',\t,\t@CLB'],
	['-\ternerallu'],
	['-\tEbbemik'],
	C() | Grep(r'\sateqarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tLene'],
	['-\tqulinik'],
	C() | Grep(r'\sukioqarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tEbbe'],
	C() | Grep(r'\saqqanilinnik$'),
	C() | Grep(r'\sukioqarpoq$'),
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tLene'],
	['-\tEbbelu'],
	['-\tatuartuupput'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tJensenikkut'],
	['-\tHvidovremi'],
	['-\tnajugaqarput'],
	['.\t.\t@CLB'],
	])
S.patterns.append([
	['-\tLene'],
	['-\tEbbelu'],
	['-\tHvidovremi'],
	['-\tatuartarput'],
	['.\t.\t@CLB'],
	])

cartesian()

QAs = []
def qa(sentence):
	global QAs
	Q = []
	A = [['', 'Nalunngilat']]
	for i,w in enumerate(sentence):
		w = w.split('\t')
		Q.append(w.copy())
		nw = w[0]
		if w[0] in S.corpus_kv and (nw := 'x') and (nw := w[0].replace('+Ind+3Sg', '+Par+3Sg')) and nw not in S.corpus_kv:
			return
		w[0] = nw

		if w[1] == 'meeraqarput':
			w[1] = 'meeraqartut'
		if w[1] == 'atuartuupput':
			w[1] = 'atuartuusut'
		if w[1] == 'najugaqarput':
			w[1] = 'najugaqartut'
		if w[1] == 'atuartarput':
			w[1] = 'atuartartut'

		if w[0] in S.corpus_kv:
			A.append([w[0], S.corpus_kv[w[0]]])
		else:
			A.append(w)

	QAs.append([Q, A, trim_ucfirst(' '.join([w[1] for w in Q])), trim_ucfirst(' '.join([w[1] for w in A]))])

for sentence in S.sentences:
	qa(sentence)

for qa in QAs:
	print(f'{qa[2]} ⇒ {qa[3]}')

write_qas(QAs, txt=True)
