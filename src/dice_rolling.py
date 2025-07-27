
import random


def roll_dice(dice_roll, purpose=None):
    """
    Rolls a specified number of dice with a given number of sides and applies a modifier.

    :param num_dice: Number of dice to roll
    :param num_sides: Number of sides on each die
    :param modifier: Modifier to apply to the total roll
    :return: Total result after rolling the dice and applying the modifier
    """

    num_dice, num_sides, modifier = parse_dice_roll(dice_roll)
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