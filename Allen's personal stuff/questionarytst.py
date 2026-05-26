try: 
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print("Warning: FileManager could not load colorama.")
    quit()

from pathlib import Path
import questionary






class FileManager:
    def __init__(self) -> None:
        # State variables to track where we are
        self.active_file = Path(__file__).resolve()
        self.current_dir = self.active_file.parent
        self.main()

    def main(self):
        self.filemanager()

    def filemanager(self):
        while True:
            print(f"\n{Fore.GREEN}Location: {self.current_dir}")
            print(f"{Fore.BLUE}Active Target: {self.active_file.name}")

            file_action = questionary.select(
                "File Manager Menu:",
                choices=[
                    "View current file",
                    "CD / Change Target", 
                    "List available files",
                    "Create Files",
                    "Delete files",
                    "Quit"
                ]
            ).ask()

            if file_action == "Quit" or file_action is None:
                break

            match file_action:
                case "View current file":
                    print(f"\n{Fore.GREEN}Full Path: {self.active_file}")
                    print(f"Size: {self.active_file.stat().st_size} bytes")
                case "CD / Change Target":
                    self.change_directory_or_file()
                case "List available files":
                    self.listFiles()
                case "Create Files":
                    self.createFile()
                case "Delete files":
                    self.deleteFile()

    def change_directory_or_file(self):
        """Dynamic navigation with a Back option"""
        while True:
            # Get directories and files
            items = [f.name for f in self.current_dir.iterdir()]
            
            # Navigation helpers
            choices = [".. (Up one level)", "Back to Main Menu"] + items

            choice = questionary.select(
                f"Navigate (Currently in {self.current_dir.name}):",
                choices=choices
            ).ask()

            if choice == "Back to Main Menu" or choice is None:
                break
            
            if choice == ".. (Up one level)":
                self.current_dir = self.current_dir.parent
                continue

            new_path = self.current_dir / choice
            if new_path.is_dir():
                self.current_dir = new_path
            else:
                self.active_file = new_path
                print(f"{Fore.GREEN}New target set: {self.active_file.name}")
                break # Return to main menu after selecting a specific file

    def listFiles(self):
        print(f"\n{Fore.BLUE}--- Files in {self.current_dir.name} ---")
        for item in self.current_dir.iterdir():
            icon = "📁" if item.is_dir() else "📄"
            print(f"{icon} {item.name}")
        questionary.press_any_key_to_continue().ask()

    def createFile(self):
        name = questionary.text("New file name (or type 'back' to cancel):").ask()
        if name and name.lower() != 'back':
            try:
                (self.current_dir / name).touch()
                print(f"{Fore.GREEN}File '{name}' created.")
            except Exception as e:
                print(f"{Fore.RED}Warning: FileManager could not create file: {e}")

    def deleteFile(self):
        files = [f.name for f in self.current_dir.iterdir() if f.is_file()]
        if not files:
            print(f"{Fore.RED}No files to delete.")
            return

        choices = ["Back"] + files
        to_delete = questionary.select("Select file to delete:", choices=choices).ask()

        if to_delete == "Back" or to_delete is None:
            return

        confirm = questionary.confirm(f"Are you sure you want to delete {to_delete}?").ask()
        if confirm:
            try:
                (self.current_dir / to_delete).unlink()
                print(f"{Fore.BLUE}Deleted: {to_delete}")
            except Exception as e:
                print(f"{Fore.RED}Warning: FileManager could not delete {to_delete}: {e}")

if __name__ == "__main__":
    fm = FileManager()