import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """displays the main menu options"""
    clear_screen()
    print("Book Management System")
    print("1. Alle Bücher anzeigen")
    print("2. Verfügbare Bücher anzeigen")
    print("3. Ausgeliehen Bücher anzeigen")
    print("4. Buch hinzufügem")
    print("5. Buch entfernen")
    print("6. Buch verteilen")
    print("7. Buch einsammeln")
    print("0. Programm beenden")

def display_error(message):
    """displays an error message"""
    print(f"Error: {message}")

def display_info(message):
    """displays a general message"""
    print(f"Info: {message}")

def get_user_choice():
    """Prompt the user to select a menu option and return the validated choice.

    Repeatedly prompts with "Please select an option: " until the user enters
    an integer within the inclusive range. Non-integer input and integers
    outside the allowed range cause an explanatory message to be printed and the
    prompt to be repeated.

    Side effects:
    - Reads from standard input using input().
    - Writes validation messages to standard output using print().

    Returns:
        int: The validated menu choice (0 through 7).
    """
    while True:
        try:
            choice = int(input("Auswahl eingeben (0-7): "))
            if 0 <= choice <= 7:
                return choice
            else:
                display_error("Ungültige Eingabe. Bitte gültige Auswahl eingeben.")
                continue
        except ValueError:
            display_error("Ungültige Eingabe. Bitte gültige Auswahl eingeben.")


def display_list_of_books(list_of_books):
    """prints book information from a list of dictionaries"""
    
    if not list_of_books:
        display_info("Keine Bücher in der Liste")
        return

    keys = list(list_of_books[0].keys())

    # compute column widths based on header and all rows
    widths = []
    for key in keys:
        widths.append(len(str(key)))

    for book in list_of_books:
        for i, key in enumerate(keys):
            val_len = len(str(book.get(key, "")))
            if val_len > widths[i]:
                widths[i] = val_len

    # print header
    print()
    for i, key in enumerate(keys):
        print(f" {key:{widths[i] + 2}}", end="")
    print()

    # separator line based on printed width
    total_width = sum(widths) + 3 * len(widths)
    print("-" * total_width)

    # print rows
    for book in list_of_books:
        for i, key in enumerate(keys):
            print(f" {str(book.get(key, '')):{widths[i] + 2}}", end="")
        print()

def get_book_details_from_user():
    """prompts the user for book details and returns a book dictionary"""
    isbn = input("ISBN eingeben: ")
    titel = input("Titel eingeben: ")
    fach = input("Fach eingeben: ")
    while True:
        try:
            gesamt = int(input("Stückzahl eingeben: "))
            break
        except ValueError:
            display_error("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
    
    return {
        "isbn": isbn,
        "title": titel,
        "subject": fach,
        "total": gesamt
    }

def get_book_name_from_user():
    """prompts the user for a book name and returns it"""
    return input("Geben Sie den Namen des Buches ein: ")


def wait_for_user_interaction():
    input("\n[Drücke Enter um fortzufahren...]")