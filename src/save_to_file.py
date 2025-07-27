import os

def save_to_file(data, filename):
    """
    Saves the given data to a file with the specified filename.
    
    Parameters:
    data (str): The data to be saved.
    filename (str): The name of the file where data will be saved.
    
    Returns:
    None
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'a') as file:
        file.write(data)
        file.write('\n')

def read_from_file(filename):
    """
    Reads data from a file with the specified filename.
    
    Parameters:
    filename (str): The name of the file to read data from.
    
    Returns:
    str: The content of the file.
    """
    if not os.path.exists(filename):
        return ""

    with open(filename, 'r') as file:
        return file.read()

