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