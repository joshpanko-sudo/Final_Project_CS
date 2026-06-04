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
        self.player_location = {"row": 0, "col": 0}
        self.loaded_map_data = None
        self.active_map = None
    #map_data is going to be the input dict for the map stuff You will see

    def load_map(self, map_data):
        self.loaded_map_data = map_data
        self.active_map = map_data["maps"]
        # print(self.loaded_map_data)
        print(tabulate(self.active_map, tablefmt="fancy_grid", stralign="center", disable_numparse=True))

    def longest_map_name(self):
        for i in range(self.active_map[0]):
            print



mm = MapManager()
mm.load_map(maps.minimap)


