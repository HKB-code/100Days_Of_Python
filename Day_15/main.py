MENU = {
  "expresso":{
    "ingredients":{
          "water":50,
           "coffee":18
  },
    "cost":1.5
  },
  "latte": {
    "ingredients":{
        "water":50,
         "coffee":18
  },
    "cost":2.5
  },
  "cacppuccino":{
    "ingredients":{
      "water": 250,
      "milk":100,
      "coffee":24
    },
    "cost":3.0
  }
}

resources = {
  "water": 300,
  "milk":200,
  "coffee":100
}

#TODO 1. Print report of all coffee machine resources

def user_inputs():
    return input("What would you like? (expresso/latte/cappuccino): ")

# def isSufficient(drink,coins):
#     if drink in MENU and drink =="cacppuccino":
#         ing = MENU[drink]["ingredients"]
#         if resources["water"] <ing["water"]:
#           print("Sorry there is no enough water")
#         if resources["coffee"]< ing["coffee"]:
#           print("Sorry there is no enough coffee")
#         if resources["milk"]<ing["milk"]:
#           print("Sorry there is no enough milk")
#         if MENU[drink]["cost"]>coins:
#           print("Sorry there is no enough coins")
#         return False
#     elif drink in MENU :
#         ing = MENU[drink]["ingredients"]
#         if resources["water"] <ing["water"]:
#           print("Sorry there is no enough water")
#         if resources["coffee"]< ing["coffee"]:
#           print("Sorry there is no enough coffee")
        
#         if MENU[drink]["cost"]>coins:
#           print("Sorry there is no enough coins")
#         return False
#     elif drink not in MENU:
#        print("Oops there is no drink like that.")
#        return False
#     return True
       
def isSufficient(drink,coins):
    if drink not in MENU:
        print("Oops, there is no drink like that.")
        return False
    ing = MENU[drink]["ingredients"]
    for item in ing:
       if resources[item]<ing[item]:
         print(f"Sorry there is no enough {item}")
         return False
   
    if MENU[drink]["cost"]>coins:
         print("Sorry that's not enough money. Money refunded.")
         return False
    return True
       
def coin_Process():
    quarters = int(input("How many quaters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    return quarters*0.25 + dimes*0.10 + nickles * 0.05+ pennies*0.01

       
def money_refund(drink,money):
    ing = MENU[drink]["cost"]
    if money>ing:
        refund = round(money-ing,2)
        return refund

def make_drink(drink):
    ing = MENU[drink]["ingredients"]
    for item in ing:
        resources[item] = resources[item] - ing[item]
    return f"Here is your {drink}. Enjoy!"

def turn_off():
    global should_continue
    should_continue = False

Money = 0
should_continue = True

while should_continue:
    user_input = user_inputs()
    if user_input == 'report':
      print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {Money}")
    elif user_input == 'off':
        turn_off()
    else:
        amount = coin_Process()
        success = isSufficient(user_input,amount)
        if success:
            money_refunded = money_refund(user_input,amount)
            print(f"Here is ${money_refunded} dollars in change")
            Money += MENU[user_input]["cost"]
            drink = make_drink(user_input)
            print(drink)

