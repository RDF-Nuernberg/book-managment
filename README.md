# RDF Book Manager

Der RDF Book Manager ist eine einfache Buchverwaltung der einen Überblick über den Gesamtbestand aller Bücher sowie die verliehenen Exemplare geben soll. 

Außerdem soll über eine einfache Oberfläche, alle ausgeliehenen/vorhandenen Bücher aufgelistet und der Status (vorhanden/ausgeliehen) geändert werden können.


## Development

Die Softwarearchitektur ist an das drei Schichten Modell angelehnt.

- Datenzugriff / Repository 
- Logik / Service
- Anzeige / UI

Damit die drei Schichten auch vernünftig miteinander arbeiten können, muss ein gemeinsammes Datenmodell existieren wie Daten ausgetauscht werden.

### Datenmodell

Zu jedem Buch liegen folgende Informationen vor: isbn, titel, zugehöriges Fach, Stückzahl und die noch verfügbaren Bücher.

Intern werden einzelne Bücher aktuell als Dictionary mit folgenden *keys* gespeichert:

```python
{
    "isbn": str,               # eindeutige Buch-ID
    "title": str,              # Titel des Buches
    "categorie": str,          # Kategorie
    "total": int,              # Gesamtanzahl der Exemplare
    "available": int,          # Zurzeit verfügbare Bücher
}
``` 

Es muss jedoch noch evaluiert werden wie alle Bücher zusammengefasst werden:

- Als Liste mit Dictionaries
- Als geschachteltes Dictionary mit ISBN als Schlüssel(key).

### Datenspeicher 

Der bisherige Bücherbestand ist als CSV Datei `bestand.csv` gespeichert. Wer welches Buch ausgeliehen hat wird aktuell nicht digital erfasst.

Langfristig soll der Wechsel auf eine Datenbank als Speichermedium eingeplant werden.

Der Code zum Zugriff auf die Daten als CSV befindet sich im **Modul** `repo_csv.py`

### Logik

Die Logik Schicht soll die Kommunikation zwischen Datenzugriff und Anzeige übernehmen.
Außerdem sollen hier die Funktionen zur Verwaltung der Bücher implementiert werden.

WICHTIG: Hier kommt kein `input()` oder `print()` Befehl vor!

Aktuell befindet sich die Logik in der `main.py` Datei. 

### Oberfläche

Als Oberfläche wird in erster Iteration eine kleine TUI Anwendung realisiert. Ein wechsel auf eine grafische Oberfläche ist für die Zukunft geplant.

Der Code zur Oberfläche befindet sich im Modul `tui.py`


## Status

Folgende Teile wurden bereits umgesetzt.

- Datenzugriff (`repo_csv.py`)
- Oberfläche (`tui.py`)
- Die Grundlogik zur Menü Auswahl (`main.py`)

Weite Teile der Logik fehlen aber noch: (`management.py`)


# Guide zur Einarbeitung

Hier folgt eine kurzer Leitfaden zur Einarbeitung in das Projekt.

## Part 1: Setup
- Legen Sie sich einen GitHub Account an.
- Legen Sie einen Fork dieses Repositories an. (Grüner Button)
- Wechseln Sie dann zu Ihrem eigenen Fork und Klonen Sie das Projekt, damit sie lokal daran arbeiten können.

## Part 2: Einarbeiten
- Informieren Sie sich, mit Hilfe des Arbeitsblattes zum 3 Schichtenmodell.
- Machen Sie sich mit Hilfe eines LLMs oder Internetrecherche die Syntax des `match` Statements klar.
Wandeln Sie das `match` - Statement in `if`/ `elif` - Statements um. Welche Schreibweise finden Sie übersichtlicher?
- Arbeiten Sie sich in den bestehenden Code ein indem Sie die Funktionen in `tui.py` und `repo_csv.py` druchlesen und versuchen in eigenen Worten Ihren Banknachbarn zu erklären. (Jeder eine durchlesen und dem Nachbar erklären.)
- Bearbeiten Sie die Theorieeinheit zu Funktionen.

## Part 3: Verfollständigen
- Vervollständigen Sie das Programm indem Sie die Funktionen zur Logik des Programms ausprogrammieren.

## Part 4: Versionskontrolle
- Überprüfen Sie die bisherige Git Commit History.
- Machen Sie einen neuen Commit mit ihren Änderungen.
- Pushen Sie den Commit von ihrem lokalen main Branch auf das remote Repo (GitHub)
- Überprüfen Sie ob die Änderungen dort sichtbar sind.
