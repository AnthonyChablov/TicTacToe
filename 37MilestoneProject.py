# Two Player Tic - Tac - Toe

# The Components

# Step 1: We use a Dictionary and its key=value to begin associating numbers to their relative positions on the board like a keypad.


board={'7':' ','8':' ','9':' ',
       '4':' ','5':' ','6':' ',
       '1':' ','2':' ','3':' '}

# Step 2: Displaying the board 
def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'] )
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])

# Step 3: Take in player input about which space to change,
    # We are making sure the user is inputting a integer between 1-9

def play_input():
    spot ='string'
    condition=False

    while spot.isdigit()== False or condition==False:
        spot=input('Which spot would you like to put your piece? (1-9): ')
        if spot.isdigit()==False:
            print('Please enter a number')
        if spot.isdigit()==True:
            if int(spot) in range(1,10):
                condition==True
                return spot
            else:
                print('Please enter a number between 1 and 9')
                condition==False

# Step 4: Functionality of the game
    # Need to keep track of each turn and each each input within the board 

def game():
    turn ='O'
    gamecount=0

    # We are going to keep track of each turn 
    for i in range(10):
        print_board(board)
        print('It is your turn ' + turn)
        move_choice=play_input()
        
        ##
        if board[move_choice]==' ':
            board[move_choice]=turn
            gamecount+=1
        else:
            print('That spot has already been played')
            continue


        # We are now going to check who wins after every 5 turns
        if gamecount>=5:
            # Top Row
            if (board['7']==board['8']==board['9']!=' '):
                print_board(board)
                print(turn +' has won!')
                break
            # Middle Row    
            elif (board['4']==board['5']==board['6']!=' '):
                print_board(board)
                print(turn +' has won!')
                break
            # Bottom Row
            elif (board['1']==board['2']==board['3']!=' '):
                print_board(board)
                print(turn +' has won!')
                break
            # Diagonal (Top right to bottom left)
            elif(board['7']==board['5']==board['3']!=' '):
                print_board(board)
                print(turn +' has won!')
                break
            # Diagonal (Bottom right to Top left)
            elif(board['1']==board['5']==board['9']!=' '):
                print_board(board)
                print(turn +' has won!')
                break
            # Down Left
            elif(board['7']==board['4']==board['1']!=' '):
                print_board(board)
                print(turn +' has won!')
                break
            # Down Middle
            elif(board['8']==board['5']==board['2']!=' '):
                print_board(board)
                print(turn +' has won!')
                break
            #Down Right
            elif(board['9']==board['6']==board['3']!=' '):
                print_board(board)
                print(turn +' has won!')
                break

        # Checking for a tie
        if gamecount==9:
            print('Tie Game! \nGame Over!')

        # Changing who's turn it is after every inputted move by a player 
        if turn=='X':
            turn='O'
        else:
            turn='X'

# Step 5: Ask the player if they wanna keep on playing
    
def keep_playing():
    keep_playing=True

    game()

    while keep_playing==True:
        play=input('Would you like to keep playing? (Y/N): ')
        if play=='y' or play =='Y':
            keep_playing= True
        else:
            print('Game Over! Thankyou for playing!')
            keep_playing= False


           
if __name__ == "__main__":
    keep_playing()