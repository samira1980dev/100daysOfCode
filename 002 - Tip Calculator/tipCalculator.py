print("Welcome to tip calculator!")
total = float(input("What was the total bill? R$ "))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
tip = tip / 100
people = int(input("How many people to split the bill? "))
final = "{:.2f}".format(((total + (total * tip)) / people), 2)
print(f"Each person should pay: R$ {final}")

