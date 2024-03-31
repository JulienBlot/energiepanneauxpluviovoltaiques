# Superficie totale de la France en mètres carrés
superficie_france_m2 = 551695000000

# Énergie récupérable par mètre carré par an en Joules
energie_par_m2_par_an_joules = 50200

# Énergie totale récupérable sur toute la superficie en Joules
energie_totale_joules = superficie_france_m2 * energie_par_m2_par_an_joules

# Convertir l'énergie totale en Terajoules (TJ) pour une meilleure lisibilité
energie_totale_terajoules = energie_totale_joules / 1e12

energie_totale_terajoules

# Calculons l'énergie totale récupérable pour 1% de la superficie de la France
energie_totale_terajoules_1pc = energie_totale_terajoules * 0.01

print("Énergie totale récupérable pour 1% de la superficie de la France : {:.2f} TJ".format(energie_totale_terajoules_1pc))

# Conversion de Terajoules en kilowatt-heures (kWh)
energie_totale_kwh = 277 * 1e12 * (2.78e-7)

# Nombre de foyers moyens pouvant être alimentés (en prenant comme référence une consommation moyenne de 4700 kWh par foyer et par an en France)
nombre_foyers_alimentes = energie_totale_kwh / 4700

print("Énergie totale récupérable en kWh :", energie_totale_kwh)
print("Nombre de foyers moyens pouvant être alimentés :", int(nombre_foyers_alimentes))
