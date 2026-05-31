'''
Legend:
Name: MapManager
Red highlight = error
Green highlight = working
Blue highlight = action
Error guide: Warning: MapManager could not {Error Here}

Yes, you could combine some aspects of this code, 
but I want to favor reliablilty and redundancy


'''

try:
    from tabulate import tabulate
except ImportError as e:
    print(f"Warning: MapManager could not load tabulate. {e}. Perhaps you have not installed it?")
    quit()

class mapManager():
    pass