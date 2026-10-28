# Conta quantes a hi ha a la cadena
textdna =  "atggatcattta"
contar=0
#print(textdna)
#print(textdna.count("a"))

for i in range(len(textdna)):
      if textdna[i] == "a":
          print("Trobada una 'a' a la posició", i)
          contar += 1
print("El número de a és:", contar)