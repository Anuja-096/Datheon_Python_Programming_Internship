"""
Datheon Python Programming Internship
Task 4: Rule-Based Interactive Terminal Assistant

A simple command-line assistant that responds to predefined
commands using Python's built-in modules.
"""

from datetime import datetime
import random


ASSISTANT_NAME = "DathBot"

COMMANDS = {
    "help": "Show available commands",
    "hello": "Display a greeting",
    "time": "Show the current time",
    "date": "Show today's date",
    "about": "Tell you about the assistant",
    "python": "Give a Python programming tip",
    "calculate": "Perform a basic calculation",
    "joke": "Tell a short programming joke",
    "commands": "Show available commands",
    "exit": "Exit the assistant"
}


PYTHON_TIPS = [
    "Use functions to keep your Python code organized and reusable.",
    "Use meaningful variable names to make your code easier to understand.",
    "Practice solving small problems before moving to larger projects.",
    "Handle invalid user input so your programs are more reliable.",
    "Comments should explain why something is done when the code is not obvious."
]


JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python programmer wear glasses? Because they couldn't C!",
    "A programmer's favorite place is the foo bar."
]


def show_welcome():
    """Display the assistant welcome message."""
    print("\n" + "=" * 65)
    print(f"              {ASSISTANT_NAME} - TERMINAL ASSISTANT")
    print("=" * 65)
    print("Hello! I am DathBot, your rule-based Python terminal assistant.")
    print("Type 'help' to see what I can do.")
    print("Type 'exit' to close the assistant.")
    print("=" * 65)


def show_help():
    """Display all available commands."""
    print("\nAVAILABLE COMMANDS")
    print("-" * 45)

    for command, description in COMMANDS.items():
        print(f"{command:<12} - {description}")

    print("-" * 45)


def show_time():
    """Display the current time."""
    current_time = datetime.now().strftime("%I:%M:%S %p")
    print(f"\nCurrent time: {current_time}")


def show_date():
    """Display today's date."""
    current_date = datetime.now().strftime("%d %B %Y")
    print(f"\nToday's date: {current_date}")


def show_about():
    """Display information about the assistant."""
    print("\nABOUT DATHBOT")
    print("-" * 45)
    print("DathBot is a rule-based interactive terminal assistant.")
    print("It responds to predefined commands using Python.")
    print("It uses functions, dictionaries, lists, loops,")
    print("conditional logic, and built-in modules.")
    print("-" * 45)


def show_python_tip():
    """Display a random Python programming tip."""
    tip = random.choice(PYTHON_TIPS)
    print(f"\nPython Tip: {tip}")


def tell_joke():
    """Display a random programming joke."""
    joke = random.choice(JOKES)
    print(f"\nJoke: {joke}")


def calculate_expression():
    """Perform a basic arithmetic calculation safely."""
    print("\nBASIC CALCULATOR")
    print("-" * 45)
    print("Supported operators: +  -  *  /")
    print("Example: 25 + 15")
    print("-" * 45)

    expression = input("Enter calculation: ").strip()

    parts = expression.split()

    if len(parts) != 3:
        print("Invalid format.")
        print("Please use: number operator number")
        return

    first_value, operator, second_value = parts

    try:
        first_number = float(first_value)
        second_number = float(second_value)
    except ValueError:
        print("Invalid numbers. Please enter numeric values.")
        return

    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        if second_number == 0:
            print("Cannot divide by zero.")
            return

        result = first_number / second_number

    else:
        print("Unsupported operator.")
        print("Please use +, -, * or /.")
        return

    if result.is_integer():
        result = int(result)

    print(f"Result: {result}")


def process_command(command):
    """
    Process a user command.

    Returns False when the user wants to exit.
    Returns True for all other commands.
    """
    if command in ("hello", "hi", "hey"):
        print("\nHello! 👋 How can I help you?")

    elif command in ("help", "commands"):
        show_help()

    elif command == "time":
        show_time()

    elif command == "date":
        show_date()

    elif command == "about":
        show_about()

    elif command == "python":
        show_python_tip()

    elif command == "calculate":
        calculate_expression()

    elif command == "joke":
        tell_joke()

    elif command in ("exit", "quit", "bye"):
        print("\nThank you for using DathBot!")
        print("Good luck with your Python learning! 🚀")
        return False

    else:
        print("\nI don't understand that command.")
        print("Type 'help' to see the available commands.")

    return True


def main():
    """Run the terminal assistant."""
    show_welcome()

    while True:
        command = input("\nYou: ").strip().lower()

        if not command:
            print("Please enter a command.")
            continue

        if not process_command(command):
            break


if __name__ == "__main__":
    main()