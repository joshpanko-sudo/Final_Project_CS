minimap = [
    [None, "Garden", None, None, None, None, None, ],
    [None, "Path", None, None, None, None, None, ],
    [None, "Castle", None, None, None, None, None, ],
    ["Tower", "Portal", "Temple", "Home", None, None, None, ],
    [None, None, None, "Garden", None, None, None, ],
    [None, None, None, "Cave", None, None, "None", ],
    ["None", None, None, "Garden", "Farm", "Gate", "Path", ],
]

minimap_2 = [
    ["Path", "Path", None, None, None],
    [None, "House", None, None, None],
    [None, "Garden", None, None, None],
    [None, "Yard", None, None, None],
    [None, None, None, None, None],
]

minimap_3 = {
    "default_player_location": {"row":1, "col":0},

    "maps":
        [
            [None, None, None, None],
            ["Garden", "Path", "Path", None],
            [None, None, "Base", None],
            [None, None, "Path", "Path"],
            [None, None, None, "Market"],
        ],
    
    "teleport": 
        {
            "minimap_3 ~> minimap_2": {"start_coord": (4,4),"target_map": minimap_2,"end_coord": (3,1)},
            "minimap_3 ~> minimap": {"start_coord": (3,1),"target_map": minimap,"end_coord": (0,1)},
            # "exit3": {"start_coord": (8,3),"target_map": minimap_2,"end_coord": (9,8)},
        }
        
        
    
}

test_map = {"maps":[[None, None], [None, None]], "exits": {"mapcoord":(0,1), "destination_map": minimap_3, "exitcoord": (9,8)}}