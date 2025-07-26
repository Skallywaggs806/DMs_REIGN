import requests

from src.save_to_file import save_to_file
from src.dice_rolling import roll_dice, roll_dice_stats
from src.npc_gen import generate_npc
from src.dnd_data import *
from src.encounter_generator import generate_encounter

print("Hello! I am your DM assistant.")

while True:
    print("Please choose an option:")
    print("1. Generate a new NPC")
    print("2. Roll Dice")
    print("3. Generate Encounter")
    
    print("4. Exit")
    
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
        dice_roll = input("Enter dice roll in format 'XdY+Z' (e.g., '2d6+3'): ")
        purpose = input("Enter purpose of the roll (e.g., attack, skill check): ")
        print(f"Rolling {dice_roll} for {purpose}...")
        try:
            result = roll_dice(dice_roll, purpose)
            print(f"Result of rolling {dice_roll} for {purpose}: {result}")
            save_to_file(f"Result of rolling {dice_roll} for {purpose}: {result}", "DM_Data/roll_results_logs.txt")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == '3':
        num_enemies = int(input("Enter number of enemies in the encounter: "))
        apl = int(input("Enter average party level (APL): "))
        encounter_name = input("Enter name for the encounter: ")
        generate_encounter(num_enemies, apl, encounter_name)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")










