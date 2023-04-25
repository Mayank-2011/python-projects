print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill? $"))
total_people = int(input("How many pople to split the bill? "))
tip_percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
pay_per_person =(bill_amount*(1+(tip_percentage/100)))/total_people
pay_per_person = "{:.2f}".format(pay_per_person)
print("Each person should pay", pay_per_person)
