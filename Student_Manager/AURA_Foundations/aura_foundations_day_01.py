def greet_user(name):
    return f"Hello, {name}. I am AURA."
def calculate_sum(a, b):
    return a + b
def process_command(command):
    command = command.lower()
    if command == "hello":
        return "Hello. How can I help you?"
    elif command == "status":
        return "AURA is running."
    else:
        return "Unknown command."

def main():
    user_name = input("Enter your name:")
    print(greet_user(user_name))
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print(f"Sum: {calculate_sum(first_number, second_number)}")
    command = input("Enter a command (hello/status):")
    print(process_command(command))
main()    