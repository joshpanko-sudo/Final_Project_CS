# -----------------------------------------------------------------------------
# Created By: Allen Feng
# Created Date: 05/20/2026
# Version 2.6 (Fully working)
# -----------------------------------------------------------------------------
"""
Map system.
"""
# -----------------------------------------------------------------------------
'''
Legend:
- Name: MapManager

Highlight Codes:
- Red: Error
- Green: Working
- Blue: Action being done

Error template:
- Warning: MapManager could not {Error Here}. {e}. Please 
Possible Solution Here}


'''
# Imports & Global Variables --------------------------------------------------
try:
    from tabulate import tabulate
except ImportError as e:
    print(
        f"Warning: MapManager could not load tabulate. {e}. "
        "Perhaps you have not installed it?")
    quit()

try:
    import questionary
except ImportError as e:
    print(
        f"Warning: MapManager could not load questionary. {e}. "
        "Perhaps you have not installed it?")
    quit()

try:
    import time
except ImportError as e:
    print(
        f"Warning: MapManager could not load time. {e}. "
        "Make sure time is loaded.")
    quit()

try:
    import game_maps
except ImportError as e:
    print(
        f"Warning: MapManager could not load game_maps.py. {e}. "
        "Make sure game_maps.py is within the same directory.")
    quit()

try:
    from dialogue_manager import character_say
    SP = character_say("")
except ImportError as e:
    print(
        f"Warning: MapManager could not load DialogueManager. {e}. "
        "Make sure dialogue_manager.py is within the same directory.")
    quit()

try:
    from item_manager import ItemManager
    IM = ItemManager("Player Inventory")
    IM.set_capacity(5)
except ImportError as e:
    print(
        f"Warning: MapManager could not load DialogueManager. {e}. "
        "Make sure dialogue_manager.py is within the same directory.")
    quit()


