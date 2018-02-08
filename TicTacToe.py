from IPython.display import clear_output

def display_board(board):  #function to print the board
    clear_output()
    print '   |   |'
    print ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]
    print '   |   |'

def player_input():   #function to get player's input

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input("Player 1: Do you want X or O").upper()   #.upper() to automatically convert lowercase
                                                                     #'O' or 'X' to corresponding uppercase
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):  #to assign given position with given marker('X' or 'O')
    board[position] = marker

def win_check(board,marker):  #to check if someone has won or not
    return ((board[7] == board[8] == board[9] == marker) or (board[4] == board[5] == board[6] == marker) or
           (board[1] == board[2] == board[3] == marker) or (board[7] == board[4] == board[1] == marker) or
            (board[8] == board[5] == board[2] == marker) or (board[9] == board[6] == board[3] == marker) or
           (board[7] == board[5] == board[3] == marker) or (board[9] == board[5] == board[1] == marker)
           )

import random
def choose_first():            #to randomly select which player goes first
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board , position):  #returns boolean indicating whether the space on board is freely available
    return board[position] == ' '

def full_board_check(board):  #returns boolean indicating whether the board is full or not
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board,player): #to get player's next position. also checks if space is there at required position. If not , asks for another input.
    position = ' '   #using strings because of raw_input().
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = raw_input(player + ' : Choose your next position:(1-9)')
    return int(position)

def replay():   #asks if players want to play again
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y') #note here startswith()

print 'Welcome to Tic Tac Toe!'

while True:
    #reset the board
    theBoard = [' '] * 10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print turn + ' will go first'
    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard,'Player 1')
            place_marker(theBoard , player1_marker , position)

            if win_check(theBoard , player1_marker):
                display_board(theBoard)
                print 'Congratulations! Player 1 has won the game!'
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print 'The game is a draw'
                    break
                else:
                    turn = 'Player 2'

        else: #Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard,'Player 2')
            place_marker(theBoard , player2_marker , position)

            if win_check(theBoard , player2_marker):
                display_board(theBoard)
                print 'Congratulations! Player 2 has won the game!'
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print 'The game is a tie'
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
