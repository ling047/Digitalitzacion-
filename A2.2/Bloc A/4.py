capital_pais = {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma"}
pais = input("Introdueix un país: ")


# a) amb if pais in capital_pais
if pais in capital_pais.keys():
    print(f"La capital de {pais} és {capital_pais[pais]}.")
else:
    print("No tinc aquest país.")

# b) amb get() i un valor per defecte
capital = capital_pais.get(pais, "No tinc aquest país")
if capital != "No tinc aquest país":
    print(f"La capital de {pais} és {capital}.")
else:
    print(capital)