from hangmanLogo import logo,stages
import random,hangman_words

word = random.choice(hangman_words.word_list)
display = ["_"]*len(word)

print(display)
print(word)


lifes = 6
game_over = False 

while not game_over:
    guess = input("guess a letter")
    if guess in display:
        print("You already guess the letter")
        continue

    for i in range(len(word)):
        letter = word[i]
        if letter ==guess:
            display[i] = letter
        if guess not in word:
            lifes-=1
            if lifes>0:
                print("Oops you lost 1 life" if lifes==5 else "you lost another life")
                print(f"{lifes} lives left")
            
            elif lifes==0:
                game_over = True
                print("You loose the game")
                print(f"The word is {word}")

    if "_" not in display:
        game_over = True
        print("You loose the game")
     
    print(stages[lifes])
    print(display)
    