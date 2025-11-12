#!/usr/bin/env python3

'''
script que permet cercar imatges que tinguin semblances visuals
d_aproximadament un 94%
'''

from PIL import Image
import imagehash
import os

# Llindar de similitud (94%)
threshold = 0.94

# Carregar totes les imatges JPG del directori actual
images = [f for f in os.listdir('.') if f.lower().endswith('.jpg')]

print(f"🔍 Comparant {len(images)} imatges amb llindar de {threshold * 100}%...")

for i in range(len(images)):
	for j in range(i + 1, len(images)):
		try:
			img1 = Image.open(images[i])
			img2 = Image.open(images[j])

			hash1 = imagehash.dhash(img1)
			hash2 = imagehash.dhash(img2)

			max_bits = len(hash1.hash.flatten())
			diff = hash1 - hash2
			similarity = 1 - (diff / max_bits)

			if similarity >= threshold:
				print(f"✅ {images[i]} i {images[j]} tenen una similitud de {round(similarity * 100, 2)}%")
		except Exception as e:
			print(f"⚠️ Error comparant {images[i]} i {images[j]}: {e}")
