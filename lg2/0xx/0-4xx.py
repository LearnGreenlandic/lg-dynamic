#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S

# load_corpus('0xx-corpus.txt')

S.patterns.append([
	['-\tDanmarkimi nunaqarpunga.'],
	['⇒'],
	['-\tNalunngilat Danmarkimi nunaqartunga.'],
	])
S.patterns.append([
	['-\tHvidovremi ilinniartitsisuuvunga.'],
	['⇒'],
	['-\tNalunngilat Hvidovremi ilinniartitsisuusunga.'],
	])
S.patterns.append([
	['-\tUkioq ataaseq kalaallisut ilinniarpunga.'],
	['⇒'],
	['-\tNalunngilat ukioq ataaseq kalaallisut ilinniartunga.'],
	])
S.patterns.append([
	['-\tKalaallisut oqalulaartarpunga.'],
	['⇒'],
	['-\tNalunngilat kalaallisut oqalulaartartunga.'],
	])
S.patterns.append([
	['-\tAasaq manna Kalaallit Nunaannut aallassaanga.'],
	['⇒'],
	['-\tNalunngilat aasaq manna Kalaallit Nunaannut aallassasunga.'],
	])
S.patterns.append([
	['-\tNuliaqarpunga.'],
	['⇒'],
	['-\tNalunngilat nuliaqartunga.'],
	])
S.patterns.append([
	['-\tTaanna Elsemik ateqarpoq.'],
	['⇒'],
	['-\tNalunngilat taanna Elsemik ateqartoq.'],
	])
S.patterns.append([
	['-\tElse peqqissaasuuvoq.'],
	['⇒'],
	['-\tNalunngilat Else peqqissaasuusoq.'],
	])
S.patterns.append([
	['-\tNapparsimmavimmi sulisarpoq.'],
	['⇒'],
	['-\tNalunngilat napparsimmavimmi sulisartoq.'],
	])
S.patterns.append([
	['-\tMarlunnik meeraqarpugut.'],
	['⇒'],
	['-\tNalunngilat marlunnik meeraqartugut.'],
	])
S.patterns.append([
	['-\tPanipput Lenemik ateqarpoq, ernerpullu Ebbemik ateqarpoq.'],
	['⇒'],
	['-\tNalunngilat panipput Lenemik ateqartoq, ernerpullu Ebbemik ateqartoq.'],
	])
S.patterns.append([
	['-\tLene qulinik ukioqarpoq.'],
	['⇒'],
	['-\tNalunngilat Lene qulinik ukioqartoq.'],
	])
S.patterns.append([
	['-\tEbbe aqqanilinnik ukioqarpoq.'],
	['⇒'],
	['-\tNalunngilat Ebbe aqqanilinnik ukioqartoq.'],
	])
S.patterns.append([
	['-\tLene Ebbelu atuartuupput.'],
	['⇒'],
	['-\tNalunngilat Lene Ebbelu atuartuusut.'],
	])
S.patterns.append([
	['-\tHvidovremi najugaqarpugut.'],
	['⇒'],
	['-\tNalunngilat Hvidovremi najugaqartugut.'],
	])
S.patterns.append([
	['-\tLene Ebbelu Hvidovremi atuartarput.'],
	['⇒'],
	['-\tNalunngilat Lene Ebbelu Hvidovremi atuartartut.'],
	])

cartesian()

QAs = []
def qa(sentence):
	global QAs
	Q = []
	A = []
	in_a = False
	for w in sentence:
		if w == '⇒':
			in_a = True
			continue

		w = w.split('\t')

		if not in_a:
			Q.append(w)
		else:
			A.append(w)

	QAs.append([Q, A, trim_ucfirst(' '.join([w[1] for w in Q])), trim_ucfirst(' '.join([w[1] for w in A]))])

for sentence in S.sentences:
	qa(sentence)

for qa in QAs:
	print(f'{qa[2]} ⇒ {qa[3]}')

write_qas(QAs, txt=True)
