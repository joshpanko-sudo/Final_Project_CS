from tabulate import tabulate
import os

# --- MAP DATA ---
minimap = [
    [None, "Garden", None, None, None, None, None],
    [None, "Path", None, None, None, None, None],
    [None, "Castle", None, None, None, None, None],
    ["Tower", "Portal", "Temple", "Home", None, None, None],
    [None, None, None, "Garden", None, None, None],
    [None, None, None, "Cave", None, None, "None"],
    ["None", None, None, "Garden", "Farm", "Gate", "Path"],
]

minimap_2 = [
    ["Path", "Path", None, None, None],
    [None, "House", None, None, None],
    [None, "Garden", None, None, None],
    [None, "Yard", None, None, None],
    [None, None, None, None, None],
]

# --- JOINING LOGIC ---

def join_maps_horizontally(map_a, map_b):
    """Joins map_b to the right of map_a."""
    height = max(len(map_a), len(map_b))
    width_a = len(map_a[0])
    width_b = len(map_b[0])
    
    new_map = []
    for i in range(height):
        # Get row from map_a or a empty row if map_a is shorter
        row_a = map_a[i] if i < len(map_a) else [None] * width_a
        # Get row from map_b or a empty row if map_b is shorter
        row_b = map_b[i] if i < len(map_b) else [None] * width_b
        new_map.append(row_a + row_b)
    return new_map

def join_maps_vertically(map_a, map_b):
    """Joins map_b below map_a."""
    width = max(len(map_a[0]), len(map_b[0]))
    
    def pad_width(m, target_w):
        return [row + [None] * (target_w - len(row)) for row in m]
    
    return pad_width(map_a, width) + pad_width(map_b, width)

# --- GAME ENGINE ---

player_location = {"row": 0, "col": 1}

def longest_map_name(input_map):
    # Flatten map and find the longest string length for consistent cell sizing
    names = [str(col) for row in input_map for col in row if col is not None]
    return len(max(names, key=len, default=""))

def format_map(r, c, input_map, cell_width):
    check_tile = input_map[r][c]
    is_player = (r == player_location["row"] and c == player_location["col"])

    if check_tile is None:
        return "█" * (cell_width + 2) # +2 accounts for the padding spaces
    
    if is_player:
        # Invert colors for player
        return f"\033[7m {check_tile} \033[0m"
    else:
        # Standard tile with padding to match width
        return f" {check_tile} ".center(cell_width + 2)

def update_map(input_map):
    cell_width = longest_map_name(input_map)
    coordinate_map = []
    
    for r in range(len(input_map)):
        row_data = [format_map(r, c, input_map, cell_width) for c in range(len(input_map[0]))]
        coordinate_map.append(row_data)

    # Clear screen (Works on most terminals)
    print("\033[2J\033[H")
    print("\n" + "=" * 40)
    print(tabulate(coordinate_map, tablefmt="fancy_grid", stralign="center", disable_numparse=True))

def move_player(direction, input_map):
    global player_location
    new_row, new_col = player_location["row"], player_location["col"]
    
    match direction:
        case "w": new_row -= 1
        case "a": new_col -= 1
        case "s": new_row += 1
        case "d": new_col += 1

    # Check boundaries and if tile is walkable (not None)
    if 0 <= new_row < len(input_map) and 0 <= new_col < len(input_map[0]):
        if input_map[new_row][new_col] is not None:
            player_location["row"] = new_row
            player_location["col"] = new_col

def gameloop(input_map):
    while True:
        update_map(input_map)
        current_tile = input_map[player_location["row"]][player_location["col"]]
        print(f"Location: ({player_location['row']}, {player_location['col']}) | Tile: {current_tile}")
        
        command = input("Move (W, A, S, D) or 'Q' to quit: ").strip().lower()
        if command == 'q':
            break
        elif command in {"w", "a", "s", "d"}:
            move_player(command, input_map)
        else:
            print("Invalid Move")

# --- EXECUTION ---

# Option A: Join Horizontally
world_map = join_maps_horizontally(minimap, minimap_2)

# Option B: Join Vertically (Uncomment to use)
# world_map = join_maps_vertically(minimap, minimap_2)

gameloop(world_map)