from aura_commands import process_command
from aura_foundations_day_05 import load_memory


def main():
    memory = load_memory()
    command = input("Enter a command (hello/status): ")
    response = process_command(command, memory)
    print(response)


if __name__ == "__main__":
    main()