import os


class Terminal:
    def clear_display(self):
        os.system('clear')

    def get_command(self) -> str:
        print("=" * 40)
        print("EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        print("=" * 40)
        
        while True:
            choice = input("Select an option (1-5): ").strip()
            commands = {
                '1': 'create',
                '2': 'read',
                '3': 'update',
                '4': 'delete',
                '5': 'exit'
            }
            if choice in commands:
                return commands[choice]
            print("Invalid option. Please select 1-5.")

    def get_input(self, prompt: str) -> str:
        return input(prompt).strip()

    def display_message(self, message: str):
        print(message)

    def wait_for_enter(self):
        input("\nPress Enter to continue...")
