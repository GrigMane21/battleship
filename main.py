import os
import time
from src.utils import clear_terminal
from src.ship_input import get_player_board_setup
from src.bot_generation import generate_bot_board
from src.gameplay import start_game

def main():
    """
    Main function to run the Battleship game.
    """
    # clear_terminal()  # <--- Keep this line commented out for now
    print("🚢 WELCOME TO BATTLESHIP! 🚢")
    time.sleep(1)

    # 1. Player Setup
    print("\n--- Player Setup ---")
    player_board = get_player_board_setup()

    # 2. Bot Setup
    print("\n--- Bot Setup ---")
    print("The Bot is placing its ships...")
    bot_board = generate_bot_board()
    time.sleep(2)
    # clear_terminal()  # <--- Keep this line commented out for now
    
    # 3. Start Game Loop
    start_game(player_board, bot_board)

if __name__ == '__main__':
    main()
