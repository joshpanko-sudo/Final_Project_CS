'''
Legend:
Name: MapManager
Red highlight = error
Green highlight = working
Blue highlight = action
Error guide: Warning: MapManager could not {Error Here}

Yes, you could combine some aspects of this code, 
but I want to favor reliablilty and redundancy


'''

try:
    from tabulate import tabulate
except ImportError as e:
    print(f"Warning: MapManager could not load tabulate. {e}. Perhaps you have not installed it?")
    quit()

class Map:
    def __init__(self,map_name = None, default_player_location = None, grid_map = None, teleport_location = None) -> None:
        self.map_name = map_name
        self.default_player_location = default_player_location
        self.grid_map = grid_map
        self.teleport_location = teleport_location
    
    def createMap(self):
        pass





mm = Map()

minimap1 = Map("main map", )




# class mapManager():
#     def __init__(self) -> None:
#         self.active_map = None
#         self.active_coordinate_grid = None
#         self.player_location = None

    
#     def load_map(self, input_map:dict) -> bool:
        
#         active_map = input_map["maps"]
#         print(tabulate(active_map, tablefmt="fancy_grid", stralign="center", disable_numparse=True))
        


# mm = mapManager()

# mm.load_map(maps.minimap_3)

    

