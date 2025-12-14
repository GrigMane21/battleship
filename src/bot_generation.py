import numpy as np
import random
from src.utils import SYMBOL_WATER, SYMBOL_SHIP, SHIP_SIZES
from src.ship_input import is_valid_placement, place_ship

def generate_bot_board():
    """Generates a board with ships placed randomly for the bot."""
    board = np.full((10, 10), SYMBOL_WATER, dtype=str)
    
    for size in SHIP_SIZES.values():
        placed = False
        while not placed:
            # Random starting position
            r = random.randint(0, 9)
            c = random.randint(0, 9)
            
            # Random direction
            direction = random.choice(['H', 'V'])
            
            if is_valid_placement(board, r, c, size, direction):
                place_ship(board, r, c, size, direction)
                placed = True
    return board
