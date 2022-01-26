one = int(input("Enter the number of 1 Rs coin available "))
five = int(input("Enter the number of 5 Rs coin available "))
amount = int(input("Enter the amount to be paid "))
final_one = one * 1
final_five = five * 5
final = final_one + final_five
if (final>amount):  
    q = amount//5
    r = amount % 5
    print("Number of Rs 5 coins is ",q)
    print("Number of Rs 1 coins is ",r)
elif(final==amount):
    print("Number of Rs 5 coins is ",final_five)
    print("Number of Rs 1 coins is ",final_one)
else:
    temp = -1
    print(temp)

