#!/usr/bin/env python3

'''
script que permet cercar imatges que tinguin semblances visuals
d_aproximadament un 94%
'''

from PIL import Image
import imagehash
import os

def obtenir_fitxers_imatge(directori):
	fitxers = []
	for arrel, _, arxius in os.walk(directori):
		for arxiu in arxius:
			if arxiu.lower().endswith(('.jpg', '.jpeg', '.png')):
				fitxers.append(os.path.join(arrel, arxiu))
	return fitxers

def comparar_fitxers(fitxer1, fitxer2, percentatge=0.94):
	try:
		img1 = Image.open(fitxer1)
		img2 = Image.open(fitxer2)

		hash1 = imagehash.dhash(img1)
		hash2 = imagehash.dhash(img2)

		max_bits = len(hash1.hash.flatten())
		diff = hash1 - hash2
		similitud = 1 - (diff / max_bits)

		if similitud >= percentatge:
			print(f"✅ {fitxer1} i {fitxer2} tenen una similitud de {round(similitud * 100, 2)}%")
	except Exception as e:
		print(f"⚠ Error comparant {fitxer1} i {fitxer2}: {e}")

# 🔍 Executa la comparació en totes les imatges del directori
directori_base = '.'  # Canviar-ho per qualsevol ruta
fitxers = obtenir_fitxers_imatge(directori_base)

print(f"🔎 S'han trobat {len(fitxers)} imatges. Iniciant comparacions amb llindar de 94%...")

for i in range(len(fitxers)):
	for j in range(i + 1, len(fitxers)):
		comparar_fitxers(fitxers[i], fitxers[j], percentatge=0.94)
