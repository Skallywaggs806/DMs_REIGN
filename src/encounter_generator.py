
from src.dnd_data import *
from src.save_to_file import save_to_file, read_from_file
from src.dice_rolling import roll_dice_stats, roll_dice

def generate_encounter(num_enemies=1, apl=1, encounter_name="Random Encounter"):

    for i in range (num_enemies):
        monster = monsters[roll_dice(1, len(monsters), 0) - 1]
        monster["Hit Points"] = calculate_total_hit_points(monster["hit_dice"], apl)
        for key, value in monster.items():
            save_to_file(f"{key}: {value}", f"DM_Data/Encounters/{encounter_name}.txt")
        save_to_file("\n", f"DM_Data/Encounters/{encounter_name}.txt")
    print(f"Encounter '{encounter_name}' generated with {num_enemies} enemies.")
    print("\nEncounter details:\n")
    print(read_from_file(f"DM_Data/Encounters/{encounter_name}.txt"))

def calculate_total_hit_points(hit_die, apl):
    """
    Calculate total hit points based on hit die and average party level (APL).
    
    :param hit_die: Hit die in the format 'XdY' where X is the number of dice and Y is the number of sides
    :param apl: Average party level
    :return: Total hit points for the monster
    """
    num_dice, sides, modifier = parse_dice_roll(hit_die)
    hit_points = 0
    for i in range(apl):
        hit_points += roll_dice(num_dice, sides, modifier)
    return hit_points





def parse_dice_roll(dice_string):
    # Initialize variables
    num_dice = 0
    sides = 0
    modifier = 0
    
    # Split on 'd' to separate number of dice and the rest
    parts = dice_string.split('d')
    num_dice = int(parts[0])  # First part is number of dice
    
    # Check for modifier in the second part
    if '+' in parts[1]:
        dice_and_modifier = parts[1].split('+')
        sides = int(dice_and_modifier[0])  # Part before '+' is sides
        modifier = int(dice_and_modifier[1])  # Part after '+' is modifier
    elif '-' in parts[1]:
        dice_and_modifier = parts[1].split('-')
        sides = int(dice_and_modifier[0])  # Part before '-' is sides
        modifier = -int(dice_and_modifier[1])  # Part after '-' is negative modifier
    else:
        sides = int(parts[1])  # No modifier, just sides
    
    return num_dice, sides, modifier
