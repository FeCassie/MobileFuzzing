#!/bin/bash

# .m4a
echo -n "Ses uzantisini gir: "
read uzanti

echo -n "Ses boyutunu gir: "
read dosyaboyutu

echo -n "Kac dosya olusturulsun?: "
read dosyanum

# dosyaboyutu=208
 
offset=0

# fuzz değeri
fuzzval=255

i=1
while [ $i -lt $dosyanum ]
do
	cp ./Alarm.m4r ./$i$uzanti
	./fuzzer $dosyaboyutu $offset $fuzzval ./$i$uzanti

	let "offset += 1"
	let "i += 1"
done
