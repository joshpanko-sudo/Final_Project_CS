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
        """
        Start the class
        """
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
        """
        Player description
        """
        self.character_description = character_description or "No description yet"
        if print_description:
            print(self.character_description)
        return None
    

    def take_damage(self, amount_of_damage:float, damaged_by:str = "Unknown"):
        """
        Entity take damage
        """
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
        """
        Heal an entity
        """
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
        """
        Start the class
        """
        super().__init__(character_name, character_health, max_character_health)
        self.power = 5


    def inflict_damage(self, target: CharacterManager, used_power: str):
        """
        Give damage to some entity
        """
        figure_out_attacks_(self.name)
        if used_power in power_data_list:
            attack_info = power_data_list[used_power]
            base_strength = attack_info["strength"]
            attack_damage = random.randint(max(0, base_strength - 5), base_strength + 5)
            print(f"{self.name} {attack_info['power']} | Damage dealt: {attack_damage}")
            time.sleep(1.5)
            target.take_damage(attack_damage, damaged_by=self.name)
        else:
            print(f"Warning: {self.name} does not know how to use {used_power}")


class Enemy(CharacterManager):
    def __init__(self, character_name: str, character_health: float, max_character_health: float = 100) -> None:
        super().__init__(character_name, character_health, max_character_health)
        self.power = 2


    def inflict_damage(self, target: CharacterManager, used_power: str):
        """
        Damage once again
        """
        figure_out_attacks_(self.name)
        if used_power in power_data_list:
            attack_info = power_data_list[used_power]
            base_strength = attack_info["strength"]
            attack_damage = random.randint(max(0, base_strength - 5), base_strength + 2)
            print(f"{self.name} {attack_info["power"]} | Damage dealt: {attack_damage}")
            time.sleep(1.5)
            target.take_damage(attack_damage, damaged_by=self.name)
        else:
            print(f"Warning: {self.name} does not know how to use {used_power}")


class CharacterBattle():
    def __init__(self, p1: Player, e1: Enemy) -> None:
        self.p1 = p1
        self.e1 = e1


    def display_battle_status(self):
        """
        Displays battle things
        """
        status_data = [
            ["NAME", self.p1.name, self.e1.name],
            ["HEALTH", f"{self.p1.health} / {self.p1.max_health}",f"{self.e1.health}/{self.e1.max_health}"],
            ["SHIELD (TEMP HP)", self.p1.temporary_max_health, self.e1.temporary_max_health],
            ["STATUS", "Alive" if self.p1.alive else "Defeated", "Alive" if self.e1.alive else "Defeated"],
            ["INFO", self.p1.character_description, self.e1.character_description],
        ]
        print("\n" + tabulate(status_data, headers=["STAT", "PLAYER", "ENEMY"], tablefmt="fancy_grid") + "\n")


    def _local_continue(self):
        """
        Preveents circular importing
        """
        questionary.select("Press enter to continue...", choices=["Continue"]).ask()
        return


    def gameloopCharacterBattle(self):
        """
        Another gameloop. Please stop making me write all of the PEP8
        """
        time.sleep(1)
        while self.p1.alive and self.e1.alive:
            print("\033[2J\033[H")
            self.display_battle_status()
            figure_out_attacks_(self.p1.name)
            while True:
                choices = list(power_data_list.keys()) + ["Check Stats"]
                action = questionary.select(
                    f"Pick action for {self.p1.name}:",
                    choices=choices
                ).ask()
                if action == "Check Stats":
                    self.display_battle_status()
                    self._local_continue()
                else:
                    self.p1.inflict_damage(self.e1, action)
                    break
            if not self.e1.alive:
                    break
            print(f"{self.e1.name}'s turn")
            time.sleep(1)
            figure_out_attacks_(self.e1.name)
            enemy_choices = list(power_data_list.keys())
            if enemy_choices:
                enemy_action = random.choice(enemy_choices)
                self.e1.inflict_damage(self.p1, enemy_action)
            else:
                print(f"Warning: CharacterBattle could not fetch moves for {self.e1.name}")
            time.sleep(1)

        print("Battle has ended.")
        if self.p1.alive:
            print(f"{self.p1.name} has won the battle")
        else:
            print(f"{self.p1.name} has lost the battle to {self.e1.name}")


# if __name__ == "__main__":
#     # Setup Entities
#     hero = Player("Player", character_health=100)
#     hero.description("The legendary chosen warrior.")
    
#     villain = Enemy("Spider Droid", character_health=80)
#     villain.description("An engineered mechanical nightmare.")

#     # Match Start
#     battle = CharacterBattle(hero, villain)
#     battle.gameloopCharacterBattle()



