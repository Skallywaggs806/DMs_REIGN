from src.save_to_file import save_to_file, read_from_file


def log_magic_items(player, item_name, item_description):
    """
    Logs a magic item for a player.
    
    :param player: The name of the player.
    :param item_name: The name of the magic item.
    :param item_description: A description of the magic item.
    """
    filename = f"DM_Data/Players/{player}_magic_items.txt"
    
    save_to_file(f"Item Name: {item_name}", filename)
    save_to_file(f"Description: {item_description}", filename)
    save_to_file("==============================", filename)
    
    print(f"Magic item '{item_name}' logged for player '{player}'.")
    print("Current magic items:")
    print(read_from_file(filename))
    