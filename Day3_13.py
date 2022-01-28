a = int(input("Enter first side "))
b = int(input("Enter second side "))
c = int(input("Enter third side "))
if((a<=(b+c)) and (b<=(a+c)) and (c<=(a+b)) and ((a+b+c)<=180)):
    print("It is a triangle")
else:
    print("It is not a triangle")