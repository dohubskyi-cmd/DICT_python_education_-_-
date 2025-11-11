def print_grid(cells_list):
    print("---------")
    print(f"| {cells_list[0]} {cells_list[1]} {cells_list[2]} |")
    print(f"| {cells_list[3]} {cells_list[4]} {cells_list[5]} |")
    print(f"| {cells_list[6]} {cells_list[7]} {cells_list[8]} |")
    print("---------")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

def get_game_state(board):
    x_wins = check_winner(board, 'X')
    o_wins = check_winner(board, 'O')
    empty_count = board.count('_')

    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if empty_count == 0:
        return "Draw"
    return "Game not finished"

cell_list = list("_" * 9)
current_player = 'X'
game_state = "Game not finished"

print_grid(cell_list)

while game_state == "Game not finished":
    try:
        coords = input("Enter the coordinates: ").split()
        row, col = int(coords[0]), int(coords[1])
        
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        
        index = (row - 1) * 3 + (col - 1)
        
        if cell_list[index] != '_':
            print("This cell is occupied! Choose another one!")
            continue
        
        cell_list[index] = current_player
        print_grid(cell_list)
        
        game_state = get_game_state(cell_list)
        
        if game_state == "Game not finished":
            current_player = 'O' if current_player == 'X' else 'X'
            
    except (ValueError, IndexError):
        print("You should enter numbers!")

print(game_state)
