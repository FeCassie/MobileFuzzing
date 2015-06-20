#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os

def SignalSEC():
	print "\n"
	print "SignalSEC MobileBrowser Audio Fuzzer"
	print "      Fatih Erdoğan @ FeCassie      " 
	print "      http://www.signalsec.com      "
	print "\n"

def sesList():
	d = os.getcwd()
	print "[*] Bulunduğunuz dizin: %s" % (d)
	global ses
	ses = raw_input("[*] Fuzz edilecek ses türünü gir: ")
	dizin = os.listdir(d)
	print "[*] %s uzantili dosyalar: " % (ses)
	for i in dizin:
		if i.endswith(ses):
			print i 

doctype = '<!DOCTYPE html>\n'
refresh = '<html><head><meta http-equiv="refresh" content="1; url='
refresh2 = '">\n</head>'
banner = '<body><h1><a href="http://www.signalsec.com">SignalSEC</a> MobileSafari Audio Fuzzer</h1>'
banner += '<b><p>Fatih ERDOGAN</p></b>'
banner += '<img src="http://www.signalsec.com/images/logo.png" alt="signalsec.com" width="240" height="62"></body>'
header = '<audio controls>'
aud = '<source src="'
aud2 = '" type="audio/mpeg">'
aud2 += '</audio>\n</html>'

SignalSEC()
sesList()
dosyasayi = int(raw_input("[*] oluşturulacak dosya sayısını gir: "))

mesaj = "\n[+] signalsec rocks!\n"
print mesaj
print "-" * len(mesaj)
i = 0
while i < dosyasayi:
	try:
		i += 1
		fuzz = doctype + refresh + "%d" % (i+1) + ".html"
		fuzz += refresh2 + banner + header + "\n" + aud + "%d" % (i) + ses + aud2
		dosya = open("%d" % (i) + ".html", "w")
		dosya.write(fuzz)

		print "[+] %s.html olusturuldu." % (i)
	except:
		print "[-] .html dosyaları oluşturulamadı!"
		sys.exit()


