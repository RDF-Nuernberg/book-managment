import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def display_list_of_books(list_of_books):
    """prints book information from a list of dictionaries"""
    table = Table(title="Book List", show_header=True, header_style="bold magenta")
    table.add_column("ISBN", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Categorie", style="yellow")
    table.add_column("Total", style="blue")
    table.add_column("Available", style="bright_green")
    
    for book in list_of_books:
        table.add_row(
            str(book.get('isbn', '')),
            str(book.get('title', '')),
            str(book.get('categorie', '')),
            str(book.get('total', '')),
            str(book.get('available', '')),
        )
    console.print(table)

def clear_screen():
    """clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """displays the main menu options"""
    clear_screen()
    menu_panel = Panel("""
[bold cyan]Book Management System[/bold cyan]

[green]1.[/green] View all books
[green]2.[/green] Show available books
[green]3.[/green] Show borrowed books
[green]4.[/green] Add a book
[green]5.[/green] Remove a book
[green]6.[/green] Borrow a book
[green]7.[/green] Return a book
[green]0.[/green] Exit program
""", title="Menu", border_style="blue")
    console.print(menu_panel)


def display_error(message):
    """displays an error message"""
    console.print(Panel(f"{message}", title="Error", border_style="red", style="bold red"))

def display_info(message):
    """displays a general message"""
    console.print(Panel(f"{message}", title="Info", border_style="blue", style="bold blue"))

def get_user_choice():
    """gets the user's menu choice"""
    while True:
        try:
            choice = int(Prompt.ask("Please select an option", choices=["1", "2", "3", "4", "5", "6", "7", "0"]))
            return choice
        except ValueError:
            display_error("Please enter a number between 1 and 5")

def get_book_details_from_user():
    """prompts the user for book details and returns a book dictionary"""
    console.print("\n[bold cyan]Enter Book Details[/bold cyan]")
    isbn = Prompt.ask("[yellow]Enter ISBN[/yellow]")
    titel = Prompt.ask("[yellow]Enter Title[/yellow]")
    fach = Prompt.ask("[yellow]Enter Subject[/yellow]")
    while True:
        try:
            gesamt = int(Prompt.ask("[yellow]Enter Total Copies[/yellow]"))
            break
        except ValueError:
            display_error("Please enter a valid number for Total Copies")
    
    return {
        "isbn": isbn,
        "title": titel,
        "categorie": fach,
        "total": gesamt,
        "available": gesamt
    }

def get_book_name_from_user():
    """prompts the user for a book name and returns it"""
    return Prompt.ask("\n[yellow]Enter the name of the book to search[/yellow]")


def wait_for_user_interaction():
    console.print("\n[Drücke Enter um fortzufahren...]")
    input()