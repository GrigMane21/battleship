import os
import numpy as np

SYMBOL_WATER = '~'
SYMBOL_SHIP = 'S'
SYMBOL_HIT = 'X'
SYMBOL_MISS = 'O'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_board_display(board, hide_ships=True):
    header = '  0 1 2 3 4 5 6 7 8 9'
    output = [header]
    
    for r in range(10):
        row_str = f'{r} '
        for c in range(10):
            cell = board[r, c]
            if hide_ships and cell == SYMBOL_SHIP:
                row_str += SYMBOL_WATER + ' '
            else:
                row_str += cell + ' '
        output.append(row_str)
        
    return '\n'.join(output) 
