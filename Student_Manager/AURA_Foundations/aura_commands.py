def process_command(command, memory):
    user_name = memory["user"]["name"]
    command = command.lower()
    if command == "hello":
        return f"Hello, {user_name}! How can I help you?"
    elif command == "status":
        return memory["aura"]["status"]
    else:
        return "Unknown command."
def calculate_sum(a, b):
    return a + b
