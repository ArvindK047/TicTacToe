import random
import os

def clear_screen():
    # Clears the terminal screen for a cleaner UI
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        # Better visual alignment
        formatted_row = [cell if cell != '' else ' ' for cell in row]
        print(f" {formatted_row[0]} | {formatted_row[1]} | {formatted_row[2]} ")
        if i < 2:
            print("---+---+---")
    print()

def game_checkwin(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return 1
        if board[0][i] == board[1][i] == board[2][i] != '':
            return 1
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return 1
    if board[0][2] == board[1][1] == board[2][0] != '':
        return 1
    return 0

def game_checkdraw(board):
    # Returns 2 if there are no empty spaces left anywhere on the board
    if not any('' in row for row in board):
        return 2
    return 0

# --- Game Setup ---
board = [['' for _ in range(3)] for _ in range(3)]
game_state = 0
current_player = random.choice(['X', 'O'])

clear_screen()
print('CLI-Based TIC TAC TOE - 2 Players')

# --- Main Game Loop ---
while game_state == 0:
    print_board(board)
    print(f"Player {current_player}'s turn")
    
    try:
        row = int(input('Enter the row (1, 2, or 3): '))
        col = int(input('Enter the column (1, 2, or 3): '))
    except ValueError:
        clear_screen()
        print("Invalid input! Please type numbers only.")
        continue

    if 1 <= row <= 3 and 1 <= col <= 3:
        if board[row - 1][col - 1] == '':
            board[row - 1][col - 1] = current_player
            
            # Check for win
            if game_checkwin(board) == 1:
                clear_screen()
                print_board(board)
                print(f"Player {current_player} wins! 🎉")
                break
                
            # Check for draw
            if game_checkdraw(board) == 2:
                clear_screen()
                print_board(board)
                print("It's a draw! 🤝")
                break
                
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
            clear_screen()
        else:
            clear_screen()
            print("That spot is already taken! Try again.")
    else:
        clear_screen()
        print("Invalid input! Please enter numbers between 1 and 3.")