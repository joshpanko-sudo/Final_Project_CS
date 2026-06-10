'''
Legend:
- Name: CharacterManager

Highlight Codes:
- Red: Error
- Green: Working
- Blue: Action being done

Error template:
- Warning: CharacterManager could not {Error Here}. {e}. Please {Possible Solution Here}

'''

try:
    from tabulate import tabulate
except ImportError as e:
    print(f"Warning: CharacterManager could not load tabulate. {e}. Perhaps you have not installed it?")
    quit()

try:
    import time
except ImportError as e:
    print(f"Warning: Characteranager could not load time. {e}. Perhaps you have not installed it?")
    quit()



class CharacterManager():
    def __init__(self, character_name:str, character_health:float) -> None:
        self.name = character_name
        self.health = character_health
        self.alive = True
        self.character_description = ""

    def __str__(self):
        return f"Character: {self.name}"
    
    def description(self, character_description:str, print_description:bool = False):
        self.character_description = character_description or "No description yet"
        if print_description:
            print(self.character_description)
        return None
    
    def character_status(self):
        status_data = [
            ["Name", self.name],
            ["Health", f"{self.health:,}"],
            ["Status", "Alive" if self.alive else "Dead"],
            ["Description", self.character_description]
        ]
        print(tabulate(status_data, stralign="center", tablefmt="fancy_grid"))


    def take_damage(self, amount_of_damage:float, damaged_by:str = "Unknown"):
        self.health -= amount_of_damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"{self.name} was defeated.") if damaged_by == "Unknown" else print(f"{self.name} was defeated by {damaged_by}.")
            time.sleep(1)
        else:
            print(f"{self.name} took damaged. Current health: {self.health}") if damaged_by == "Unknown" else print(f"{self.name} took damage from {damaged_by}. Current health: {self.health}")
            time.sleep(1) 

    def heal(self, healing_amount:float, healing_item:str = "Unknown"):
        if not self.alive:
            print(f"{self.name} is no longer alive and cannot be healed.")



Josh = CharacterManager("Josh", 10000000000)
Josh.description("I am very good at coding", True)
# Josh.character_status()


