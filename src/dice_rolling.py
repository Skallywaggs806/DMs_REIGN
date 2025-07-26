
import random


def roll_dice(num_dice, num_sides, modifier, purpose=""):
    """
    Rolls a specified number of dice with a given number of sides and applies a modifier.

    :param num_dice: Number of dice to roll
    :param num_sides: Number of sides on each die
    :param modifier: Modifier to apply to the total roll
    :return: Total result after rolling the dice and applying the modifier
    """
    if num_dice < 0:
        raise ValueError("Number of dice cannot be negative.")
    if num_sides <= 0:
        raise ValueError("Number of sides must be a positive integer.")
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total = sum(rolls) + modifier
    return total

def roll_dice_stats():
    """
    Rolls 4d6 and returns the sum of the highest three rolls.
    
    :return: Total of the highest three rolls from four six-sided dice
    """


    stats = {
        "Strength": None,
        "Dexterity": None,
        "Constitution": None,
        "Intelligence": None,
        "Wisdom": None,
        "Charisma": None}
    
    for key in stats.keys():
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort(reverse=True)
        stats[key] = sum(rolls[:3])
        rolls = rolls[3:]
        
    
    return stats