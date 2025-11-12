#!/usr/bin/env python3

'''
Aquest script permet veure si la part final de les imatges contenen bytes extres
10~15kb que només fan que pesi més. Tot i que la imatge tingui la mateixa resolució
aquests bytes extres fn que ocupi més sense millorar la imatge
'''

import os

def obtenir_fitxers_jpg(directori):
	fitxers = []
	for arrel, _, arxius in os.walk(directori):
		for arxiu in arxius:
			if arxiu.lower().endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')):
				fitxers.append(os.path.join(arrel, arxiu))
	return fitxers

def comparar_fitxers(fitxer1, fitxer2, percentatge=0.92):
	try:
		with open(fitxer1, 'rb') as f1, open(fitxer2, 'rb') as f2:
			dades1 = f1.read()
			dades2 = f2.read()

		mida_minima = min(len(dades1), len(dades2))
		mida_comparacio = int(mida_minima * percentatge)

		inicial1 = dades1[:mida_comparacio]
		inicial2 = dades2[:mida_comparacio]

		if inicial1 == inicial2:
			final1 = dades1[mida_comparacio:]
			final2 = dades2[mida_comparacio:]

			if final1 != final2:
				print(f"✅ Coincidència parcial: \n  - {fitxer1}\n  - {fitxer2}")
	except Exception as e:
		print(f"⚠️ Error comparant {fitxer1} i {fitxer2}: {e}")

# 🔍 Executa la comparació en totes les imatges del directori
directori_base = '.'  # Canviar-ho per qualsevol ruta
fitxers = obtenir_fitxers_jpg(directori_base)

print(f"🔎 S'han trobat {len(fitxers)} imatges JPG. Iniciant comparacions...")

for i in range(len(fitxers)):
	for j in range(i + 1, len(fitxers)):
		comparar_fitxers(fitxers[i], fitxers[j], percentatge=0.94)
