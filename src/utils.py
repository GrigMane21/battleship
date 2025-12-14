import os
import time
import numpy as np

COLOR_WATER = '\033[94m'  # Blue
COLOR_MISS = '\033[97m'   # White/Light Gray
COLOR_HIT = '\033[91m'    # Red
COLOR_SHIP = '\033[92m'   # Green
COLOR_END = '\033[0m'     # Reset

SYMBOL_WATER = '~'
SYMBOL_SHIP = 'S'
SYMBOL_MISS = 'O'
SYMBOL_HIT = 'X'

def clear_terminal():
    """Clears the terminal screen for better presentation."""
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_board_display(board, hide_ships=True):
    """
    Generates a colored, string representation of the board.
    
    :param board: The NumPy array representing the game board.
    :param hide_ships: If True, hides 'S' (ships) and shows them as water (for the bot's board).
    :return: A string ready for printing.
    """
    output = "  " + " ".join([str(i) for i in range(10)]) + "\n"
    
    for r_idx, row in enumerate(board):
        output += str(r_idx) + " "
        for cell in row:
            char = str(cell)
            color = COLOR_END
            
            if char == SYMBOL_WATER:
                color = COLOR_WATER
            elif char == SYMBOL_MISS:
                color = COLOR_MISS
            elif char == SYMBOL_HIT:
                color = COLOR_HIT
            elif char == SYMBOL_SHIP:
                if hide_ships:
                    color = COLOR_WATER
                    char = SYMBOL_WATER  
                else:
                    color = COLOR_SHIP 

            output += f"{color}{char}{COLOR_END} "
        output += "\n"
    return output


SHIP_SIZES = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}
