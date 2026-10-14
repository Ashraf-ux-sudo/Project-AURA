def process_command(command, memory):
    user_name = memory["user"]["name"]
    command = command.lower().strip()
    if command == "hello":
        return f"Hello, {user_name}! How can I help you?"
    elif command == "":
        return "Please enter a command."
    elif command == "status":
        return memory["aura"]["status"]
    elif command == "help":
        return "Available commands: hello, status, help, whoami"
    elif command == "whoami":
        return f"You are {user_name}."
    else:
        return "Unknown command."
    

def calculate_sum(a, b):
    return a + b
