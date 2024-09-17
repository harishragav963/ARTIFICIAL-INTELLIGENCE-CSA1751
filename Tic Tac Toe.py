# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

# Function to check if the board is full
def check_full(board):
    return all([spot != " " for row in board for spot in row])

# Function to get player's move
def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("This spot is already taken. Choose another.")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number between 1 and 9.")

# Main function to control the game flow
def tic_tac_toe():
    # Initialize an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Print instructions for the game
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'.")
    print("Enter your move as a number from 1 to 9 corresponding to the grid below:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9\n")

    # Variable to track the current player ('X' or 'O')
    current_player = 'X'
    
    # Game loop
    while True:
        print_board(board)
        
        # Get the current player's move
        row, col = get_player_move(board, current_player)
        
        # Place the player's marker on the board
        board[row][col] = current_player
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (a draw)
        if check_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
