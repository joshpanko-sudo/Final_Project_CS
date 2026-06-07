from tabulate import tabulate
from colorama import init

init()

# =========================
# SETTINGS
# =========================
player = {"row": 0, "col": 0}
BLOCK_CHAR = "█" 

house_map = [
    ["Living Room", "Kitchen", None, None],
    ["Hallway", "Bathroom", "Bedroom", None],
    [None, "Office", "Garage", "Exit"]
]

ROWS = len(house_map)
COLS = len(house_map[0])

# 1. Determine the absolute maximum width needed
# (Longest room name + 2 for the brackets)
MAX_NAME_LEN = max(len(str(cell)) if cell else 0 for row in house_map for cell in row)
FIXED_WIDTH = MAX_NAME_LEN + 2

# =========================
# THE FIX: STABLE CELL GENERATOR
# =========================
def get_stable_cell(r, c):
    tile = house_map[r][c]
    is_player = (r == player["row"] and c == player["col"])
    
    # CASE 1: BLOCKED CELL
    if tile is None:
        return BLOCK_CHAR * FIXED_WIDTH
    
    # CASE 2: PLAYER IN ROOM
    if is_player:
        # Create the visible string first: "[Kitchen]"
        visible_text = f"[{tile}]"
        # Pad it to the FIXED_WIDTH
        padded = f"{visible_text:^{FIXED_WIDTH}}"
        # Apply the color codes AFTER padding
        return f"\033[7m{padded}\033[0m"
    
    # CASE 3: EMPTY ROOM
    # Use spaces to match the width of brackets: " Kitchen "
    visible_text = f" {tile} "
    return f"{visible_text:^{FIXED_WIDTH}}"

# =========================
# DISPLAY & LOOP
# =========================
def display_map():
    # Build a fresh grid with fixed-length strings
    grid = []
    for r in range(ROWS):
        grid.append([get_stable_cell(r, c) for c in range(COLS)])

    print("\n" + "="*30)
    # Using 'grid' tablefmt and forcing center alignment
    print(tabulate(
        grid, 
        tablefmt="fancy_grid", 
        stralign="center", 
        disable_numparse=True
    ))

def move(direction):
    r, c = player["row"], player["col"]
    nr, nc = r, c
    if direction == "1": nr -= 1
    elif direction == "2": nr += 1
    elif direction == "3": nc += 1
    elif direction == "4": nc -= 1

    if 0 <= nr < ROWS and 0 <= nc < COLS and house_map[nr][nc] is not None:
        player["row"], player["col"] = nr, nc

while True:
    display_map()
    print(f"\nCurrent Room: {house_map[player['row']][player['col']]}")
    cmd = input("Move (1-4) or Q: ").lower()
    if cmd == 'q': break
    move(cmd)