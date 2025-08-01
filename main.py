import requests

from src.save_to_file import save_to_file
from src.dice_rolling import roll_dice, roll_dice_stats
from src.npc_gen import generate_npc
from src.dnd_data import *
from src.encounter_generator import generate_encounter
from src.log_magic_items import log_magic_items
from src.generate_gold import generate_gold

print("Hello! Welcome to Dungeon Masters R.E.I.G.N.!")

while True:
    print("Please choose an option:")
    print("1. Generate a new NPC")
    print("2. Roll Dice")
    print("3. Generate Encounter")
    print("4. Log Magic Items")
    print("5. Generate Gold")
    print("6. Exit")
    
    choice = input("Please select an option: ")
    print("==========================")
    
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
            print("==========================")
            save_to_file(f"Result of rolling {dice_roll} for {purpose}: {result}", "DM_Data/roll_results_logs.txt")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == '3':
        num_enemies = int(input("Enter number of enemies in the encounter: "))
        apl = int(input("Enter average party level (APL): "))
        encounter_name = input("Enter name for the encounter: ")
        generate_encounter(num_enemies, apl, encounter_name)
    elif choice == '4':
        player = input("Enter player's name: ")
        item_name = input("Enter magic item name: ")
        item_description = input("Enter magic item description: ")
        log_magic_items(player, item_name, item_description)
    elif choice == '5':
        level = int(input("Enter character level (1-20): "))
        type_of_gold = input("Enter type of gold ('low_level', 'mid_level', 'high_level'): ")
        try:
            gold = generate_gold(level, type_of_gold)
            print(f"Generated gold for level {level} ({type_of_gold}): {gold}")
            save_to_file(f"Generated gold for level {level} ({type_of_gold}): {gold}", "DM_Data/gold_generation_logs.txt")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")










