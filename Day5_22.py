def find_pairs_of_numbers(l,num):
    count = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]+l[j]==num):
                count = count + 1
    return(count)


l = []
n = int(input("Enter the range: "))
for i in range(n):
    numbers = int(input("Enter the numbers: ")) 
    l.append(numbers)
num = int(input("Enter the number to be added upto: "))
print(find_pairs_of_numbers(l,num)) 