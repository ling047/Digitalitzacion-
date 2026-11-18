list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]


# Inverteix l’ordre dels elements d’una llista sense usar reverse().
list_num2 = []

for x in range(len(list_num)-1, -1, -1):
    list_num2.append(list_num[x])

print(list_num2)

