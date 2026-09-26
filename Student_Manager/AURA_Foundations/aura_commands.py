def process_command(command):
    command = command.lower()
    if command == "hello":
        return "Hello. How can I help you?"
    elif command == "status":
        return "AURA is running."
    else:
        return "Unknown command."
def calculate_sum(a, b):
    return a + b