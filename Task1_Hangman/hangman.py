import random
from pathlib import Path

# ASCII art for 0 to 6 incorrect guesses.
HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

# Fallback words keep the game executable even if words.txt is not present.
FALLBACK_WORDS = [
    "python", "computer", "program", "software", "developer",
    "keyboard", "internet", "project", "student", "technology",
    "engineering", "database", "network", "hardware", "terminal"
]


def load_words():
    """Load suitable words from words.txt if it exists."""
    word_file = Path(__file__).with_name("words.txt")

    if word_file.exists():
        try:
            words = []
            with word_file.open("r", encoding="utf-8", errors="ignore") as file:
                for line in file:
                    word = line.strip().lower()
                    if word.isalpha() and 4 <= len(word) <= 12:
                        words.append(word)

            if words:
                return list(set(words))
        except OSError:
            pass

    return FALLBACK_WORDS


def display_word(secret_word, guessed_letters):
    """Return the masked word using guessed letters."""
    return " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_game():
    words = load_words()
    secret_word = random.choice(words)

    guessed_letters = set()
    incorrect_letters = set()
    mistakes = 0
    max_mistakes = 6

    print("\n" + "=" * 45)
    print("          HANGMAN WORD GUESSING GAME")
    print("=" * 45)
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect guesses available.")
    print("Duplicate guesses will not cost an attempt.\n")

    while mistakes < max_mistakes:
        print(HANGMAN_STAGES[mistakes])
        print("Word:", display_word(secret_word, guessed_letters))
        print("Incorrect guesses:", " ".join(sorted(incorrect_letters)) or "None")
        print(f"Attempts remaining: {max_mistakes - mistakes}")

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. No penalty for a duplicate guess.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_letters.add(guess)
            mistakes += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            print(HANGMAN_STAGES[mistakes])
            print("Word:", display_word(secret_word, guessed_letters))
            print("\n" + "*" * 45)
            print("          CONGRATULATIONS! YOU WON!")
            print(f"          The word was: {secret_word.upper()}")
            print("*" * 45)
            return

    print(HANGMAN_STAGES[max_mistakes])
    print("Word:", secret_word.upper())
    print("\n" + "!" * 45)
    print("             GAME OVER!")
    print(f"             The word was: {secret_word.upper()}")
    print("!" * 45)


def main():
    while True:
        play_game()

        choice = input("\nWould you like to play again? (y/n): ").strip().lower()
        if choice not in ("y", "yes"):
            print("\nThanks for playing Hangman!")
            break

        print("\nStarting a new game...")


if __name__ == "__main__":
    main()
