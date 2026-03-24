# TODO 8.exception for milk in espresso
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

machine_working = True
quarters = 0
dimes = 0
nickles = 0
pennies = 0
money_amount = 0

# TODO: 1.Print the resource of all machine resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
def process_coins(quarters, dimes, nickles, pennies):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters, dimes, nickles, pennies



#def check_resources(water, coffee, milk):


# TODO: 2.Turn off The Machine by entering "off" prompt
while machine_working:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_working = False
# TODO: 3.Print report when user enters "report"
    if user_choice == "report":
        report()
        continue
# TODO: 4.Resources suffiecent?
    elif user_choice == "espresso":
        if MENU["espresso"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            print("Sucfiecent resources")
            
    elif user_choice == "latte":
        if MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
            print("Sucfiecent resources")
    elif user_choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"] and MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]:
            print("Sucfiecent resources")
# TODO: 5.Process coins.
    print("Please insert coins ")
    money_amount = 0
    quarters, dimes, nickles, pennies = process_coins(quarters, dimes, nickles, pennies)
    money_amount = money_amount + quarters * 25
    print(money_amount)
    money_amount = money_amount + dimes * 10
    print(money_amount)
    money_amount = money_amount + nickles * 5
    print(money_amount)
    money_amount = money_amount + pennies
    print(money_amount)
    money_amount = money_amount / 100
    print(money_amount)

# TODO: 6.Check if transaction is successful?
    if money_amount >= MENU[user_choice]["cost"]:
        money_amount = money_amount - MENU[user_choice]["cost"]
        print("made")
        print(money_amount)
# TODO: 7.Make coffee.
    resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
    print(f"Your {user_choice} is ready")
