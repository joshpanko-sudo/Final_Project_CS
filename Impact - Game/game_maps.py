'''
Rigid means that data must be there and exist
Soft means the data is optional and does not need to exist

map_name = {
    Rigid "location_name":"Name your location
    Soft "tutorial": "Put help data here, acessed with (?)"
    Soft "actual_tutorial": "Place tutorial of information data here. Will be displayed everytime. Cannot be turned off."
    Rigid "default_player_location": {"row": 0, "col": 0} Place default player spawn location here
    Rigid "maps": Place map data here
        [
        [None, None],
        [None, None],
        ]

    All teleport systems use this system:  "Teleport Name": {"start_coord": (0,0),"target_map": lambda: Place map to teleport to here,"end_coord": (0,0)},
    Rigid "teleport": Place teleport data here. Player will automatically teleport upon matching the coordinates

    


}



'''
battle_1 = {
    "location_name": "Battle 1!",

    "tutorial": "Move around with W, A, S, D, and use F, and E to go to other areas. If you need help, type ?",

    "actual_tutorial": "The spider robot is ahead of you! Move the player with WASD to the spider bot, and press Q to start the battle!",

    "default_player_location": {"row":1, "col":0},

    "maps":
        [
            ["Path", "Path", "Path", "Path", "Path", "Path", "Path", "Path"],
            ["Path", "Path", "Path", "Path", "Path", "Path", "Path", "Path"],
            ["Path", "Path", "Path", "Path", "Path", "Path", "Path", "Path"],
        ],

    "teleport":
    {

    },

    "enter_teleport":
    {

    },

    "enemies": {
        (1, 7): {
            "name": "Spider Droid",
            "health": 80,
            "max_health": 100,
            "description": "A spider like robot."
        },
        (0, 4): {
            "name": "Spider Droid",
            "health": 60,
            "max_health": 70,
            "description": "A spider like robot."
        }
    },


}











tutorial_spawn = {
    "location_name": "Tutorial Spawn",

    "tutorial": "Move around with W, A, S, D, and use F, and E to go to other areas. If you need help, type ?",

    "actual_tutorial": "Try to find the key. It should be here somewhere...",

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
            "tutorial_spawn to tutorial_level_1": {"start_coord": (7,2),"target_map": lambda: tutorial_level,"end_coord": (0,0)},
            "tutorial_spawn to tutorial_level_2": {"start_coord": (7,3),"target_map": lambda: tutorial_level,"end_coord": (0,1)},
            "tutorial_spawn to tutorial_level_3": {"start_coord": (7,4),"target_map": lambda: tutorial_level,"end_coord": (0,2)},
        },

    "enter_teleport":
        {
        
        },

    "ladder_teleport":
        {

        }
}

tutorial_level = {
    "location_name": "Tutorial One",

    "default_player_location": {"row":1, "col":0},

    "maps":
        [
            ["Path", "Path", "Path"],
            ["Path", "Path", "Path"],
            ["Path", "Path", "Path"],
            ["Path", "Path", "Path"],
            ["Path", "Path", "Path"],
            ["Path", "Path", "Path"],
            ["Path", "Path", "Path"],
            ["Path", "Path", "Path"],
            ["Path", "Path", "Path"],
        ],
    
    "teleport": 
        {
            "tutorial_level to tutorial_spawn_1": {"start_coord": (-1,0),"target_map": lambda: tutorial_spawn,"end_coord": (6,2)},
            "tutorial_level to tutorial_spawn_2": {"start_coord": (-1,1),"target_map": lambda: tutorial_spawn,"end_coord": (6,3)},
            "tutorial_level to tutorial_spawn_3": {"start_coord": (-1,2),"target_map": lambda: tutorial_spawn,"end_coord": (6,4)},
        },
   

    "enter_teleport":
        {
            # "Tutorial Level to Tutorial House": {"start_coord": (2,1),"target_map": lambda: basement,"end_coord": (0,0)},
        },

    "ladder_teleport":
        {

        },
    
    "items": {
        (7, 2): {
            "name": "Warp key",
            "amount": 1,
            "max_stack": 1,
            "exit_on_pickup": True
        }
    },

      "enemies": {
        (6, 2): {
            "name": "Spider Droid",
            "health": 80,
            "max_health": 100,
            "description": "A spider like robot."
        },
        (8, 2): {
            "name": "Spider Droid",
            "health": 60,
            "max_health": 70,
            "description": "A spider like robot."
        },
          (7, 1): {
            "name": "Spider Droid",
            "health": 60,
            "max_health": 70,
            "description": "A spider like robot."
        }
    },

}

tutorial_House = {
    "location_name": "Tutorial House",

    "default_player_location": {"row":0, "col":1},

    "maps":
        [
            [None, "Path", None],
            [None, "Path", None],
            [None, "Path", None],
        ],
    
    "teleport": 
        {
            # "minimap_3 ~> minimap": {"start_coord": (1,-1),"target_map": lambda: minimap,"end_coord": (0,1)},
        },
   

    "enter_teleport":
        {
            # "Tutorial Level to Tutorial House": {"start_coord": (2,1),"target_map": lambda: basement,"end_coord": (0,0)},
        },

    "ladder_teleport":
        {
            # "Market ~> Second market floor": {"start_coord": (4,3),"target_map": lambda: market_second_floor,"end_coord": (4,3)},
            # "Market ~> Market Basement": {"start_coord": (4,3),"target_map": lambda: basement,"end_coord": (4,3)},
        },

    "enemies": {
        (2, 1): {
            "name": "Helper Robot",
            "health": 150,
            "max_health": 150,
            "description": "The final boss."
        }
    }
    

}