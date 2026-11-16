"""
Datheon Python Programming Internship
Task 3: Automated File Organizer & Cleanup Utility

This program organizes files into folders based on their
file type. It also provides a safe preview mode before
moving files.
"""

from pathlib import Path
import shutil


# File categories based on extensions
FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".svg"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf",
        ".odt"
    ],
    "Spreadsheets": [
        ".xls", ".xlsx", ".csv"
    ],
    "Presentations": [
        ".ppt", ".pptx"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv"
    ],
    "Audio": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],
    "Code": [
        ".py", ".java", ".cpp", ".c", ".js",
        ".html", ".css", ".sql"
    ]
}


def get_category(file_extension):
    """Return the category for a file extension."""
    extension = file_extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """
    Create a unique filename if a file with the same
    name already exists in the destination folder.
    """
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1


def find_files(folder):
    """Return files directly inside the selected folder."""
    return [
        item for item in folder.iterdir()
        if item.is_file()
    ]


def organize_files(folder, preview=True):
    """
    Organize files into category folders.

    If preview is True, only show what would happen.
    Otherwise, move the files.
    """
    files = find_files(folder)

    if not files:
        print("\nNo files found in the selected folder.")
        return

    operations = []

    for file in files:
        category = get_category(file.suffix)

        category_folder = folder / category
        destination = category_folder / file.name

        destination = get_unique_destination(destination)

        operations.append(
            (file, category_folder, destination, category)
        )

    print("\n" + "=" * 70)
    print("FILE ORGANIZATION PLAN")
    print("=" * 70)

    for file, _, destination, category in operations:
        print(
            f"{file.name:<30} -> "
            f"{category}/{destination.name}"
        )

    print("=" * 70)

    if preview:
        print("\nPreview complete.")
        print("No files were moved.")

        return

    moved_count = 0

    for file, category_folder, destination, _ in operations:
        category_folder.mkdir(exist_ok=True)
        shutil.move(str(file), str(destination))
        moved_count += 1

    print(f"\nSuccessfully organized {moved_count} file(s).")


def choose_folder():
    """Ask the user for the folder to organize."""
    while True:
        folder_path = input(
            "\nEnter the folder path to organize: "
        ).strip().strip('"')

        folder = Path(folder_path).expanduser()

        if not folder.exists():
            print("Folder does not exist. Please try again.")
            continue

        if not folder.is_dir():
            print("The selected path is not a folder.")
            continue

        return folder


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("       AUTOMATED FILE ORGANIZER & CLEANUP UTILITY")
    print("=" * 60)
    print("1. Preview organization")
    print("2. Organize files")
    print("3. Exit")
    print("-" * 60)


def main():
    """Run the file organizer."""
    print("\nWelcome to the Automated File Organizer!")

    folder = choose_folder()

    while True:
        display_menu()

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            organize_files(folder, preview=True)

        elif choice == "2":
            print("\nYou are about to move files inside:")
            print(folder)

            confirmation = input(
                "Do you want to continue? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                organize_files(folder, preview=False)
            else:
                print("Operation cancelled.")

        elif choice == "3":
            print("\nThank you for using the File Organizer!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()