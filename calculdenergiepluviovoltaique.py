from math import pi

# Densité de l'eau (kg/m³)
densite_eau = 1000  

# Diamètres représentatifs des gouttes en mètres (petite, moyenne, grande)
diametres_gouttes = [0.001, 0.002, 0.004]  # Converti en mètres

# Vitesses terminales correspondantes en m/s
vitesses_terminales = [9, 12, 20]

# Calcul de la masse et de l'énergie cinétique pour chaque taille de goutte
masses = []
energies_cinetiques = []

for diametre, vitesse in zip(diametres_gouttes, vitesses_terminales):
    # Volume de la goutte (V = 4/3 * pi * r^3)
    volume = (4/3) * pi * (diametre / 2)**3
    # Masse (m = densité * volume)
    masse = densite_eau * volume
    # Énergie cinétique (E_k = 1/2 * m * v^2)
    e_k = 0.5 * masse * vitesse**2
    masses.append(masse)
    energies_cinetiques.append(e_k)

# Proportions estimées des tailles de gouttes dans les précipitations annuelles
proportions = [0.7, 0.2, 0.1]

# Quantité moyenne de précipitations annuelles en mètres cubes par mètre carré
quantite_precipitations_m3_par_m2 = 0.8

# Nombre total de gouttes par m² par an, calculé pour chaque taille
nombre_total_gouttes_par_taille = [(quantite_precipitations_m3_par_m2 / volume) for volume in [(4/3) * pi * (d / 2)**3 for d in diametres_gouttes]]

# Énergie totale générée par m² par an pour chaque taille de goutte, puis sommée
energie_totale_par_m2_par_an = sum([nombre * energie * proportion for nombre, energie, proportion in zip(nombre_total_gouttes_par_taille, energies_cinetiques, proportions)])

print(energie_totale_par_m2_par_an)

