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
        '''
        Retuns the character's name
        '''
        return f"Character: {self.name}"
    

    def description(self, character_description: str, print_description: bool = False):
        self.character_description = character_description or "No description yet"
        if print_description:
            print(self.character_description)
        return None
    

    def take_damage(self, amount_of_damage:float, damaged_by:str = "Unknown"):
        # Take health away from temporary if that exists
        if self.temporary_max_health > 0:
            if amount_of_damage <= self.temporary_max_health:
                self.temporary_max_health -= amount_of_damage
                amount_of_damage = 0
            else:
                # Damage is larger than temporary health, take away all temp and subtract that from damage
                amount_of_damage -= self.temporary_max_health
                self.temporary_max_health = 0
        if self.health > 0:
            self.health -= amount_of_damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"{self.name} was defeated") if damaged_by == "Unknown" else print(f"{self.name} was defeated by {damaged_by}.")
            time.sleep(1)
        else:
            print(f"{self.name} took damage. Current health {self.health}") if damaged_by == "Unknown" else print(f"{self.name} took damage from {damaged_by}. Current health: {self.health}")
            time.sleep(1)

    def heal(self, healing_amount:float, healing_item: str = "Unknown"):
        if not self.alive:
            print(f"{self.name} is no longer alive and cannot be healed.")
            return
        total_health = self.health + healing_amount
        if total_health > self.max_health:
            overflow_health = total_health - self.max_health
            self.temporary_max_health += overflow_health
            self.health = self.max_health
        else:
            self.health = total_health

class Player(CharacterManager):
    def __init__(self, character_name: str, character_health: float, max_character_health: float = 100) -> None:
        super().__init__(character_name, character_health, max_character_health)
        self.power = 2

    def inflict_damage(self, target: CharacterManager, used_power: str):
        figure_out_attacks_(self.name)
        if used_power in power_data_list:
            attack_info = power_data_list[used_power]
            base_strength = attack_info["strength"]
            attack_damage = random.randint(max(0, base_strength - 5), base_strength + 5)
            print(f"{self.name} {attack_info["power"]} | Damage dealt: {attack_damage}")