class MapManager():
    '''
    Main class
    '''
    def __init__(self) -> None:
        '''
        Initilize the class
        '''
        self.player_location = {"row": 0, "col": 0}
        self.default_main_player_location = {"row": 0, "col": 0}
        self.loaded_map_data = None
        self.active_map = None
        self.longest_map_name = None
        # map_data is going to be the input dict for the map stuff You will see


    def load_map(self, map_data, default_player: bool = False):
        '''
        Load a map form maps.py
        '''
        self.loaded_map_data = map_data
        self.active_map = map_data["maps"]
        if default_player:
            self.player_location = map_data["default_player_location"]
        self.tutorial_data = map_data["tutorial"] if map_data.get(
            "tutorial") is not None else False
        self.actual_tutorial = map_data["actual_tutorial"] if map_data.get(
            "actual_tutorial") is not None else False
        if self.actual_tutorial:
            SP.say(self.actual_tutorial)
            self.continue_game()
        self.find_longest_map_name()
        # print(self.loaded_map_data)
        # print(tabulate(self.active_map, tablefmt="fancy_grid", stralign="center", disable_numparse=True))


    def find_longest_map_name(self):
        '''
        Finds the longest string name within the active map in order to make 
        columns equal sized
        '''
        self.longest_map_name = (len(max(
            (column for row in self.active_map for column in row if 
             column is not None), 
            key=len, default="")))
        # print(self.longest_map_name)
        return self.longest_map_name


    def format_map(self, rows, columns):
        '''
        Applies the player location highlight and the white square for non 
        accessible tiles
        '''
        # Return the state of the tile (None, player is on, or location)
        check_tile = self.active_map[rows][columns]
        # Check if player is occupying tile
        player_highlight = (
            rows == self.player_location["row"] and columns == (
                self.player_location["col"]))
        if check_tile is None:  # Empty tile, no location on it
            return "█" * self.longest_map_name  # White square blocked off
        enemy_dict = self.loaded_map_data.get("enemies", {})
        if (rows, columns) in enemy_dict and not player_highlight:
            return f"\033[91m[{check_tile[0]}!]\033[0m"
        item_dict = self.loaded_map_data.get("items", {})
        if (rows, columns) in item_dict and not player_highlight:
            return f"\033[94m[{check_tile[0]}?]\033[0m"
        if player_highlight:  
        # If is_player is true, highlight the tile and add brackets 
        # to represent player is there
            # player_tile = f"[{check_tile}]" #Puts brackets around player
            # occupied tile
            # Invert the tile to represent player
            player_tile = f"\033[7m{check_tile}\033[0m"
        else:

            # Player is not on tile, no modifications
            player_tile = f"{check_tile}"
        return f"{player_tile}"  # Return tiles


    def update_map(self):
        '''
        Updates the map after modifications or the player moving
        '''
        cooridnate_map = []
        for rows in range(
                len(self.active_map)):  
            # Loop through tows of the input map
            cooridnate_map.append([self.format_map(rows, columns) for 
                                   columns in range(
                len(self.active_map[0]))])  
            # Loop through columns of input map
        print("\033[2J\033[H")
        print("\n" + "=" * 30)
        print(
            tabulate(
                cooridnate_map,
                tablefmt="fancy_grid",
                stralign="center",
                disable_numparse=True))  # Print out the map


    def teleport_player(self, teleport_data):
        '''
        Global funciton to teleport player
        '''
        self.player_location["row"] = teleport_data["end_coord"][0]
        self.player_location["col"] = teleport_data["end_coord"][1]
        self.load_map(teleport_data["target_map"](), False)
        return


    def check_teleport(self, row, col):
        '''
        _ is called teleport_name if needed in future
        '''
        for _, teleport_data in self.loaded_map_data.get(
                "teleport", {}).items():
            if row == teleport_data["start_coord"][0] and col == (
                teleport_data["start_coord"][1]):
                self.teleport_player(teleport_data)
                return True
        return False


    def enter_check_teleport(self):
        """
        Teleport if you press enter then enter
        """
        for _, teleport_data in self.loaded_map_data.get(
                "enter_teleport", {}).items():
            if self.player_location["row"] == teleport_data["start_coord"][
                    0] and self.player_location["col"] == (
                        teleport_data["start_coord"][1]):
                move = questionary.select(
                    f'Enter {
                        self.loaded_map_data["location_name"]}',
                    choices=[
                        "Yes",
                        "No"]).ask()
                match move:
                    case "Yes":
                        self.teleport_player(teleport_data)
                        return
                    case "No":
                        return
                    case _:
                        print(
                            "Warning: MapManager cannot enter "
                            "location. Fatal error")
                        quit()
                return True
        return False


    def ladder_check_teleport(self):
        '''
        Go up or down with teleport
        '''
        ladders = self.loaded_map_data.get("ladder_teleport", {})
        choices = [name for name, data in ladders.items()
                   if self.player_location["row"] == (
                       data["start_coord"][0]) 
                       and self.player_location["col"] == (
                           data["start_coord"][1])]
        if not choices:
            return False
        move = questionary.select(
            f'Go {
                self.loaded_map_data["location_name"]}',
            choices=["Stay"] +
            choices).ask()
        if move != "Stay" and move is not None:
            teleport_data = ladders[move]
            self.teleport_player(teleport_data)
            return True

        return False


    def battle_check(self):
        """
        Check if there is a battle trigger and triggers the battle
        """
        enemy_dict = self.loaded_map_data.get("enemies", {})
        current_player_location = (
            self.player_location["row"],
            self.player_location["col"])

        if current_player_location in enemy_dict:
            enemy_info = enemy_dict[current_player_location]
            print(f"An enemy has been detected. {enemy_info['name']}")
            time.sleep(1)
            try:
                from character_managerV2 import Player, Enemy, CharacterBattle
                player = Player("Player", character_health=150)
                player.description("A scientist who has been warped")
                enemy = Enemy(
                    character_name=enemy_info["name"],
                    character_health=enemy_info["health"],
                    max_character_health=enemy_info.get("max_health", 100)
                )
                enemy.description(
                    enemy_info.get(
                        "description",
                        "Hostile robot"))
                battle = CharacterBattle(player, enemy)
                battle.gameloopCharacterBattle()
                if not enemy.alive:
                    print(f"{enemy_info['name']} has been cleared")
                    del enemy_dict[current_player_location]
                    if not enemy_dict:
                        print(
                            "\033[92m[Map Cleared!]\033[0m All enemies have "
                            "been defeated!")
                        time.sleep(1.5)
                        return "CLEARED"
                    self.continue_game()
                else:
                    print(f"\033[91m[Error] You were defeated.\033[0m")
                    quit()
                return True
            except ImportError as e:
                print(
                    f"Warning: MapManager could not initiate battle. {e}. "
                    "Please ensure character_managerV2 file exists.")
                quit()
        else:
            print("There are no enemies here to fight.")
            time.sleep(1)
        return False


    def item_check(self):
        """
        Allows player to pick up items
        """
        item_dict = self.loaded_map_data.get("items", {})
        current_player_location = (
            self.player_location["row"],
            self.player_location["col"])
        if current_player_location in item_dict:
            item_info = item_dict[current_player_location]
            print(
                f"\033[94m[Action] You found something on the ground: {
                    item_info['name']}!\033[0m")
            time.sleep(1)
            try:
                IM.add_item(
                    item_name=item_info["name"],
                    item_amount=item_info["amount"],
                    max_stack=item_info["max_stack"]
                )
                del item_dict[current_player_location]
                if item_info.get("exit_on_pickup", False):
                    print(
                        f"\033[92m[Working] Objective complete! Leaving "
                        "location...\033[0m")
                    time.sleep(1.5)
                    return "EXIT_KEY_FOUND"
                self.continue_game()
                return True
            except Exception as e:
                print(
                    f"\033[91mWarning: MapManager could not add item. {e}. "
                    "Please ensure inventory system is installed.\033[0m")
                quit()
        return False


    def continue_game(self):
        """
        Stops program from continuing without user input
        """
        game_continue = questionary.select("Continue?", choices=["Yes"]).ask()
        match game_continue:
            case "Yes":
                return
            case _:
                print("Warning: MapManager cannot continue game. Fatal Error")
                quit()


    def move_player(self, command):  # Move the player
        '''
        Function to make player move
        '''
        rows, cols = self.player_location["row"], self.player_location["col"]
        new_row, new_col = rows, cols
        match command:
            case "w":
                new_row -= 1
            case "a":
                new_col -= 1
            case "s":
                new_row += 1
            case "d":
                new_col += 1
            case "e":
                self.enter_check_teleport()
            case "f":
                self.ladder_check_teleport()
            case "q":
                status = self.battle_check()
                if status == "CLEARED":
                    return "CLEARED"
            case "r":
                IM.see_inventory()
                self.continue_game()

                return
            case "?":
                if self.tutorial_data:
                    SP(self.tutorial_data)
                    self.continue_game()
                return
            case _:
                print("Warning: MapManager cannot move player. Fatal Error")
                quit()
        if self.check_teleport(new_row, new_col):
            return
        if 0 <= new_row < len(
                self.active_map) and 0 <= new_col < len(
                self.active_map[0]):
            if self.active_map[new_row][new_col] is not None:
                self.player_location["row"] = new_row
                self.player_location["col"] = new_col
                return self.item_check()


    def gameloopMapManager(self):
        '''
        Update map, do things... etc
        '''
        self.update_map()
        print(self.player_location)
        print(
            "Current location:"
              f"{self.active_map[self.player_location['row']]
                 [self.player_location['col']]}")
        enemy_dict = self.loaded_map_data.get("enemies", None)
        if enemy_dict is not None and not enemy_dict:
            print("\033[92m[Map Cleared!]\033[0m All enemies "
                  "have been cleared.")
            return False
        while (command := input("W, A, S, D, E, F, Q, R, "
                                "?: ").strip().lower()) not in {
                "w", "a", "s", "d", "e", "f", "?", "q", "r"}:
            print("Wrong Move")
        else:
            result = self.move_player(command)
            if result == "CLEARED":
                return False
            return True


# mm = MapManager()
# mm.load_map(game_maps.battle_1, True)
# mm.update_map()

# # # print(list(maps.minimap_3["ladder_teleport"].keys())[0])
# while True:
#     map_active = mm.gameloopMapManager()
#     if not map_active:
#         print("\033[94m[Action] Transitioning out of cleared map...\033[0m")
#         break
