import numpy as np
import cv2
import os
import time

from src.utils import clear_terminal
from src.ship_input import get_player_board_setup
from src.bot_generation import generate_bot_board
from src.gameplay import start_game

SHIP_SIZES = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}

def run_startup_animation():
    print("\n--- Running OpenCV Animation Check (Simulated) ---")
    
    width, height = 200, 100
    dummy_image = np.zeros((height, width, 3), dtype=np.uint8) 
    
    cv2.putText(dummy_image, 
                "Loading...", 
                (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, 
                (0, 255, 0), 
                1)
    
    time.sleep(1)
    print("OpenCV methods successfully executed.")
    print("------------------------------------------\n")

def main():
    clear_terminal()
    print("WELCOME TO BATTLESHIP!")
    
    run_startup_animation()

    print("--- Player Setup ---")
    player_board = get_player_board_setup()
    
    print("--- Bot Setup ---")
    bot_board = generate_bot_board()
    
    start_game(player_board, bot_board)

if __name__ == "__main__":
    main()
