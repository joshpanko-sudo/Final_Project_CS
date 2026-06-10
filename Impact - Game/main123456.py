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
            print("Required Extensions: Questionary, Tabulate, Colorama, JSON, Bcrypt, Pathlib\n")
    
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
    from tabulate import tabulate
except ImportError:
    game_warnings("Import Error")
    safe_mode()



try:
    from map_managerV2 import MapManager as MM
    from item_manager import ItemManager as IM
except ImportError:
    game_warnings("Game File Error")
    safe_mode()


def startup():
    print("-----------------------------------------")
    print("             IMPACT GAME                 ")
    print("         Created By Josh and Allen       ")
    print("-----------------------------------------")

  




<<<<<<< HEAD
SP("You arrive home from studying at the highest science techology university", delay=0.0225)
SP("You see that you got mail. You open up your mail box", 0.0225)
SP("You have been selected as a researcher to try time travel!", 0.0225)

SP("The science team decided to fly you out first class.", 0.0225)
SP("You finally arrive and meet the leader, Jim Kalper", 0.0225)
SP("Jim: Welcome to the team!!", 0.0225)
SP("Jim: We are going to start testing tomorrow!", 0.0225)
SP("Jim: You should take some rest now..", 0.0225)

SP("The next day.....", 0.0625)
SP("Jim: Everything on?!?!", 0.0525)
SP("Mike: Red switch on!!", 0.0225)
SP("Lakrry: Green switch on!!", 0.0225)
SP("Loon: Black is blinking?????", 0.0225)
SP("Jim: Shut it down!!!!", 0.0225)
SP("Lakrry: ITS TO LATE, ITS FULL POWER!!", 0.0225)
SP("BLASTTTT!!!!!!!!", 0.00225)
SP("You appear in a strange new word", 0.0225)
SP("It looks like your world but......", 0.0225)
SP("Robots are taking over!!!", 0.0225)
SP("You: There is massive spider robots everywhere", 0.0225)

Enemy = Belly_Badge_Evil_Bear("Spider Droid", 20)
Player = Belly_Badge_Care_Bear("You", 50)
Stun = False
maxhealcooldown = 3
healcooldown = 0

start_battle(Enemy, Player)
=======
def main():
    startup()
    
def story():
    





if __name__ == "__main__":
    main()
>>>>>>> 7646d9bd81cecc9471a56588b26eda45374f3041
