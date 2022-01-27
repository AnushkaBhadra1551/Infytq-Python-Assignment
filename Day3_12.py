shop_count = int(input("Enter the number of gems variety present in the market : "))
gems_list = []
price_list = []

for i in range(shop_count):   

    gems = input("Enter the gems available in the market ")
    gems_list.append(gems)
    price = int(input("Enter the price "))
    price_list.append(price)

user_count = int(input("Enter the number of gems variety required by the user "))
reqd_gems = []
reqd_quantity = []
total_price = 0
temp = -1

if(user_count>0):

    for j in range(user_count):

        user_gems = input("Enter the gems required by the user ")
        reqd_gems.append(user_gems)
        user_count = int(input("Enter the number of gems required by the user "))
        reqd_quantity.append(user_count)   

    
        for x in range(shop_count):
            if(reqd_gems[j] in gems_list[x]):
                quantity = reqd_quantity[j]
                price = price_list[x]
                total_price = total_price + (quantity*price)
                if(total_price>30000):
                    discount = (5/100)*total_price
                    final_amount = total_price - discount
                    print("Amount to be paid with discount ",final_amount)
                else:
                    print("Amount to be paid ",total_price)
            break
            
        else:
            print(temp)
                
            
else:
    print("Nothing to pay :) ")