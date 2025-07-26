import requests

from src.save_to_file import save_to_file
from src.dice_rolling import roll_dice, roll_dice_stats
from src.npc_gen import generate_npc
from src.dnd_data import *

print("Hello! I am your DM assistant.")

while True:
    print("Please choose an option:")
    print("1. Generate a new NPC")
    print("2. Roll Dice")
    print("3. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == '1':
        level = input("Enter NPC level (default is 1): ")
        if not level.isdigit():
            level = 1
        else:          
            level = int(level)
            if level < 1:
                print("Level must be at least 1. Setting to default level 1.")
                level = 1
        generate_npc(level)
    elif choice == '2':
        num_dice = int(input("Enter number of dice to roll: "))
        num_sides = int(input("Enter number of sides on each die: "))
        modifier = int(input("Enter modifier to apply: "))
        purpose = input("Enter purpose of the roll (e.g., attack, skill check): ")
        print(f"Rolling {num_dice}d{num_sides} with modifier {modifier} for {purpose}...")
        try:
            result = roll_dice(num_dice, num_sides, modifier, purpose)
            print(f"Result of rolling {num_dice}d{num_sides} with modifier {modifier} for {purpose}: {result}")
            save_to_file(f"Result of rolling {num_dice}d{num_sides} with modifier {modifier} for {purpose}: {result}", "DM_Data/roll_results_logs.txt")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")










