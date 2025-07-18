
# from logo import logo, vs
# from game_data import data
# import random


# def formatData(account):
#     """Format the account data into printable format"""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}"


# def check_answer(user_guess,a_followers,b_followers):
#     if(a_followers>b_followers):
#         return user_guess=='a'
#     else:
#         return user_guess=="b"
    

# print(logo)
# account_a = random.choice(data)
# account_b = random.choice(data)
# if account_a==account_b:
#     account_b = random.choice(data)

# score = 0 
# game_over = False

# while not game_over:
#     print(f"Compare A: {formatData(account_a)}")
#     print(vs)
#     print(f"Compare B: {formatData(account_b)}")


#     guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

#     #  clear screen
#     print("\n"*20)
#     print(logo)


#     a_follower = account_a["follower_count"]
#     b_follower = account_b["follower_count"]



#     is_correct = check_answer(guess,a_follower,b_follower)
#     if is_correct:
#         score+=1
#         print(f"You're right!, Current Score {score}")
#         account_a = account_b
#         account_b = random.choice(data)
#         if account_a== account_b:
#             account_b = random.choice(data)
#     else: 
#         print(f"Sorry, that's wrong, Final score {score}")
#         game_over = True



  
# ///////////

from logo import logo, vs
from game_data import data
import random

def format_data(account):
    """Return formatted string for account info."""
    name = account["name"]
    descr = account["description"]
    country = account["country"]
    return f"{name}, a {descr}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Return True if guess is correct."""
    # Outside of strings, \ is used to split long lines of code across multiple lines for readability.
    return (guess == "a" and a_followers > b_followers) or \
           (guess == "b" and b_followers > a_followers)



# Game start
print(logo)
score = 0
game_should_continue = True

account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

while game_should_continue:
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    if check_answer(guess, a_followers, b_followers):
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False