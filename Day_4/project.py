import random
user_input = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors. \n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]

if(user_input>=3):
    print("oops please select the right input")
else:
    print(game[user_input])
    computer_choice = random.randint(0,2)
    print(game[computer_choice])
    if(user_input==0 and computer_choice==2):
        print("You win")
    elif (user_input==2 and computer_choice==0):
        print("You lose")
    elif(user_input>computer_choice):
        print("You win")
    elif(user_input<computer_choice):
        print("You lose")
    else:
        print("Draw")
