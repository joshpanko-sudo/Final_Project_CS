game_name = "Impact"

# extensions_loaded = True
# Red means error
# Green means working
# Blue means action in progress
# Errors: Warning: main.py cannot {Error Here}

print(f"Loading {game_name}...")


def game_warnings(warning: str):
    match warning:
        case "Invalid Input":
            print("Invalid Input Detected")

        case "Import Error":
            print("Warning: main.py has failed to load extensions, please reinstall extensions\n")
            print("Required Extensions: Questionary, Tabulate, \n")
    
        case "Game File Error":
            print("Warning: main.py has failed to load game files, please repair game files")

        case "Fatal Error":
            print("Warning: main.py has encountered a fatal error")
            quit()

        case _:
            print("Warning: main.py cannot operate properly. Fatal Error")
            quit()


def safe_mode():
    while (choice := input(f"{game_name}, has started in safe mode. Select an option: 1: Quit, 2: Repair, 3: Instructions: ")).strip() not in {"1", "2"}:
        game_warnings("Invalid Input")
    else:
        match choice:
            case "1":
                quit()
            case "2":
                pass
                # Redownload or reextract assets, and check everything. Does not reinstall extensions though.
            case "3":
                print("Instructions: Download a IDE of choice (Prefer VS Code)\nInstall extensions and dependancies" \
                "\nMake sure that all game files are installed and are in correct locations.")
                safe_mode()
            case _:
                game_warnings("Invalid Input")


try:
    import questionary
except ImportError:
        game_warnings("Import Error")
        safe_mode()
print(f"Importing files for {game_name}".center(20, "-"))
try:
    from map_managerV2 import MapManager
    MM = MapManager()
except ImportError:
    game_warnings("Game File Error")
    safe_mode()


def print_credits():
    '''
    Print the credits for the game
    '''
    print("System design: Allen\n" \
    "Game Design: Josh")
    MM.continue_game()
    startup()


def startup():
    print("\n-----------------------------------------")
    print("|            IMPACT GAME                |")
    print("|        Created By Josh and Allen      |")
    print("-----------------------------------------\n")
    option = questionary.select("Main Menu", choices=["Start Game", "Quit", "Credits"]).ask()
    match option:
        case "Start Game":
            start_story()
        case "Quit":
            quit()
        case "Credits":
            print_credits()


  




def main():
    startup()

    
def start_story():
    pass
    
    





if __name__ == "__main__":
    main()
