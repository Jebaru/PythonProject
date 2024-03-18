# Day 15 Project👌
# Feature 1: Make 3 coffee
# 1. Espresso - 50ml Water, 18g Coffee - $1.50
# 2. Latte - 200ml Water, 24g Coffee, 150ml Milk - $2.50
# 3. Cappuccino - 250ml Water, 24g Coffee, 100ml Milk - $3.00
# Feature 2: Coin Operated
# 4 types of coin
# 1. Penny - 1 cent - $0.01
# 2. Nickel - 5 cents - $0.05
# 3. Dime - 10 cents - $0.10
# 4. Quarter - 25 cents - $0.25
# Program Requirements:
# 1. Print Report
# 2. Check resources are sufficient?
# 3. Process Coin
# 4. Check Transaction Successful?
# 5. Make Coffee
from art import coffee_cup

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def report_make():
    """This function generates a report on the amount of ingredients in the coffee machine"""
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")


def amount_paid(quat_amount, dim_amount, nic_amount, pen_amount):
    """Returns the dollar value of amount paid"""
    dollar_amount = quat_amount * QUARTER + dim_amount * DIME + nic_amount * NICKEL + pen_amount * PENNY
    return round(dollar_amount, 2)


def make_coffee(coffee_type, quarters, dimes, nickles, penny):
    """This function generates the coffee if the coin inserted is equal or more than the price of coffee"""
    dollars = amount_paid(quarters, dimes, nickles, penny)
    actual_amount = MENU[coffee_type]['cost']
    drink = MENU[coffee_type]['ingredients']
    if dollars >= actual_amount:
        for item in drink:
            resources[item] -= drink[item]
        print(f"Here is ${dollars - actual_amount} in change.\nHere is your {coffee_type} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money Refunded.")


def check_ingredient(coffee):
    """Check whether if there is sufficient ingredient to make the coffee"""
    ingredients = MENU[coffee]['ingredients']
    for item in ingredients:
        if resources[item] < ingredients[item] and resources[item] != ingredients[item]:
            return 0, item
    return 1, 'none'


print(coffee_cup)
done_or_not = 1
while done_or_not:
    request = input("What would you like? (Espresso, Latte, Cappuccino): ").lower()
    if request == 'report' or request == 'r':
        report_make()
    elif request == 'espresso' or request == 'latte' or request == 'cappuccino':
        # check resource function must be called
        sufficient, mixture = check_ingredient(request)
        if sufficient:
            no_of_quarters = float(input("Please insert coins.\nHow many Quarters?: "))
            no_of_dimes = float(input("How many Dimes?: "))
            no_of_nickles = float(input("How many Nickles?: "))
            no_of_pennies = float(input("How many Pennies?: "))
            make_coffee(request, no_of_quarters, no_of_dimes, no_of_nickles, no_of_pennies)
            money += MENU[request]['cost']
        else:
            print(f"Sorry there is not enough {mixture}.")
    elif request == 'off':
        done_or_not = 0
    else:
        print("Provide proper input.😵‍💫")
