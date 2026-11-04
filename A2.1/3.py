list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
suma=None
for x in list_num:
    if suma==None:
        suma=x
    else:
        suma+=x
print("Suma de todos los elementos: ", suma)