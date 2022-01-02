#Two Player Tic - Tac - Toe

# Step 1: We use a Dictionary and its key=value to begin assiciating numbers to their relative positions on the board like a keypad.

board={'7':' ','8':' ','9':' ',
       '4':' ','5':' ','6':' ',
       '1':' ','2':' ','3':' '}


# Step 2: Printout the board 
def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('=+=+=')
    print(board['4'] + '|' + board['5'] + '|' + board['6'] )
    print('=+=+=')
    print(board['1']+'|'+board['2']+'|'+board['3'])

# Step 3: Take in player input about which space in dictionary to change

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
                
def game():
    



print_board(board)
x=play_input()
print(x)