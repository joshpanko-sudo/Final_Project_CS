'''
Legend:
Name: MapManager
Red highlight = error
Green highlight = working
Blue highlight = action
Error guide: Warning: MapManager could not {Error Here}
# GIVE JOSH THE AKIRA CODE
Yes, you could combine some aspects of this code, 
but I want to favor reliablilty and redundancy


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
        pass
        self.player_location = {"row": 0, "col": 0}

  
    
    def longest_location_name(self,input_map):
        '''
        A function to find the longest name in the provided map.
        '''
        return len(
            max(
                (column for row in input_map for column in row if column is not None), 
                key=len,
                default=""
                )
        )
        
    
    def create_coordinate_grid(self, rows, columns, input_map):
         pass

    def update_map(self, input_map):
        '''
        Generates a 2D array list of coorinate points to keep track of player location
        '''
        cooridnate_map = []
        for rows in range(len(input_map)): #Loop through tows of the input map
        cooridnate_map.append([format_map(rows, columns, input_map) for columns in range(len(input_map[0]))]) #Loop through columns of input map

    
    def check_teleport(self, map_data, row, col):
         pass
    
    def enter_map(self, map_data, row, col):
         pass
    
    def move_player(self, command, map_data):
         pass
    
  
                  
    def initlize_gameloop(self, map_data):
        # MapManager.player_location
        input_map = map_data["maps"]
        self.gameloop_Mapmanager(map_data)


    def gameloop_Mapmanager(self, map_data):
        # MapManager.player_location
        self.update_map(input_map)
        print(MapManager.player_location)
        print(f"Current location: {input_map[self.player_location['row']][self.player_location['col']]}")
        while (command := input("W, A, S, D: ").strip().lower()) not in {"w", "a", "s", "d"}:
            print("Wrong Move")
        else:
            move_player(command, input_map)

        

    

    





while True:
    MapManager.gameloop_Mapmanager(maps.minimap)

# while True: 
#     while (command := input("W, A, S, D: ").strip().lower()) not in {"w", "a", "s", "d", "e"}:
#             print("Wrong Move")
#         else:
#             mm.move_player(command, map_config)
    


# mm = mapManager()

# mm.load_map(maps.minimap_3)

    

