 # Crea una llista amb 5 números enters i mostra-la per pantalla
llista=[91,78,27,12,15]

print("Llista de números:", llista)
for x in llista:
    print(x)
# Crea una llista de noms, mostra el primer i l’últim element.
# Utilitzar len(llista) per mostrar lúltim element 
# No utilitzar llista[-1]
llista_nom=["haha","jaja","fun"]
print("Primer element:", llista_nom[0])
print("Últim element:",llista_nom[len(llista_nom)-1])

 # Afegeix un element nou al final d’una llista i elimina el primer.
llista.append(10)
llista_nom.append("happy")
del llista[0]
del llista_nom[0]
print(llista)
print(llista_nom)
# Mostra quants elements tenen les llistes que has creat
print("Quants elements tenen: ",len(llista))
print("Quants elements tenen: ",len(llista_nom))