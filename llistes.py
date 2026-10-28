llista=[2,5,8]

print(llista[0])
print(llista[1])
print(llista[2])



for x in llista:
    print(x)

for x in range (len(llista)):
    print("Posició: ",x," Contigut: ",llista[x])

llista.append(10)
print(llista)
llista.insert(1,300)
print(llista)

del llista[2]
print(llista)

llista[1]=100