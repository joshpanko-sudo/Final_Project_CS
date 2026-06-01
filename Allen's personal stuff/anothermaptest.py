from tabulate import tabulate
import maps

# Global tracking of the player position
player_location = {"row": 1, "col": 0}


def longest_map_name(grid):
    return len(
        max(
            (column for row in grid for column in row if column is not None),
            key=len,
            default=""
        )
    )


def format_map(rows, columns, grid):
    check_tile = grid[rows][columns]  # The tile the player is on
    is_player = (rows == player_location["row"] and columns == player_location["col"])

    if check_tile is None:
        return "█" * longest_map_name(grid)
    
    if is_player:
        player_tile = f"\033[7m{check_tile}\033[0m"
    else:
        player_tile = f" {check_tile} "
        
    return f"{player_tile}"


def update_map(grid):
    cooridnate_map = []
    for rows in range(len(grid)):
        cooridnate_map.append([format_map(rows, columns, grid) for columns in range(len(grid[0]))])

    print("\033[2J\033[H")
    print("\n" + "=" * 30)
    print(tabulate(cooridnate_map, tablefmt="fancy_grid", stralign="center", disable_numparse=True))


def check_teleport(map_config, row, col):
    """
    Checks the teleport dictionary. If a coordinate matches, executes the 
    destination lambda to swap maps.
    """
    global player_location
    
    for _, teleport_data in map_config.get("teleport", {}).items():
        if row == teleport_data["start_coord"][0] and col == teleport_data["start_coord"][1]:
            
            # --- THE LAMBDA UNPACKING ---
            # Calling the lambda function () fetches the target map dictionary safely!
            next_map_config = teleport_data["target_map"]() 
            
            # Update player's new landing coordinates
            player_location["row"] = teleport_data["end_coord"][0]
            player_location["col"] = teleport_data["end_coord"][1]
            
            # Start the game loop with the newly fetched map configuration
            gameloop(next_map_config)
            return True # Signal that a teleport occurred
            
    return False # No teleport occurred


def move_player(direction, map_config):
    global player_location
    grid = map_config["maps"]
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

    # 1. Check if the player stepped into a portal first
    if check_teleport(map_config, new_row, new_col):
        return  # Stop execution here because gameloop() called a new instance

    # 2. Standard boundary and collision check on the current grid
    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
        if grid[new_row][new_col] is not None:
            player_location["row"] = new_row
            player_location["col"] = new_col


def gameloop(map_config):
    """
    Accepts the FULL map dictionary configuration, not just the grid layout.
    """
    global player_location
    grid = map_config["maps"]
    
    while True:
        update_map(grid)
        print(player_location)
        print(f"Current location: {grid[player_location['row']][player_location['col']]}")
        
        while (command := input("W, A, S, D: ").strip().lower()) not in {"w", "a", "s", "d"}:
            print("Wrong Move")
        else:
            move_player(command, map_config)


if __name__ == "__main__":
    # Start the game by passing the entire dictionary configuration
    gameloop(maps.minimap_3)