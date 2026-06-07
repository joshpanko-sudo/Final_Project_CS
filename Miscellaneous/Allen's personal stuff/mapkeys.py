import maps



world = {
        "minimap": {
                    "data": maps.minimap,
                    "exits": {
                              (7, 6): {"target_map": "minimap2", "start_pos": {"row": 0, "col": 0}}
        }
    },

    
    "minimap2":{"data":maps.minimap_2,"exits":{(0, 0): {"target_map": "minimap", "start_pos": {"row": 7, "col": 5}}}},



    "minimap3":{"data":maps.minimap_3,"exits":{(0, 0): {"target_map": "minimap", "start_pos": {"row": 7, "col": 5}}}},

    # world = {key: {key:maps.minimap, value: exits}, value}





}

# world = {
#     "forest": {
#         "data": maps.minimap,
#         "exits": {
#             (7, 6): {"target_map": "cave", "start_pos": {"row": 0, "col": 0}},  # Southern exit
#             (3, 9): {"target_map": "town", "start_pos": {"row": 5, "col": 1}},  # Eastern exit
#             (4, 4): {"target_map": "hut",  "start_pos": {"row": 2, "col": 2}}   # Secret entrance
#         }
#     },
#     "town": {
#         "data": maps.town_map,
#         "exits": {
#             (5, 0): {"target_map": "forest", "start_pos": {"row": 3, "col": 8}} # Back to forest
#         }
#     },
#     # ... and so on
# }