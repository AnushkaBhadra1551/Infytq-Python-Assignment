num = []
prod = 1
for i in range(3):
    num.append(int(input("Enter the numbers ")))
if 7 in num:
    id = num.index(7)
    temp = num[id+1:]
    if (len(temp)==0):
        prod = -1
    else:
        for j in temp:
            prod = prod*j
else:
    for k in num:
        prod = prod*k
print(prod)