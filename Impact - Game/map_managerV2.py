'''
Legend:
- Name: MapManager

Highlight Codes:
- Red: Error
- Green: Working
- Blue: Action being done

Error template:
- Warning: MapManager could not {Error Here}. {e}. Please {Possible Solution Here}


'''

try:
    from tabulate import tabulate
except ImportError as e:
    print(f"Warning: MapManager could not load tabulate. {e}. Perhaps you have not installed it?")
    quit()

try:
    import maps
except ImportError as e:
    print(f"Warning: MapManager could not load maps.py. {e}. Make sure maps.py is within the same directory.")
    quit()

class MapManager():
    def __init__(self) -> None:
        '''
        Initilize the class
        '''
        self.player_location = {"row": 0, "col": 0}
        self.default_main_player_location = {"row": 0, "col": 0}
        self.loaded_map_data = None
        self.active_map = None
        self.longest_map_name = None
    #map_data is going to be the input dict for the map stuff You will see

    def load_map(self, map_data):
        '''
        Load a map form maps.py
        '''
        self.loaded_map_data = map_data
        self.active_map = map_data["maps"]
        self.find_longest_map_name()
        # print(self.loaded_map_data)
        # print(tabulate(self.active_map, tablefmt="fancy_grid", stralign="center", disable_numparse=True))

    def find_longest_map_name(self):
        '''
        Finds the longest string name within the active map in order to make colums equal sized
        '''
        self.longest_map_name = (len(max((column for row in self.active_map for column in row if column is not None),key=len,default="")))
        # print(self.longest_map_name)
        return self.longest_map_name
       

    def format_map(self, rows, columns):
        '''
        Applies the player location highlight and the white square for non accessible tiles
        '''

        check_tile = self.active_map[rows][columns] # Return the state of the tile (None, player is on, or location)
        
        player_highlight = (rows == self.player_location["row"] and columns == self.player_location["col"]) #Check if player is occupying tile
        
        if check_tile is None: # Empty tile, no location on it
            return "█" * self.longest_map_name # White square blocked off
        if player_highlight: #If is_player is true, highlight the tile and add brackets to represent player is there
        # player_tile = f"[{check_tile}]" #Puts brackets around player occupied tile
            player_tile = f"\033[7m{check_tile}\033[0m" # Invert the tile to represent player
        else:
            
            player_tile = f"{check_tile}" #Player is not on tile, no modifications
        return f"{player_tile}" # Return tiles
    

    def update_map(self):
        '''
        Updates the map after modifications or the player moving
        '''
        cooridnate_map = []
        for rows in range(len(self.active_map)): #Loop through tows of the input map
            cooridnate_map.append([self.format_map(rows, columns) for columns in range(len(self.active_map[0]))]) #Loop through columns of input map
        print("\033[2J\033[H")
        print("\n" + "=" * 30)
        print(tabulate(cooridnate_map, tablefmt="fancy_grid", stralign="center", disable_numparse=True)) # Print out the map


    def check_teleport(self, row, col):
        '''
        _ is called teleport_name if needed in future
        '''
        for _, teleport_data in self.loaded_map_data.get("teleport", {}).items():
            if row == teleport_data["start_coord"][0] and col == teleport_data["start_coord"][1]:
                self.player_location["row"] = teleport_data["end_coord"][0]
                self.player_location["col"] = teleport_data["end_coord"][1]
                self.load_map(teleport_data["target_map"]())
                return True
        return False

    def move_player(self, command): # Move the player
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

        if self.check_teleport(new_row, new_col):
            return
        
        if 0 <= new_row < len(self.active_map) and 0 <=new_col < len(self.active_map[0]):
            if self.active_map[new_row][new_col] is not None:
                self.player_location["row"] = new_row
                self.player_location["col"] = new_col


    def gameloopMapManager(self):
        '''
        Update map, do things... etc
        '''
        self.update_map()
        print(self.player_location)
        print(f"Current location: {self.active_map[self.player_location['row']][self.player_location['col']]}")
        while (command := input("W, A, S, D: ").strip().lower()) not in {"w", "a", "s", "d"}:
                print("Wrong Move")
        else:
                self.move_player(command)
            

mm = MapManager()
mm.load_map(maps.minimap_4)
# mm.update_map()

while True:
    mm.gameloopMapManager()


