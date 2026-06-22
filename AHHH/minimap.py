from tabulate import tabulate

minimap = [
    [None, "Garden", None, "kjrevbkrjgbvkjrg", None, None, None, ],
    [None, "Path", None, None, None, None, None, ],
    [None, "Castle", None, None, None, None, None, ],
    ["Tower", "Portal", "Temple", "Home", None, None, None, ],
    [None, None, None, "Garden", None, None, None, ],
    [None, None, None, "Cave", None, None, None, ],
    [None, None, None, "Garden", "Farm", "Gate", "Path", ],
]


# print(tabulate(minimap, tablefmt="fancy_grid", missingval="█"))



def longest_name(input_map:list):
    return len(
        max(
            (column for row in input_map for column in row if column is not None),
            key=len,
            default=""
        )
    )


def update_table(input_map:list):
    cannot_access = "█"
    updated_map = []

    for row in input_map:
        new_row = []
        for column in row:
            if column is None:
                new_row.append(cannot_access * longest_name(input_map))
            else: 
                new_row.append(column.center(longest_name(input_map)))
        updated_map.append(new_row)
    
    print(tabulate(updated_map, tablefmt="fancy_grid", colglobalalign = 'center'))


update_table(minimap)




from tabulate import tabulate



minimap = [
    [None, None, "Garden", None],
    ["Road", "Road", "Home", "Pool"],
    [None, None, "Road", None],
]


player_location = minimap[2][2]

# print(player_location)


def move():
    global player_location
    # row, column = player_location["row"], player_location["col"]
    print(player_location)
    
    while (move_direction := input("W, A, S, D: ").strip().lower()) not in {"w", "a", "s", "d"}:
        print("Wrong Move")
        pass
    else:
        row, col = player_location
        match move_direction:
            case "w":
                row -= 1
                print(player_location)
            case "a":
                pass
            case "s":
                pass
            case "d":
                pass
            case _:
                print("Invalid Movement")
                pass

# print(tabulate(minimap, tablefmt="fancy_grid"))
move()
# print(minimap[0][2])


