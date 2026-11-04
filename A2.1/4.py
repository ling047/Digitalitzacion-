list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

max=None
min=None
for x in list_num:
    #print(x)
    if max==None or x>max:
        max=x
    if min==None or x<min:
        min=x
print("Max:", max, "Min:", min)