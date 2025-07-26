
from src.dnd_data import *


def check_racial_modifiers(npc, stats):
    """
    Checks and applies racial modifiers to the NPC's stats. 
    """
    if npc["Race"] == "Human":
        # Humans get +1 to all stats
        for key in stats.keys():
            stats[key] += 1
    elif npc["Race"] == "Dwarf":
        # Dwarves get +2 Constitution, +1 Wisdom
        stats["Constitution"] += 2
        stats["Wisdom"] += 1    
    elif npc["Race"] == "Elf":
        # Elves get +2 Dexterity, +1 Intelligence
        stats["Dexterity"] += 2
        stats["Intelligence"] += 1 
    elif npc["Race"] == "Gnome":
        # Gnomes get +2 Intelligence, +1 Dexterity
        stats["Intelligence"] += 2
        stats["Dexterity"] += 1
    elif npc["Race"] == "Halfling":
        # Halflings get +2 Dexterity, +1 Charisma
        stats["Dexterity"] += 2
        stats["Charisma"] += 1
    elif npc["Race"] == "Half-Elf":
        # Half-Elves get +2 Charisma, +1 to two other stats of choice
        stats["Charisma"] += 2
        # Assuming player chooses Strength and Intelligence for example
        stats["Strength"] += 1
        stats["Intelligence"] += 1
    elif npc["Race"] == "Half-Orc":
        # Half-Orcs get +2 Strength, +1 Constitution
        stats["Strength"] += 2
        stats["Constitution"] += 1
    elif npc["Race"] == "Dragonborn":
        # Dragonborn get +2 Strength, +1 Charisma
        stats["Strength"] += 2
        stats["Charisma"] += 1
    elif npc["Race"] == "Tiefling":
        # Tieflings get +2 Charisma, +1 Intelligence
        stats["Charisma"] += 2
        stats["Intelligence"] += 1