from aura_commands import process_command
from aura_foundations_day_05 import load_memory


def main():
    memory = load_memory()
    while True:
        command = input("Enter a command (hello/status/whoami/help/exit): ")
        command = command.lower().strip()
        if command == "exit":
            print("Exiting AURA. Goodbye!")
            break
        response = process_command(command, memory)
        print(response)

if __name__ == "__main__":
    main()