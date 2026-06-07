from tabulate import tabulate

minimap = [
    [None, None, None, None, None, None, None, ],
    [None, None, None, None, None, None, None, ],
    [None, None, None, None, None, None, None, ],
    [None, None, None, "Testing", None, None, None, ],
    [None, None, None, None, None, None, None, ],
    [None, None, None, None, None, None, None, ],
    [None, None, None, None, None, None, None, ],
]


print(tabulate(minimap, tablefmt="fancy_grid"))