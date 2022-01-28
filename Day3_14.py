heads = int(input("Enter the number of heads "))
legs = int(input("Enter the number of legs "))

if((legs//heads==4) and (legs%heads==0)):
    print("Number of chicken ",0)
    int("Number of rabbits ",heads)
elif((legs//heads==2) and (legs%heads==0)):
    print("Number of chicken ",heads)
    print("Number of rabbits ",0)
else:
    rem = legs%heads
    q = legs//heads
    if(q==2):
        print("Number of chicken ",rem)
        print("Number of rabbits ",heads-rem)
    elif(q==4):
        print("Number of chicken ",heads-rem)
        print("Number of rabbits ",rem)
    else:
        print("No solution")
