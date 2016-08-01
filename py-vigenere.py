#!/usr/bin/env python

import os, sys

class bg:
    default = '\033[00m'
    red =  '\033[31m' + '\033[01m'
    green = '\033[32m' + '\033[01m'
    yellow = '\033[33m' + '\033[01m'
    blue =  '\033[34m' + '\033[01m'
    purple = '\033[35m' + '\033[01m'
    bluish = '\033[36m' + '\033[01m'
    white = '\033[37m' + '\033[01m'
    redb = '\033[41m'
    blueb = '\033[44m'
    greenb = '\033[42m'
    purpleb = '\033[45m'

alf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
try:
	metin = sys.argv[1]
	anahtar = sys.argv[2]	
	sifreSira = []
	sifrelenmis = ""

	if len(anahtar) < len(metin):
		for k in range(0, len(metin) - len(anahtar)):
			anahtar += anahtar[k]
			
	for sifreHarf in metin:
		sifreSira.append(alf.index(sifreHarf.upper()))

	def cAlf(x):
		newAlf = []
		indexAlf = range(alf.index(x), len(alf))
		indexAlf.extend(range(0, alf.index(x)))
		for index in indexAlf:
			newAlf.append(alf[index])
		return newAlf
			
	os.system('clear')
	print "\n     ",
	
	for i in alf:
		try:
			if metin.upper().index(i) != None:
				print bg.yellow + i + bg.default,
		except ValueError:
			print i,
		if i == alf[-1]:
			print "\n"
			
	for k, y in zip(anahtar, range(0, len(sifreSira))):
		print "  " +  k.upper() + "  ",
		for b in cAlf(k.upper()):
			if b == cAlf(k.upper())[sifreSira[y]]:
				print bg.default + bg.red + b + bg.default,
				sifrelenmis += b
			else:
				print b,
		print "" + bg.default

	print "\n"
	print bg.red + "         Metin: " + bg.default + bg.white + metin.upper() + bg.default
	print bg.green + "       Anahtar: " + bg.default + bg.white + anahtar.upper() + bg.default
	print bg.blue + "   Sifrelenmis: " + bg.default + bg.blueb + bg.white + sifrelenmis + bg.default + "\n"
	
except IndexError:
	print bg.red + "Eksik bilgi girdiniz." + bg.default
