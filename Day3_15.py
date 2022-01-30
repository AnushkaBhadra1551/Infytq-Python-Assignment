num1 = int(input("Enter the minimum number: "))
num2 = int(input("Enter the maximum number: "))
temp = -1

l = []   
for i in range(num1, num2+1):
    sum = 0
    for j in str(i):
        sum = sum + int(j)           
    if(sum%3==0 and len(str(i))==2 and i%5==0):
        l.append(i)

if(len(l)==0):
    print(temp) 
elif num1<num2:
    print(max(l)) 
else:
    print(temp)