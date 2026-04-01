#Topic: Flight Calculation Algorithm
#Formula: Initial + Landing - Takeoffs

initial_no_of_flights= 10

#We use int() to convert text input into a whole number
Landings= int(input("Enter number of Landings:"))
Takeoffs= int(input("Enter number of Takeoffs:"))

current_total= initial_no_of_flights+Landings-Takeoffs

print("Result")
print("Current number of flights at the airport:", current_total)
