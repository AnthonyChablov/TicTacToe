#Two Player Tic - Tac - Toe

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

    while spot.isdigit()== False and condition==False:
        spot=input('Which spot would you like to put your piece? (1-9)')
        if spot.isdigit()==False:
            print('Please enter a number')
        if spot.isdigit()==True:
            if int(spot) in range(1,10):
                condition=True
                return spot
            else:
                print('Please enter a number between 1 and 9')
                condition=False
                
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

        if board[move_choice]==' ':
            board[move_choice]=turn
            gamecount+=1
        else:
            print('That spot has already been played')
            continue

    # Changing who's turn it is after every move by a player 
    for x in range(10):
        if turn=='X':
            turn='O'
        else:
            turn='X'

    # We are now going to check who wins after every 5 turns
    if gamecount>=5:
        if (board[7]==board[8]==board[9]==turn):
            print_board(board)
            print(turn +'has won!')
            
        elif (board[4]==board[5]==board[6]==turn):
            print_board(board)
            print(turn +'has won!')
        elif (board[1]==board[2]==board[3]==turn):
            print_board(board)
            print(turn +'has won!')
        elif(board[7]==board[5]==board[3]==turn):
            print_board(board)
            print(turn +'has won!')
        elif(board[1]==board[5]==board[9]==turn):
            print_board(board)
            print(turn +'has won!')
        elif(board[7]==board[4]==board[1]==turn):
            print_board(board)
            print(turn +'has won!')
        elif(board[8]==board[5]==board[2]==turn):
            print_board(board)
            print(turn +'has won!')
        elif(board[9]==board[6]==board[3]==turn):
            print_board(board)
            print(turn +'has won!')

    # Checking for a tie

    if gamecount==9:
        print('Tie Game! \n Game Over!')


    



game()