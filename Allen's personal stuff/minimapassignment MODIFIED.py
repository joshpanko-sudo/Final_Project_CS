from tabulate import tabulate
import mapkeys


default_player_location = {"row": 0, "col": 0}
player_location = {"row":0, "col":1}

def load_map():
    for _ in mapkeys.world:
        print(mapkeys.world["minimap"]["data"][""])

def longest_map_name(input_map):
    return len(
        max(
            (column for row in input_map for column in row if column is not None),
            key=len,
            default=""
        )
    )




def format_map(rows, columns, input_map):
    check_tile = input_map[rows][columns] #The tile the player is on
    is_player = (rows == player_location["row"] and columns == player_location["col"]) #Check if player is occupying tile

    if check_tile is None: #No location avaliable, empty tile
        return "█" * longest_map_name(input_map)
    if is_player: #If is_player is true, highlight the tile and add brackets to represent player is there
        # player_tile = f"[{check_tile}]" #Puts brackets around player occupied tile
        player_tile = f"\033[7m{check_tile}\033[0m"

    else:
        player_tile = f" {check_tile} " #No brackts, no player occupation
    return f"{player_tile}" # Return the tile modified by palayer location


def update_map(input_map):
    '''
    Generates a 2D array list of coorinate points to keep track of player location
    '''
    cooridnate_map = []
    for rows in range(len(input_map)): #Loop through tows of the input map
        cooridnate_map.append([format_map(rows, columns, input_map) for columns in range(len(input_map[0]))]) #Loop through columns of input map

    print("\033[2J\033[H")
    print("\n" + "=" * 30)
    print(tabulate(cooridnate_map, tablefmt="fancy_grid", stralign="center", disable_numparse=True)) # Print out the map


def move_player(direction, input_map): # Move the player
    global player_location
    rows, cols = player_location["row"], player_location["col"]
    new_row, new_col = rows, cols
    match direction:
        case "w":
            new_row -= 1
        case "a":
            new_col -= 1
        case "s":
            new_row += 1
        case "d":
            new_col += 1

    if new_col == 6 and new_row == 7:
        player_location = default_player_location
        gameloop(maps.minimap_2)
        return
    
    if 0 <= new_row < len(input_map) and 0 <=new_col < len(input_map[0]):
        if input_map[new_row][new_col] is not None:
            player_location["row"] = new_row
            player_location["col"] = new_col


    
def gameloop(input_map):
    global player_location
    while True:
        update_map(input_map)
        print(player_location)
        print(f"Current location: {input_map[player_location["row"]][player_location["col"]]}")
        while (command := input("W, A, S, D: ").strip().lower()) not in {"w", "a", "s", "d"}:
            print("Wrong Move")
        else:
            move_player(command, input_map)

# gameloop(maps.minimap)

if __name__ == "__main__":
    load_map()