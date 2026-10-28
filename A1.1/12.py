# Compara els caràcters d’una cadena amb una altra 
text =  "Hello World"
text2 = "Hola mon!!!"  
contar = 0
for c in range(len(text)):
    if text[c] == text2[c]:
        print("Els caràcters són iguals: ", text[c])
        contar += 1
    
print(text," / ",text2)
print("El caracter que se coincide és :", contar)        
