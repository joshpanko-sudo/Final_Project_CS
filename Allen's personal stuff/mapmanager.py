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


class MapManager():
    def __init__(self) -> None:
        pass

  
    
    def longest_location_name(self,input_map):
         pass
    
    def create_coordinate_grid(self, rows, columns, input_map):
         pass

    def update_map(self, input_map):
         pass
    
    def check_teleport(self, map_data, row, col):
         pass
    
    def enter_map(self, map_data, row, col):
         pass
    
      def move_player(self, command, map_data):
         pass
    
    





while True: 
    while (command := input("W, A, S, D: ").strip().lower()) not in {"w", "a", "s", "d", "e"}:
            print("Wrong Move")
        else:
            mm.move_player(command, map_config)
    


# mm = mapManager()

# mm.load_map(maps.minimap_3)

    

