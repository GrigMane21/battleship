import numpy as np
from src.utils import SYMBOL_WATER, SYMBOL_SHIP, SHIP_SIZES, get_board_display

def is_valid_placement(board, r, c, size, direction):
    """
    Checks if a ship can be placed at the given location without overlap or going off-board.
    Also ensures a 1-cell buffer around the ship.
    """
    rows, cols = board.shape
    r_end, c_end = r, c
    
    if direction == 'H':
        c_end += size
        if c_end > cols:
            return False
    else: 
        r_end += size
        if r_end > rows:
            return False

    
    for i in range(r - 1, r_end + 1):
        for j in range(c - 1, c_end + 1):
            if 0 <= i < rows and 0 <= j < cols:
                if board[i, j] == SYMBOL_SHIP:
                    return False
    return True

def place_ship(board, r, c, size, direction):
    """Places a ship on the board."""
    if direction == 'H':
        board[r, c:c + size] = SYMBOL_SHIP
    else: 
        board[r:r + size, c] = SYMBOL_SHIP

def get_player_board_setup():
    """Prompts the player to place all ships on the board."""
    board = np.full((10, 10), SYMBOL_WATER, dtype=str)
    
    for name, size in SHIP_SIZES.items():
        while True:
            print(get_board_display(board, hide_ships=False))
            print(f"Placing {name} (Size: {size})")
            
            
            try:
                coords = input("Enter starting coordinates (Row,Col e.g., 0,0): ")
                r, c = map(int, coords.split(','))
                if not (0 <= r < 10 and 0 <= c < 10):
                    raise ValueError
            except:
                print("Invalid coordinates. Must be R,C (0-9).")
                continue

            
            direction = input("Enter direction (H for Horizontal, V for Vertical): ").upper()
            if direction not in ['H', 'V']:
                print("Invalid direction. Must be H or V.")
                continue

            if is_valid_placement(board, r, c, size, direction):
                place_ship(board, r, c, size, direction)
                break
            else:
                print("Invalid placement. Ship overlaps, touches another ship, or goes off-board.")

    return board
