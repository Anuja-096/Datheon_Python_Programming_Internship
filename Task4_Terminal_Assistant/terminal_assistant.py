"""
Datheon Python Programming Internship
Task 4: Rule-Based Interactive Terminal Assistant

A rule-based command-line assistant that uses an external
JSON file for greetings and frequently asked questions.
"""

import json
import random
from datetime import datetime
from pathlib import Path


ASSISTANT_NAME = "DathBot"
FAQ_FILE = Path(__file__).parent / "sample_faq.json"


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


def load_faq_data():
    """Load greetings and FAQs from the JSON file."""
    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("\nWarning: sample_faq.json was not found.")
        return {"greetings": [], "faqs": []}

    except json.JSONDecodeError:
        print("\nWarning: sample_faq.json contains invalid JSON.")
        return {"greetings": [], "faqs": []}


def show_welcome():
    """Display the assistant welcome message."""
    print("\n" + "=" * 70)
    print(f"                 {ASSISTANT_NAME} - TERMINAL ASSISTANT")
    print("=" * 70)
    print("Hello! I am DathBot, your rule-based Python terminal assistant.")
    print("I can answer greetings, FAQs, Python questions, and more.")
    print("Type 'help' to see what I can do.")
    print("Type 'exit' to close the assistant.")
    print("=" * 70)


def show_help():
    """Display all available commands."""
    print("\nAVAILABLE COMMANDS")
    print("-" * 50)
    print("help        - Show available commands")
    print("hello       - Display a greeting")
    print("time        - Show the current time")
    print("date        - Show today's date")
    print("about       - Tell you about the assistant")
    print("faq         - Show available FAQs")
    print("python      - Give a Python programming tip")
    print("calculate   - Perform a basic calculation")
    print("joke        - Tell a programming joke")
    print("exit        - Exit the assistant")
    print("-" * 50)


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
    print("-" * 50)
    print("DathBot is a rule-based interactive terminal assistant.")
    print("It loads greetings and FAQs from a JSON file.")
    print("It uses Python functions, dictionaries, lists,")
    print("loops, conditional logic, JSON, and built-in modules.")
    print("-" * 50)


def show_faqs(faq_data):
    """Display all FAQs stored in the JSON file."""
    faqs = faq_data.get("faqs", [])

    if not faqs:
        print("\nNo FAQs are currently available.")
        return

    print("\nAVAILABLE FAQs")
    print("-" * 70)

    for index, faq in enumerate(faqs, start=1):
        print(f"{index}. {faq.get('question', 'Unknown question')}")

    print("-" * 70)


def answer_faq(user_input, faq_data):
    """Find and answer a matching FAQ question."""
    faqs = faq_data.get("faqs", [])
    user_text = user_input.lower().strip()

    faq_keywords = {
        "hours": ["hours", "operation", "timing", "open"],
        "submit": ["submit", "submission", "project", "github"],
        "certificate": ["certificate", "certification", "receive"]
    }

    for faq in faqs:
        question = faq.get("question", "").lower()
        answer = faq.get("answer", "")

        # Check for an exact question match.
        if question and question in user_text:
            print(f"\nDathBot: {answer}")
            return True

        # Check for related keywords.
        for keywords in faq_keywords.values():
            matching_keywords = sum(
                1
                for keyword in keywords
                if keyword in user_text and keyword in question
            )

            if matching_keywords >= 2:
                print(f"\nDathBot: {answer}")
                return True

    return False


def handle_greeting(user_input, faq_data):
    """Respond to greetings stored in the JSON file."""
    greetings = faq_data.get("greetings", [])
    normalized_input = user_input.lower().strip()

    for greeting in greetings:
        if normalized_input == greeting.lower().strip():
            print("\nDathBot: Hello! 👋 How can I help you?")
            return True

    return False


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
    print("-" * 50)
    print("Supported operators: +  -  *  /")
    print("Example: 25 + 15")
    print("-" * 50)

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


def process_command(command, faq_data):
    """Process a user command."""

    if handle_greeting(command, faq_data):
        return True

    if answer_faq(command, faq_data):
        return True

    if command in ("help", "commands"):
        show_help()

    elif command == "time":
        show_time()

    elif command == "date":
        show_date()

    elif command == "about":
        show_about()

    elif command == "faq":
        show_faqs(faq_data)

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
        print("\nDathBot: I don't understand that command.")
        print("Type 'help' to see the available commands.")

    return True


def main():
    """Run the terminal assistant."""
    faq_data = load_faq_data()

    show_welcome()

    while True:
        command = input("\nYou: ").strip().lower()

        if not command:
            print("Please enter a command.")
            continue

        if not process_command(command, faq_data):
            break


if __name__ == "__main__":
    main()