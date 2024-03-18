from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_card = Menu()

make_coffee = True

while make_coffee:
    drink_choice = input("What would you like? (Espresso, Latte, Cappuccino): ").lower()
    if drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink_choice == "off":
        make_coffee = False
    else:
        drink = menu_card.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
