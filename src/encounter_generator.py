
from src.dnd_data import *
from src.save_to_file import save_to_file, read_from_file
from src.dice_rolling import roll_dice_stats, roll_dice

def generate_encounter(num_enemies=1, apl=1, encounter_name="Random Encounter"):
    save_to_file(f"Encounter Name: {encounter_name}", f"DM_Data/Encounters/{encounter_name}.txt")
    save_to_file(f"Average Party Level (APL): {apl}", f"DM_Data/Encounters/{encounter_name}.txt")
    save_to_file(f"Number of Enemies: {num_enemies}", f"DM_Data/Encounters/{encounter_name}.txt")
    save_to_file("===============================", f"DM_Data/Encounters/{encounter_name}.txt")

    for i in range (num_enemies):
        monster = monsters[roll_dice("1d8") - 1]
        monster["Hit Points"] = calculate_total_hit_points(monster["hit_dice"], apl)
        for key, value in monster.items():
            if isinstance(value, list):
                for item in value:
                    save_to_file("\n", f"DM_Data/Encounters/{encounter_name}.txt")
                    for key_item, value_item in item.items():
                        save_to_file(f"{key_item}: {value_item}", f"DM_Data/Encounters/{encounter_name}.txt")
                    save_to_file("\n", f"DM_Data/Encounters/{encounter_name}.txt")
            else:
                save_to_file(f"{key}: {value}", f"DM_Data/Encounters/{encounter_name}.txt")
        save_to_file("===============================", f"DM_Data/Encounters/{encounter_name}.txt")
      
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
    
    hit_points = 0
    for i in range(apl):
        hit_points += roll_dice(hit_die)
    return hit_points






