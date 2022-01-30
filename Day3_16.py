airline = input("Enter the airline: ")
airline = airline.upper()
source = input("Enter the source: ")
source = source[:3]
destination = input("Enter the destination: ")
destination = destination[:3]
passenger_count = int(input("Enter the number of passengers: "))
start = 101
l = []

for i in range(passenger_count):
    s = airline + ":" + source + ":" + destination + ":" + str(start)
    l.append(s)
    start = start + 1

if(passenger_count<5):
    print(l)

else:
    print(l[-5:])