import numpy as np
import time
from src.utils import SYMBOL_WATER, SYMBOL_SHIP, SYMBOL_HIT, SYMBOL_MISS, clear_terminal, get_board_display

BOARD_SIZE = 10

def check_for_sunk(board):
    return SYMBOL_SHIP not in board

def display_boards(player_board, bot_board):
    clear_terminal()
    print("--- YOUR BOARD ---")
    print(get_board_display(player_board, hide_ships=False))
    print("\n--- BOT'S BOARD (Tracking) ---")
    print(get_board_display(bot_board, hide_ships=True))

def take_shot(target_board, target_name):
    shot_successful = False
    while not shot_successful:
        try:
            coords_input = input(f"Enter target coordinates (Row,Col) for {target_name}: ")
            r_str, c_str = coords_input.split(',')
            r, c = int(r_str.strip()), int(c_str.strip())
        except ValueError:
            print("Invalid coordinates. Must be R,C (0-9).")
            continue
            
        if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE):
            print("Coordinates out of bounds (0-9).")
            continue
            
        if target_board[r, c] == SYMBOL_HIT or target_board[r, c] == SYMBOL_MISS:
            print("Already fired at this location. Choose a new one.")
            continue
            
        shot_successful = True
        
    is_hit = False
    if target_board[r, c] == SYMBOL_SHIP:
        target_board[r, c] = SYMBOL_HIT
        is_hit = True
    elif target_board[r, c] == SYMBOL_WATER:
        target_board[r, c] = SYMBOL_MISS
        
    return target_board, is_hit

def bot_take_shot(target_board):
    shot_successful = False
    r, c = -1, -1
    
    while not shot_successful:
        r = np.random.randint(0, BOARD_SIZE)
        c = np.random.randint(0, BOARD_SIZE)
        
        if target_board[r, c] != SYMBOL_HIT and target_board[r, c] != SYMBOL_MISS:
            shot_successful = True
            
    is_hit = False
    if target_board[r, c] == SYMBOL_SHIP:
        target_board[r, c] = SYMBOL_HIT
        is_hit = True
    elif target_board[r, c] == SYMBOL_WATER:
        target_board[r, c] = SYMBOL_MISS
        
    return target_board, is_hit, r, c

def start_game(player_board, bot_board):
    turn = 'player'
    
    while True:
        display_boards(player_board, bot_board)
        
        if turn == 'player':
            print("\n--- YOUR TURN ---")
            bot_board, is_hit = take_shot(bot_board, "Bot")
            
            if is_hit:
                print("HIT! You hit a ship!")
            else:
                print("MISS. Shot landed in the water.")
            
            time.sleep(1)
            
            if check_for_sunk(bot_board):
                display_boards(player_board, bot_board)
                print("\n*** CONGRATULATIONS! YOU SUNK ALL ENEMY SHIPS AND WON! ***")
                break
                
            if not is_hit:
                turn = 'bot'

        elif turn == 'bot':
            print("\n--- BOT'S TURN ---")
            time.sleep(1.5)
            
            player_board, is_hit, r, c = bot_take_shot(player_board)
            
            print(f"Bot shot at: ({r},{c})")
            if is_hit:
                print("Bot HIT! Your ship was hit!")
            else:
                print("Bot MISS. Safe this time.")
                
            time.sleep(1.5)
            
            if check_for_sunk(player_board):
                display_boards(player_board, bot_board)
                print("\n*** GAME OVER! THE BOT SUNK ALL YOUR SHIPS! ***")
                break
                
            if not is_hit:
                turn = 'player'
