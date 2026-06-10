import os
import sys

# --- Cross-Platform Key Capture Setup ---
def get_key():
    """Captures a single keypress instantly without requiring Enter."""
    if os.name == 'nt':  # Windows
        import msvcrt
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch in (b'\x00', b'\xe0'):
                ch = msvcrt.getch()
                if ch == b'H': return 'up'
                if ch == b'P': return 'down'
            try:
                return ch.decode('utf-8').lower()
            except UnicodeDecodeError:
                return None
        return None
    else:  # macOS / Linux
        import tty
        import select
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
            if rlist:
                ch = sys.stdin.read(1)
                if ch == '\x1b':
                    ch2 = sys.stdin.read(1)
                    if ch2 == '[':
                        ch3 = sys.stdin.read(1)
                        if ch3 == 'A': return 'up'
                        if ch3 == 'B': return 'down'
                return ch.lower()
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def clear_screen():
    """Clears the terminal screen smoothly."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Menu Configuration ---
options = ["Start Game", "Exit"]
current_selection = 0  # 0 for the first option, 1 for the second

# --- Main Menu Loop ---
while True:
    clear_screen()
    print("--- MAIN MENU ---")
    print("Use W/S or Arrow Keys to navigate. Press 'Enter' to select.\n")
    
    # Render options with the trailing selection arrow
    for i, option in enumerate(options):
        if i == current_selection:
            print(f"{option} <-")  # Arrow on the rightside
        else:
            print(f"{option}")
            
    # Input Loop
    key = None
    while key is None:
        key = get_key()
        
    # Processing Navigation Logic
    if key in ('w', 'up', 's', 'down'):
        # Toggles seamlessly between 0 and 1
        current_selection = 1 - current_selection
    elif key in ('\r', '\n'):  # Enter key pressed
        clear_screen()
        print(f"You selected: {options[current_selection]}!")
        break
