import numpy as np
from src.ship_input import is_valid_placement, place_ship, SHIP_SIZES
from src.utils import SYMBOL_WATER

BOARD_SIZE = 10

def generate_bot_board():
    bot_board = np.full((BOARD_SIZE, BOARD_SIZE), SYMBOL_WATER, dtype=str)
    
    for name, size in SHIP_SIZES.items():
        placed = False
        while not placed:
            r = np.random.randint(0, BOARD_SIZE)
            c = np.random.randint(0, BOARD_SIZE)
            orientation = np.random.choice(['h', 'v'])
            
            if is_valid_placement(bot_board, r, c, size, orientation):
                bot_board = place_ship(bot_board, r, c, size, orientation)
                placed = True
                
    return bot_board
