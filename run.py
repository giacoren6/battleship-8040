# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


#storyboard
# x for taking the ship and hit battleship
# ' ' for avalible space
# '-' for missed shot


import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleship-8040')


from random import randint


BOARD_GAME_HIDDEN = [[' '] * 9 for x in range(9)]
GAME_GUESS_BOARD = [[' '] * 9 for x in range(9)]

letter_for_number = {'A': 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' 8} 

def print_board(board):
    print('A B C D E F G H I')
    print(' -------------------')
    row_number = 1 

    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
 
def ship_create(board):
    for ship in range(6):
        ship_row, ship_column = randint(0,8), randint(0,8)
        while board[ship_row][ship_column] == 'X':
            ship_row,ship_column = randint(0,8), randint(0,8)
            board[ship_row][ship_column] = 'X'

def get_ship_location():
    row = input('Enter a ship row 1-9:' )
    while row not in '1 2 3 4 5 6 7 8 9':
        print('Enter a valid row')
    row = input('Enter a ship row 1-9')
    column = input('Enter a ship column  A-I:' ).upper()
    while column not in 'ABCDEFGHI':
            column = input('Enter a ship column  A-I:' ).upper()
            return int(row) - 1  letter_for_number[column]






def count_hit(board):
    count = 0:
    for row in board:
    for column in row:
    if column == 'X':
        count += 1
        return count



ship_create(BOARD_GAME_HIDDEN)
turns = 10
while turns > 0:
    print('Welcome to Battleship-8040')
    print_board(GAME_GUESS_BOARD)
    row, column = get_ship_location()
    if GAME_GUESS_BOARD[row][column] == '-':
    print('You already guess it ')
    elif BOARD_GAME_HIDDEN[row][column] == 'X':
        print('Contrats')
        GAME_GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('You Missed')
        GAME_GUESS_BOARD[row][column] '-':
        turns -= 1
    if count_hit(GAME_GUESS_BOARD) == 6:
        print('Congrats You Win !!!')
        break
    print('You have' + str(turns) + 'Remaining turns')
    if turns = 0:
    print('Game Over')
    break
    

