# import random

# track_counts = {}
# def dice_rolling():
#     print("Welcome to the Dice Rolling Simulator")
#     count = 0

#     while True:
#         h=input("PRESS ENTER TO ROLL TWO DICE (OR 'Q' TO QUIT)").lower()
#         if h == "q":
#             print("Thanks for playing!")

#             break
#         count+=1
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         total = die1+die2
#         track_counts [count] = total

#         print(f"You rolled: {die1} + {die2} = {total}")

#         play_again = input("Roll again? (y/n): ").lower()
#         if play_again != 'y':
#             print("Thanks for playing!")
#             print(track_counts)
#             break


# dice_rolling()

import random

def dice_rolling():
    print("Welcome to the Dice Rolling Simulator!")
    
    # Get number of dice
    while True:
        try:
            num_dice = int(input("How many dice to roll? (1 or more): "))
            if num_dice >= 1:
                break
            print("Please enter a number of 1 or more.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Initialize tracking dictionaries
    track_counts = {}  # Roll number -> total
    total_frequency = {}  # Total value -> frequency
    count = 0

    while True:
        h = input("Press Enter to roll the dice (or 'q' to quit): ").lower()
        if h == 'q':
            break
        if h != '':  # Ignore non-empty input except 'q'
            print("Press Enter to roll or 'q' to quit.")
            continue
        
        count += 1
        # Roll the specified number of dice
        dice = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(dice)
        
        # Store roll result
        track_counts[count] = total
        
        # Update frequency of total
        total_frequency[total] = total_frequency.get(total, 0) + 1
        
        # Display roll result
        dice_str = " + ".join(str(d) for d in dice)
        print(f"You rolled: {dice_str} = {total}")
        
        # Ask to roll again
        play_again = input("Roll again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    # Display results
    print("\nThanks for playing!")
    print(f"Roll history: {track_counts}")
    print("Frequency of totals:")
    # Possible totals range from num_dice*1 to num_dice*6
    min_total = num_dice
    max_total = num_dice * 6
    for total in range(min_total, max_total + 1):
        freq = total_frequency.get(total, 0)
        print(f"Total {total}: {freq} time(s)")

    # Ask to play again
    replay = input("\nPlay again? (y/n): ").lower()
    if replay == 'y':
        dice_rolling()

dice_rolling()