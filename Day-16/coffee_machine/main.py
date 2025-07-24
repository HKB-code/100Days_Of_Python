from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
is_on = True
while is_on:
    user_input = input(f"what you want to oredre?{menu.get_items()} ")
    if user_input == 'report':
      coffee.report()
      money.report()
    elif user_input  == 'off':
       is_on = False
    else:
     drink =  menu.find_drink(user_input)
     if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
        coffee.make_coffee(drink)
   