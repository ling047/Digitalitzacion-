list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
list_num2 = []
 # Donada una llista amb elements repetits, crea una nova llista sense duplicats.  Crear una llista Nova
for x in list_num:
    estat=False
    for y in list_num2:
        if x==y:
            estat=True
    if estat==False:
        
        list_num2.append(x)
print("Llista sense duplicats:", list_num2)