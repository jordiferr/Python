#!/usr/bin/python3

def find_index(vect, value):
	index_min = 0
	index_max = n_max + 1
	index = (index_min + index_max) // 2
	i = 0

	while (index_max - index_min) > 1 and i < 500:
		if vect[index] == value:
			break
		elif vect[index] > value:
			index_max = index
		else:
			index_min = index

		index = (index_min + index_max) // 2
		i += 1

	if index < n_max:
		tol1 = abs(vect[index] / value - 1.0)
		tol2 = abs(vect[index + 1] / value - 1.0)
		if tol1 < tol2:
			return index
		else:
			return index + 1
	else:
		return index

rd = float(input("\nIntrodueix el valor de resistència desitjat: "))
series = input("\nIntrodueix la sèrie de resistències (E12, E24, E48, E96): ")
print("\n")

if series == "E12":
	Rbase = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
elif series == "E24":
	Rbase = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]
elif series == "E48":
	Rbase = [1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.90, 6.19, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53]
elif series == "E96":
	Rbase = [1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00, 2.05, 2.10, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.50, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76]
else:
	Rbase = []

R = []
for mult in range(7):
	for idx in range(len(Rbase)):
		# Arrodoniment per compensar els errors pow(); permet un màxim de dos decimals, necessaris per a E48 i E96
		R.append(round(Rbase[idx] * 10 ** mult, 2))

n_max = len(R) - 1  # maxim index valid

G = []
# Calculem la matriu de conductàncies, primer la conductància més baixa per tenir una matriu ordenada en ordre ascendent
G = [1.0 / R[n_max - idx] for idx in range(len(R))]

r1 = r2 = r1_idx = rres = rres_tol = best_tol = out_idx = op = 0
out_prres = out_vrres = 0
iter = 0  # Nombre d'iterations
out_r1 = []
out_r2 = []
out_op = []
out_rres = []
out_tol = []

# Calculem assumint resistències en series
r1_idx = find_index(R, rd)

r1 = R[r1_idx]
r2 = 0  # Inicialitzem les altres resistències a 0
rres = r1
rres_tol = (rres - rd) / rd  # Tolerancia relativa
best_tol = rres_tol

out_r1.append(r1)
out_r2.append(r2)
out_op.append("+")
out_rres.append(rres)
out_tol.append(rres_tol)

for r1_idx in range(r1_idx, -1, -1):
	if R[r1_idx] < rd / 2.0:
		break
	iter += 1
	r1 = R[r1_idx]

	r2d = rd - r1  # Aquest és el valor que necessitem
	if r2d < 0:
		continue

	r2_idx = find_index(R, r2d)
	r2 = R[r2_idx]  # Aconseguim el valor estàndard més pròxim
	rres = r1 + r2  # Calcula el resultat a mostrar
	rres_tol = rres / rd - 1.0  # I les toleràncies respectives

	if abs(rres_tol) < abs(best_tol):
		out_r1.append(r1)
		out_r2.append(r2)
		out_op.append("+")
		out_rres.append(rres)
		out_tol.append(rres_tol)

rd = 1.0 / rd
# Calcula assumint que les resistències estàn en paral·lel
r1_idx = find_index(G, rd)
for r1_idx in range(r1_idx, -1, -1):
	if G[r1_idx] < rd / 2.1:
		break
	iter += 1
	r1 = G[r1_idx]

	r2d = rd - r1  # Aquest és el valor que necessitem
	if r2d < 0:
		continue

	r2_idx = find_index(G, r2d)
	r2 = G[r2_idx]  # Aconseguim el valor estàndard més pròxim
	rres = r1 + r2  # Calcula el resultat a mostrar
	rres_tol = rd / rres - 1.0  # I les toleràncies respectives

	if abs(rres_tol) < abs(best_tol):
		out_r1.append(R[n_max - r1_idx])  # Utilitzar els valors del vector de resistencies per evitar errors d'arrodoniment
		out_r2.append(R[n_max - r2_idx])
		out_op.append("||")
		out_rres.append(1.0 / rres)
		out_tol.append(rres_tol)

# Ordenar els resultats
resultats_ordenats = sorted(zip(out_r1, out_r2, out_op, out_rres, out_tol), key=lambda x: abs(x[4]))
out_r1, out_r2, out_op, out_rres, out_tol = zip(*resultats_ordenats)

print("\nR1 (Ω)\tconf\tR2 (Ω)\t\tRt (Ω)\t\tError (%)\n----------------------------------------------------------")
for r1_idx in range(len(out_r1)):
	out_prres = round(out_rres[r1_idx] * 1000) / 1000
	out_vrres = f"{out_prres:.3f}"

	if len(out_vrres) < 8:
		out_vrres += "\t"
	print(f"{out_r1[r1_idx]}\t{out_op[r1_idx]}\t{out_r2[r1_idx]}\t=\t{out_vrres}\t({round(out_tol[r1_idx] * 100000) / 1000} %)")
print("\n")
