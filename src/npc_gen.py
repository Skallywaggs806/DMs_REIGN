import random
import requests

from src.save_to_file import save_to_file, read_from_file
from src.dice_rolling import roll_dice_stats, roll_dice
from src.dnd_data import *
from src.racial_modifiers import check_racial_modifiers

def generate_npc(level=1):
    """
    Generates a random NPC
    and saves the details to a file.
"""
    if level < 1:
        raise ValueError("Level must be at least 1.")
    
    class_type = classes[roll_dice("1d12") - 1]
    race = races[roll_dice("1d9") - 1]
    background = backgrounds[roll_dice("1d12") - 1] 

    npc_name = requests.get(f"https://fantasyname.lukewh.com/?family=t").text
    npc = {
        "Name": npc_name,
        "Class": class_type,
        "Race": race,
        "Level": level,
        "Background": background


        }

    

    stats = roll_dice_stats()
    modifiers = {
        "Strength": (stats["Strength"] - 10) // 2,
        "Dexterity": (stats["Dexterity"] - 10) // 2,
        "Constitution": (stats["Constitution"] - 10) // 2,
        "Intelligence": (stats["Intelligence"] - 10) // 2,
        "Wisdom": (stats["Wisdom"] - 10) // 2,
        "Charisma": (stats["Charisma"] - 10) // 2
    }

    combat_stats = {
        "Hit Points": 0,
        "Armor Class": 10 + modifiers["Dexterity"],
        "Base Attack Bonus": modifiers["Strength"],
        "Base Attack Bonus (Ranged)": modifiers["Dexterity"],
        "Initiative": modifiers["Dexterity"],
        "Speed": 30,
        "Proficiency Bonus": (level - 1) // 4 + 2
    }


    class_dict = requests.get(f"https://www.dnd5eapi.co/api/2014/classes/{class_type.lower()}").json()
    hit_dice = class_dict["hit_die"]
    
    con_modifier = modifiers["Constitution"]
    npc["Hit Die"] = hit_dice
    hit_points = roll_dice(f"{level}d{hit_dice}+{con_modifier * level}")
    combat_stats["Hit Points"] = hit_points

    proficiencies = class_dict.get("proficiencies", [])

    check_racial_modifiers(npc, stats)
    


    for key, value in npc.items():
        save_to_file(f"{key}: {value}", f"DM_Data/NPCs/{npc_name}_npc_data.txt")
    save_to_file("\n\n", f"DM_Data/NPCs/{npc_name}_npc_data.txt") 
    for key, value in combat_stats.items():
        save_to_file(f"{key}: {value}", f"DM_Data/NPCs/{npc_name}_npc_data.txt")
    save_to_file("\n\n", f"DM_Data/NPCs/{npc_name}_npc_data.txt") 
    for stat, value in stats.items():
        save_to_file(f"{stat}: {value}", f"DM_Data/NPCs/{npc_name}_npc_data.txt")
    save_to_file("\n\n", f"DM_Data/NPCs/{npc_name}_npc_data.txt") 
    for mod, value in modifiers.items():
        save_to_file(f"{mod} Modifier: {value}", f"DM_Data/NPCs/{npc_name}_npc_data.txt")
    save_to_file("\n\n", f"DM_Data/NPCs/{npc_name}_npc_data.txt")
    for proficiency in proficiencies:
        save_to_file(f"Proficiency: {proficiency['name']}", f"DM_Data/NPCs/{npc_name}_npc_data.txt")
    print(f"NPC {npc_name} generated and saved to DM_Data/NPCs/{npc_name}_npc_data.txt")
    print(read_from_file(f"DM_Data/NPCs/{npc_name}_npc_data.txt"))
    print("\nNPC generated successfully!\n")

