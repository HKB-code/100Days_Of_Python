print("Welcome to the tip calculator.")
bill =float (input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give 10 ,12 or 15?\n"))
print(tip)
if(tip!=10 and tip!=12 and tip!=15):
    print("You choose wrong tip value?")
else: 
    split = int(input("How many people to split the bill?\n"))
    amount = (bill*(tip/100))
    each_amount = "{:.2f}".format(amount/split)
    print(f"The total amount is {amount}, Each person should pay: {each_amount}")