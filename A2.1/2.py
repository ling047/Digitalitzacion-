list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
 # Compta quantes vegades apareix un determinat valor dins d’una llista.
valor=3
contador=0
for x in list_num:
    if x==valor:
        contador+=1
print("El valor", valor, "apareix", contador, "vegades en la llista.")