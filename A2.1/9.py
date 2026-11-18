list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

list_ordenada = []
#1.Intenta fer el teu algoritme cercant els mínims de la llista

list_num1 = list_num.copy()

while len(list_num1) > 0:
    minimo = list_num1[0]

    for x in list_num1:
        if x < minimo:
            minimo = x

    list_ordenada.append(minimo)
    list_num1.remove(minimo)

print(list_ordenada)

#2.Cerca diferents algoritmes d’ordenació

#    • Bubble Sort (Ordenació de bombolla): Compara elements adjacents i els intercanvia si estan desordenats, fent que els números més grans "pugin" al final com bombolles.
#    • Selection Sort (Ordenació per selecció): Busca l'element més petit de la part desordenada i l'intercanvia amb el primer element desordenat.
#    • Insertion Sort (Ordenació per inserció): Agafa cada element i l'insereix a la posició correcta dins de la part que ja està ordenada (com quan ordenes cartes a la mà).
#    • Merge Sort (Ordenació per mescla): Divideix la llista per la meitat recursivament fins a tenir elements sols i després els va ajuntant de manera ordenada.
#    • Quick Sort (Ordenació ràpida): Tria un element com a "pivot" i posa els més petits a l'esquerra i els més grans a la dreta.


#3.Implementa amb l’algoritme d’ordenació “Selection Sort”
list_num3=list_num.copy()

for i in range(len(list_num3)):
    minim = i

    for j in range(i + 1, len(list_num3)):
        if list_num3[j] < list_num3[minim]:
            minim = j

    aux = list_num3[i]
    list_num3[i] = list_num3[minim]
    list_num3[minim] = aux

print(list_num3)

#4.Implementa amb l’algoritme d’ordenació “Insertion Sort”

list_num4=list_num.copy()

for i in range(1, len(list_num4)):
    num = list_num4[i]
    j = i - 1

    while j >= 0 and list_num4[j] > num:
        list_num4[j + 1] = list_num4[j]
        j = j - 1

    list_num4[j + 1] = num

print(list_num4)