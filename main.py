# Bookmanagement
import repo_csv as repo
import tui
import management


# Hauptprogramm
def main():
    # Load book data from CSV file
    file = "bestand.csv"

    try:
        all_books = repo.load_books(file)
    except FileNotFoundError:
        tui.display_error(f"Datei '{file}' nicht gefunden.")
        tui.display_info("Programm wird beendet.")
        return # exit if file does not exist
   
    while True:
        tui.display_menu()
        user_choice = tui.get_user_choice()
        tui.clear_screen()
        # using a match here instead multiple if - elif bloocks 
        match user_choice:
            case 1: # Alle Bücher anzeigen
                tui.display_list_of_books(all_books)
            case 2: # Verfügbare Bücher anzeigen
                pass  # TODO: implement this
            case 3: # Ausgeliehene Bücher anzeigen
                pass  # TODO: implement this
            case 4: # Buch hinzufügen
                pass  # TODO: implement this
            case 5: # Buch löschen
                pass # TODO: implement this
            case 6: # Buch ausleihen
                pass # TODO: implement this
            case 7: # Buch zurückgeben
                pass # TODO implement this
            case 0: # exit the programm
                repo.save_books(file, all_books)
                tui.display_info("Programm wird beendet.")
                return
        # Pause before showing the menu again    
        tui.wait_for_user_interaction()


if __name__ == "__main__":
    main()
