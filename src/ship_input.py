import numpy as np
from src.utils import SYMBOL_WATER, SYMBOL_SHIP, get_board_display

BOARD_SIZE = 10
SHIP_SIZES = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}

def is_valid_placement(board, r, c, size, orientation):
    if orientation == 'h':
        if c + size > BOARD_SIZE:
            return False
        for i in range(size):
            if board[r, c + i] == SYMBOL_SHIP:
                return False
    elif orientation == 'v':
        if r + size > BOARD_SIZE:
            return False
        for i in range(size):
            if board[r + i, c] == SYMBOL_SHIP:
                return False
    else:
        return False
    return True

def place_ship(board, r, c, size, orientation):
    if orientation == 'h':
        for i in range(size):
            board[r, c + i] = SYMBOL_SHIP
    elif orientation == 'v':
        for i in range(size):
            board[r + i, c] = SYMBOL_SHIP
    return board

def get_player_board_setup():
    player_board = np.full((BOARD_SIZE, BOARD_SIZE), SYMBOL_WATER, dtype=str)
    
    for name, size in SHIP_SIZES.items():
        placed = False
        while not placed:
            print(get_board_display(player_board, hide_ships=False))
            print(f"(Placing {name} (Size: {size})")
            
            try:
                coords_input = input("Enter starting coordinates (Row,Col e.g., 0,0): ")
                r_str, c_str = coords_input.split(',')
                r, c = int(r_str.strip()), int(c_str.strip())
            except ValueError:
                print("Invalid coordinates. Must be R,C (0-9).")
                continue
                
            if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE):
                print("Coordinates out of bounds (0-9).")
                continue
                
            orientation = input("Enter orientation (v/h): ").lower().strip()
            
            if is_valid_placement(player_board, r, c, size, orientation):
                player_board = place_ship(player_board, r, c, size, orientation)
                placed = True
            else:
                print("Invalid placement. Ship is out of bounds or overlaps another ship.")
                
    return player_board
