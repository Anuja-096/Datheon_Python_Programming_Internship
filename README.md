# Datheon Python Programming Internship

This repository contains the projects completed as part of the **Datheon Python Programming Internship**.

The projects demonstrate practical Python programming concepts including functions, loops, conditional statements, data structures, file handling, JSON processing, input validation, and modular programming.

---

## Internship Tasks

### Task 1 — Hangman Word Guessing Game

A console-based Hangman game where the player guesses a hidden word one letter at a time.

**Features:**
- Random word selection
- Letter-by-letter guessing
- Maximum of 6 incorrect attempts
- ASCII hangman stages
- Tracks previously guessed letters
- Duplicate guesses do not reduce attempts
- Win and loss handling
- Replay option
- Uses an external word list

**Files:**
- `hangman.py`
- `words.txt`

**Concepts Used:**
- Lists and sets
- Loops
- Conditional statements
- Functions
- Random module
- File handling
- User input validation

---

### Task 2 — Stock Portfolio Performance Tracker

A console-based application for managing a stock portfolio and calculating investment performance.

**Features:**
- Add stocks
- View portfolio
- Remove stocks
- Calculate total investment
- Calculate current portfolio value
- Calculate profit or loss
- Calculate percentage return
- Display overall portfolio status
- Input validation
- Prevents duplicate stock entries

**File:**
- `portfolio_tracker.py`

**Concepts Used:**
- Functions
- Lists and dictionaries
- Loops
- Conditional statements
- Exception handling
- Arithmetic calculations
- Input validation

---

### Task 3 — Automated File Organizer & Cleanup Utility

A file organization utility that automatically categorizes files into folders based on their extensions.

**Features:**
- Preview organization before moving files
- Organizes files into categories
- Supports images, documents, spreadsheets, presentations, videos, audio, archives, and code files
- Handles unknown file types using an `Others` category
- Prevents filename conflicts
- User confirmation before moving files
- Handles invalid folder paths
- Uses Python's `shutil` module for file movement

**File:**
- `file_organizer.py`

**Concepts Used:**
- `pathlib`
- `shutil`
- File and directory handling
- Functions
- Dictionaries
- Loops
- Conditional statements
- Input validation

---

### Task 4 — Rule-Based Interactive Terminal Assistant

A command-line assistant named **DathBot** that responds to predefined commands and uses an external JSON file for greetings and frequently asked questions.

**Features:**
- Greeting recognition
- JSON-based FAQ responses
- Displays available FAQs
- Internship-related FAQ responses
- Current time
- Current date
- Python programming tips
- Basic calculator
- Programming jokes
- Help and command handling
- Invalid input handling
- Missing or invalid JSON file handling
- Exit commands

**Files:**
- `terminal_assistant.py`
- `sample_faq.json`

**Concepts Used:**
- Functions
- Lists and dictionaries
- Loops
- Conditional statements
- JSON file handling
- `pathlib`
- `datetime`
- `random`
- Exception handling
- User input validation

---

## Repository Structure

```text
Datheon_Python_Programming_Internship
│
├── Task1_Hangman
│   ├── hangman.py
│   └── words.txt
│
├── Task2_Stock_Portfolio
│   └── portfolio_tracker.py
│
├── Task3_File_Organizer
│   └── file_organizer.py
│
├── Task4_Terminal_Assistant
│   ├── terminal_assistant.py
│   └── sample_faq.json
│
└── README.md