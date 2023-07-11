MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

coffee_machine_off = False

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def money():
     print("Please insert coins.\n")
     quarters = int(input("how many quarters?: "))
     dimes = int(input("how many dimes?: "))
     nickels = int(input("how many nickels?: "))
     pennies = int(input("how many pennies?: "))
     return round(((quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)),2)

def make_coffee(drink_name, order_ingredients):
    global profit
    if total_money_in < required_money:
        print("Sorry that's not enough money. Money refunded.")
    elif total_money_in >= required_money:
        change = round((total_money_in - required_money),2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice}. Enjoy!")
        for item in drink["ingredients"]:
            resources[item] = resources[item] - drink["ingredients"][item]
        profit += drink['cost']

while not coffee_machine_off:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    
    if choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")

    elif choice == 'off':
        coffee_machine_off = True
    
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            required_money = MENU[choice]['cost']
            total_money_in = money()
            make_coffee(choice, drink['ingredients'])