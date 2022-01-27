year = int(input("Enter a year "))
year_list = []
count = 1

while count<=15:

    if ((year%4==0) and (year%100==0)):
        if(year%400==0):
            year_list.append(year)
            count = count + 1
    
    elif(year%4==0):
        
        year_list.append(year)
        count = count + 1
    year = year + 1

print(year_list)

