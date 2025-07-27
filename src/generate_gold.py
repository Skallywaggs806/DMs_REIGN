

from src.dnd_data import *
from src.dice_rolling import roll_dice

def generate_gold(level=1, type="low_level"):
    """
    Generates gold based on the level and type of encounter.
    """
    if type not in coinage_table:
        raise ValueError("Invalid coinage type. Choose from 'low_level', 'mid_level', or 'high_level'.")

    if level < 1 or level > 20:
        raise ValueError("Level must be between 1 and 20.")

    for range_key, coins in coinage_table[type].items():
        start, end = map(int, range_key.split('-'))
        if start <= level <= end:
            return {coin: roll_dice(dice) for coin, dice in coins.items()}

    return {}