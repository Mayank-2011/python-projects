print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

size_bill = 0
if size=="S":
    size_bill+=15
elif size=="M":
    size_bill+=20
elif size=="L":
    size_bill+=25
pepperoni_bill = 0
if add_pepperoni=="Y" and size=="S":
    pepperoni_bill += 2
elif add_pepperoni=="Y" and (size=="M" or size=="L"):
    pepperoni_bill += 3
extra_cheese_bill = 0
if extra_cheese=="Y":
    extra_cheese_bill+=1
total_bill = size_bill+extra_cheese_bill+pepperoni_bill
print(f"Your final bill is: ${total_bill}")
