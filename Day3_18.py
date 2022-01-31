def profit_or_loss(distance, passenger_count):
    price_per_litre = 70
    price_per_ticket = 80
    mileage = 10
    ticket_price = passenger_count * price_per_ticket
    litre = distance / mileage
    litre_price = litre * price_per_litre
    profit = ticket_price-litre_price
    if(ticket_price>litre_price):
        return profit
    else:
        return -1

distance = float(input("Enter the distance in kms : "))
passenger_count = int(input("Enter the number of passengers: "))
print(profit_or_loss(distance, passenger_count))