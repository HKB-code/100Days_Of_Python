import random
from logo import logo

print(logo)
def deal_cards():
    """Return a random card from deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_cards(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards)==21 and len(cards)==2:
     return 0 
  if 11 in cards and sum(cards)>21:
     cards.remove(11)
     cards.append(1)
  return sum(cards)

def compare_score(user_score,computer_score):
   if user_score == 0 :
      return "Win with the BlackJack"
   elif computer_score ==0:
      return "Lose, Computer hit BlackJack"
   elif user_score>21:
      return "You went over, You Lose"
   elif computer_score>21:
      return "Opponent went over, You Win"
   elif user_score==computer_score:
      return "Draw"
   elif user_score>computer_score:
      return "You Win"
   else: 
      return "You Lose"
   

def play_game():
   print(logo)
   user_cards = []
   computer_cards = []
   game_over = False
   user_score = -1
   computer_score = -1


   for _ in range(2):
      user_cards.append(deal_cards())
      computer_cards.append(deal_cards())
   # print(user_cards)
   # print(computer_cards)

   while not game_over:
      user_score = calculate_cards(user_cards)
      computer_score = calculate_cards(computer_cards)
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer's first cards: {computer_cards[0]}")

      if user_score ==0 or  computer_score == 0 or user_score>21:
         game_over = True
      else:
         user_should_deal = input("Type 'Y' to get another card, type 'N' to pass:\n").lower()
         if user_should_deal == 'y':
           user_cards.append(deal_cards())
         else:
            game_over=True

   while computer_score!=0 and computer_score<17:
      computer_cards.append(deal_cards())
      computer_score = calculate_cards(computer_cards)

   print(f"Your final hand: {user_cards}, final score: {user_score}")
   print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
   print(compare_score(user_score,computer_score))
         

   

play =  input("Do you want to play another game. Type 'Y' for yes or 'N' for no ").lower()
  
while play == 'y':
  play_game()