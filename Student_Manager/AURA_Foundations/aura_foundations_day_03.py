from aura_commands import process_command, calculate_sum
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
print(f"Sum: {calculate_sum(first_number, second_number)}")
command = input("Enter a command (hello/status): ")
print(process_command(command))