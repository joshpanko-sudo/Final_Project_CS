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

try:
    import random
except ImportError as e:
    print(f"Warning: Characteranager could not load random. {e}. Perhaps you have not installed it?")
    quit()

try:
    from character_attacks_database import figure_out_attacks_
    from character_attacks_database import power_data_list
except ImportError as e:
    print(f"Warning: CharacterManager could not load character_attacks_database.py. {e}. Perhaps you have not installed it?")
    quit()



class CharacterManager():
    def __init__(self, character_name:str, character_health:float, max_character_health:float = 100) -> None:
        self.name = character_name
        self.health = character_health
        self.max_health = max_character_health
        self.temporary_max_health = 0
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
            ["Health", f"{self.health + self.temporary_max_health:,}"],
            ["Status", "Alive" if self.alive else "Dead"],
            ["Description", self.character_description]
        ]
        print(tabulate(status_data, stralign="center", tablefmt="fancy_grid"))


    def take_damage(self, amount_of_damage:float, damaged_by:str = "Unknown"):
        if self.temporary_max_health > 0:
            if amount_of_damage <= self.temporary_max_health:
                self.temporary_max_health -= amount_of_damage
                amount_of_damage = 0
            else:
                amount_of_damage -= self.temporary_max_health
                self.temporary_max_health = 0
        if amount_of_damage > 0:
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
        # Add code in the case if an item is a revive item, the character can come back to life.
        if not self.alive:
            print(f"{self.name} is no longer alive and cannot be healed.")
            return
        total_health = self.health + healing_amount
        if total_health > self.max_health:
            overflow = total_health - self.max_health
            self.temporary_max_health += overflow
            self.health = self.max_health
        else:
            self.health = total_health


class Player(CharacterManager):
    def __init__(self, character_name: str, character_health: float, max_character_health: float = 100) -> None:
        super().__init__(character_name, character_health, max_character_health)
        self.power = 2
        

    def inflict_damage(self, target: CharacterManager, used_power:str):
        figure_out_attacks_(self.name) # Load character attacks
        if used_power in power_data_list:
            attack_info = power_data_list[used_power]
            base_strength = attack_info["strength"]
            # Damage variance logic
            attack_damage = random.randint(max(0, base_strength - 5), base_strength + 5)
            
            print(f"{self.name} {attack_info['power']} | Damage dealt: {attack_damage}")
            time.sleep(1)
            target.take_damage(attack_damage, damaged_by=self.name)
        else:
            print(f"{self.name} does not know how to use {used_power}!")

class Enemy(CharacterManager):
    def __init__(self, character_name: str, character_health: float, max_character_health: float = 100) -> None:
        super().__init__(character_name, character_health, max_character_health)

    def inflict_damage(self, target: CharacterManager, used_power: str):
        # Step A: Load this enemy's specific attacks
        figure_out_attacks_(self.name)
        
        if used_power in power_data_list:
            attack_info = power_data_list[used_power]
            base_strength = attack_info["strength"]
            
            # Enemy damage variance logic
            attack_damage = random.randint(max(0, base_strength - 5), base_strength + 2)
            
            print(f"{self.name} {attack_info['power']} | Damage dealt: {attack_damage}")
            time.sleep(1)
            target.take_damage(attack_damage, damaged_by=self.name)
        else:
            print(f"{self.name} does not know how to use {used_power}!")


def start_battle(player_character: Player, enemy_character: Enemy):
    print(f"⚔️ BATTLE START: {player_character.name} vs {enemy_character.name} ⚔️\n")
    time.sleep(1)
    
    while player_character.alive and enemy_character.alive:
        # --- PLAYER TURN ---
        print(f"\n--- {player_character.name}'s Turn ---")
        # Load attacks so we can print options for the user
        figure_out_attacks_(player_character.name)
        
        print("Available Attacks:")
        for move in power_data_list.keys():
            print(f"- {move}")
            
        choice = input("Choose your attack: ").strip()
        player_character.inflict_damage(enemy_character, choice)
        
        # Check if enemy died from the attack
        if not enemy_character.alive:
            break
            
        # --- ENEMY TURN ---
        print(f"\n--- {enemy_character.name}'s Turn ---")
        # Load enemy attacks to select one randomly
        figure_out_attacks_(enemy_character.name)
        enemy_moves = list(power_data_list.keys())
        
        if enemy_moves:
            enemy_choice = random.choice(enemy_moves)
            enemy_character.inflict_damage(player_character, enemy_choice)
        else:
            print(f"{enemy_character.name} has no attacks available!")
            
        time.sleep(1)

    # --- BATTLE OVER RESULT ---
    print("\n--- Battle Ended ---")
    if player_character.alive:
        print(f"🎉 Victory! {player_character.name} won the battle!")
    else:
        print(f"💀 Game Over! {enemy_character.name} defeated you.")


hero = Player("Player", character_health=100)
villain = Enemy("Spider Droid", character_health=80)

# 2. Run the battle loop!
start_battle(hero, villain)