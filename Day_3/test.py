# # By using if and else statements,
#  # we can get our computer to do different things and respond differently depending on different conditions.
# * Exercise :1
# num = int(input("enter number"))
# if(num%2==0):
#   print(f"num {num} is even number")
# else:
# print(f"num {num} is odd number")

# * Exercise 2
# print("Welcome to python pizza delivery")
# sizes= input("What size do you want?\n S, M OR L. \n")
# pepperoni = input("Do you want pepperoni on your pizza?\n Y or N: \n")
# extra_cheese = input("Do you want extra cheese? Y or N: \n")
# bill =0
# if(sizes=='s' or sizes=="S"):
#   bill = 15
#   print("small pizza : 15$")
# elif (sizes=='m' or sizes=="M"):
#   bill = 20
#   print("medium pizza : 20$")
# elif (sizes=='l' or sizes=="L"):
#   bill = 25
#   print("large pizza : 25$")
# else:
#   print("Wrong input:")
# if( pepperoni=='y' or pepperoni=='Y'):
#   if(sizes=="s" or sizes=="S"):
#    bill+=2
#   else:
#     bill+=3
# if(extra_cheese=="y" or extra_cheese=='Y'):
#   bill+=1

# print(f"HERE IS YOUR FINAL BILL ${bill}")

print("Welcome to the rollercoaster ride...")
height = int(input("What is your height in cm? \n"))
bill=0
if height>=120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age?\n"))
  if(age<=12):
    print("Child tickets are 5$")
    bill = 5
  elif(age<=18):
    print("Youth tickets are 7$")
    bill=6
  elif(age>=45 and age<=55):
    print("Have a free ride")
    bill=0
  else:
    print("Adults tickets are 12$")
    bill=12
  
  wants_photo = input("Do you want to have a photo take? Type y for yes and n for no.")
  if wants_photo == 'y' or wants_photo=="Y":
    bill+=3
  print(f"Your final bill is {bill}")
 
else:
  print("Better luck next time")