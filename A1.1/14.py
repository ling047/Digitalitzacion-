text = input("Introduce un texto: ")
text_invertit = ""


for i in range(len(text) - 1, -1, -1):
    text_invertit += text[i]

print(text_invertit)
