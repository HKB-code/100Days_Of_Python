def tic_tac_toe():
    print("Welcom to Tic-Tac-Toe!")
    board = [" " for _ in range(9)]
    current_player ="X"
    print(board)


    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("-"* 9)
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("-"* 9)
        print(f"{board[6]} | {board[7]} | {board[8]}")
        
    def check_winner():
        winner_condition = [(0,1,2),(3,4,5),(6,7,8),  #rows
                            (0,3,6),(1,4,7),(2,5,8), #columns
                             (0,4,8), (2,4,6) #diagonals   
                             ]   
        for a,b,c in winner_condition:
            if board[a] == board[b] == board[c] !=" ":
                return board[a]
        if " " not in board:
            return "Draw"
        return None

    while True:
        print_board()
        move =input(f"player {current_player}, enter position (1-9): ")     
        try: 
            move = int(move)-1
            if 0<=move<=8 and board[move] == " ":
                board[move] = current_player
                winner = check_winner()
                if winner:
                    print_board()
                    if winner=='Draw':
                        print("Its a draw")
                    else:
                        print(f"Player {winner} wins!")
                    break
                current_player = 'O' if current_player =='X' else 'X'
            else:
                print("Invalid move! Try again.")
        except ValueError:      
          print("Enter a number between 1 and 9!")

    

should_play = True
while should_play:
    tic_tac_toe()
    play_agian = input("Play again? (y/n): ").lower()
    if play_agian != 'y':
        should_play = False

            
            





