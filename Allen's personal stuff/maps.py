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
    "default_player": {"row":1, "col":0},

    "maps":
        [
            [None, None, None, None],
            ["Garden", "Path", "Path", None],
            [None, None, "Base", None],
            [None, None, "Path", "Path"],
            [None, None, None, "Market"],
        ],
    
    "exit": 
        {
            "exit1": {"mapcoord": (0,1),"destination_map": minimap_2,"exitcoord": (9,8)},
            "exit2": {"mapcoord": (0,1),"destination_map": minimap_2,"exitcoord": (9,8)},
            "exit3": {"mapcoord": (0,1),"destination_map": minimap_2,"exitcoord": (9,8)},
        }
        
        
    
}

test_map = {"maps":[[None, None], [None, None]], "exits": {"mapcoord":(0,1), "destination_map": minimap_3, "exitcoord": (9,8)}}