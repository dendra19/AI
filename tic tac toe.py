import os
import time

board = [' '] * 10  # Using index 1-9 for the game board
player = 1

# Constants for game states
Win = 1
Draw = -1
Running = 0

Game = Running
Mark = 'X'

def DrawBoard():
    print("%c | %c | %c" % (board[1], board[2], board[3]))
    print("__|___|__")
    print("%c | %c | %c" % (board[4], board[5], board[6]))
    print("__|___|__")
    print("%c | %c | %c" % (board[7], board[8], board[9]))
    print("  |   |  ")

def CheckPosition(x):
    return board[x] == ' '

def CheckWin():
    global Game

    # Horizontal winning conditions
    if board[1] == board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        Game = Win

    # Vertical winning conditions
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        Game = Win

    # Diagonal winning conditions
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        Game = Win
    elif board[3] == board[5] == board[7] and board[3] != ' ':
        Game = Win

    # Check for draw
    elif all(cell != ' ' for cell in board[1:]):
        Game = Draw
    else:
        Game = Running

print("Tic-Tac-Toe Game")
print("Player 1 [X] -- Player 2 [O]\n")
print("Please wait...")
time.sleep(1)

while Game == Running:
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawBoard()
    if player % 2 != 0:
        print("Player 1's Chance")
        Mark = 'X'
    else:
        print("Player 2's Chance")
        Mark = 'O'
        
    try:
        choice = int(input("Enter the position between [1-9] where you want to mark: "))
        if choice < 1 or choice > 9 or not CheckPosition(choice):
            print("Invalid move. Try again.")
            continue
        board[choice] = Mark
        player += 1
        CheckWin()
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number between 1 and 9.")

os.system('cls' if os.name == 'nt' else 'clear')
DrawBoard()

if Game == Draw:
    print("Game Draw")
elif Game == Win:
    player -= 1
    if player % 2 != 0:
        print("Player 1 Won")
    else:
        print("Player 2 Won")
