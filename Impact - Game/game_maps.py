tutorial_spawn = {
    "location_name": "Tutorial Spawn",

    "tutorial": "Welcome to the game. Here, you are at a tutorial level. Move around with W, A, S, D, and use F, and E to go to other areas. If you need help, type ?",

    "default_player_location": {"row":3, "col":3},

    "maps":
        [
            [None, None, "Path", "Path", "Path", None, None],
            [None, "Path", "Path", "Path", "Path", "Path", None],
            ["Path", "Path", "Path", "Path", "Path", "Path", "Path"],
            ["Path", "Path", "Path", "Spawn", "Path", "Path", "Path"],
            ["Path", "Path", "Path", "Path", "Path", "Path", "Path"],
            [None, "Path", "Path", "Path", "Path", "Path", None],
            [None, None, "Path", "Path", "Path", None, None],
        ],
    
    "teleport": 
        {
            # "minimap_3 ~> minimap": {"start_coord": (1,-1),"target_map": lambda: minimap,"end_coord": (0,1)},
        },
   

    "enter_teleport":
        {
            "Tutorial Level to Tutorial House": {"start_coord": (2,1),"target_map": lambda: basement,"end_coord": (0,0)},
        },

    "ladder_teleport":
        {
            # "Market ~> Second market floor": {"start_coord": (4,3),"target_map": lambda: market_second_floor,"end_coord": (4,3)},
            # "Market ~> Market Basement": {"start_coord": (4,3),"target_map": lambda: basement,"end_coord": (4,3)},
        }
}

tutorial_level = {
    "location_name": "Tutorial Level",

    "default_player_location": {"row":1, "col":0},

    "maps":
        [
            [None, "Viewing Platform", None],
            ["Spawn", "Path", None],
            [None, "House", None],
        ],
    
    "teleport": 
        {
            # "minimap_3 ~> minimap": {"start_coord": (1,-1),"target_map": lambda: minimap,"end_coord": (0,1)},
        },
   

    "enter_teleport":
        {
            "Tutorial Level to Tutorial House": {"start_coord": (2,1),"target_map": lambda: basement,"end_coord": (0,0)},
        },

    "ladder_teleport":
        {
            # "Market ~> Second market floor": {"start_coord": (4,3),"target_map": lambda: market_second_floor,"end_coord": (4,3)},
            # "Market ~> Market Basement": {"start_coord": (4,3),"target_map": lambda: basement,"end_coord": (4,3)},
        }
}

tutorial_House = {
    "location_name": "Tutorial House",

    "default_player_location": {"row":1, "col":0},

    "maps":
        [
            [None, "Viewing Platform", None],
            [None, "Path", None],
            [None, "House", None],
        ],
    
    "teleport": 
        {
            # "minimap_3 ~> minimap": {"start_coord": (1,-1),"target_map": lambda: minimap,"end_coord": (0,1)},
        },
   

    "enter_teleport":
        {
            "Tutorial Level to Tutorial House": {"start_coord": (2,1),"target_map": lambda: basement,"end_coord": (0,0)},
        },

    "ladder_teleport":
        {
            # "Market ~> Second market floor": {"start_coord": (4,3),"target_map": lambda: market_second_floor,"end_coord": (4,3)},
            # "Market ~> Market Basement": {"start_coord": (4,3),"target_map": lambda: basement,"end_coord": (4,3)},
        }
}