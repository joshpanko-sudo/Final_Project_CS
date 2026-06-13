"""
Legend:
- Name: CharacterManager

Highlight Codes:
- Red: Error
- Green: Working
- Blue: Action being done

Error template:
- Warning: CharacterManager could not {Error Here}. {e}. Please {Possible Solution Here}
"""

try:
    from tabulate import tabulate
except ImportError as e:
    print(f"Warning: CharacterManager could not load tabulate. {e}. Perhaps you have not installed it?")
    quit()

try:
    import questionary
except ImportError as e:
    print(f"Warning: CharacterManager could not load questionary. {e}. Please run 'pip install questionary'.")
    quit()

try:
    import time
except ImportError as e:
    print(f"Warning: CharacterManager could not load time. {e}. Perhaps you have not installed it?")
    quit()

try:
    import random
except ImportError as e:
    print(f"Warning: CharacterManager could not load random. {e}. Perhaps you have not installed it?")
    quit()

try:
    from character_attacks_database import figure_out_attacks_
    from character_attacks_database import power_data_list
except ImportError as e:
    print(f"Warning: CharacterManager could not load character_attacks_database.py. {e}. Perhaps you have not installed it?")
    quit()

class CharacterManager:
    # Defaults the max character health to 100
    def __init__(self, character_name: str, character_health: float, max_character_health: float = 100) -> None:
        self.name = character_name # The name of the character
        self.health = character_health # Current character health (Does not have to be max)
        self.max_health = max_character_health # Value cannot change, maximum health a character can have
        self.temporary_max_health = 0 # Allows the character health to go above the max
        self.alive = True # Character is alive and not defeated
        self.character_description = "" # Info about character

    def __str__(self):
        return f"Character: {self.name}"
    
    def description(self, character_description: str, print_description: bool = False):
        self.character_description = character_description or "No description yet"
        if print_description:
            print(self.character_description)
        return None
