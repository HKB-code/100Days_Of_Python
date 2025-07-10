def check_answer(guess,answer,turns):
    if guess > answer:
        print('Too high')

        return turns-1
    elif answer> guess:
        print('Too low')

        return turns-1
    elif answer==guess:
        print(f'You Got it. The guess was {guess}') 
        return -1
    

easy_level = 5
difficult_level = 10
from random import randint

def level():
    try:
        levels = input("Choose a difficulty. Type 'easy' or 'hard':").strip().lower()
        if levels == "":
            return 'Please enter difficulties level'
        elif levels not in ["easy", "hard"]:
            return "Invalid difficulty. Please type 'easy' or 'hard'."
        elif levels == "easy":
            return easy_level
        else:
            return difficult_level 


    except  Exception as e:
        return (f"An unexpected erroe occurred: {e}")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    print("---------", answer)
    turns = level()
    print(f"You have {turns} attempts remaining to guess the number..")
    guess = 0 
    while guess!=answer:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns==-1:
            return
        print(f"You have {turns} remaining to guess the number")
        if turns==0:
          print("You've lost the game....")
          return
        elif guess!=answer:
         print("Guess Again")




    

game()