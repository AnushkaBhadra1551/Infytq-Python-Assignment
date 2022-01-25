percentage_score = int(input("Enter the score "))
if(percentage_score>=80 and percentage_score<=100):
    print("A")
elif(percentage_score>=73 and percentage_score<=79):
    print("B")
elif(percentage_score>=65 and percentage_score<=72):
    print("C")
elif(percentage_score>=0 and percentage_score<=64):
    print("D")
else:
    print("Z")