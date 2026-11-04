list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
# Pregunta a l’usuari un número i comprova si està dins d’una llista.
usuari_num = int(input("Introdueix un número: "))
estat=False
for x in list_num:
    if usuari_num==x:
        estat=True
    if estat==False:
    
        print("El número", usuari_num, "no està dins de la llista.")
if estat==True:
    print("El número", usuari_num, "està dins de la llista.")