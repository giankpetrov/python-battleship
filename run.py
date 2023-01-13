import os
import random
import time
import sys

ROWS = 5
COLUMNS = 5
SEA = " "
DESTRUCTOR = "D"  # One Cell
HEAVY = "H"  # Two cells
CRUISER = "C"  # Cells
SHOT_MISSED = "-"
GOOD_SHOOT = "*"
STARTING_SHELLS = 25
P_1 = "Player 1"
P_2 = "Player 2"
LINE_BREAK = "\n" + str("-" * 80) + "\n"

def title():
    """
    Prints the title of the game
    """
    print("\n <====>  BATTLESHIP: Guadalcanal 1942  <====>")

def clear_screen():
    """
    Clears the terminal
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("clr")

def print_slow(str):
    """
    Prints each char slowly
    """
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.005)

def continue_key():
    """
    Allows the user to continue by pressing enter
    """
    input("\nPress Enter to continue...")

def continue_key_history():
    """
    Allows the user to continue by pressing enter
    """
    input("\nPress Enter to reload and continue...")

def STARTING_BATTLEFIELD():
    """
    Creates an array that will work as the board for the game
    """
    battlefield = []
    for y in range(ROWS):
        # We amend the Array adding the rows
        battlefield.append([])
        for x in range(COLUMNS):
            # We add a cell within the row. its "SEA" by default.
            battlefield[y].append(SEA)
    return battlefield

def INCREMENT(letter):
    """
    Function that increments the letter +1 in ASCII
    """
    return chr(ord(letter)+1)

def print_horizontal_separator():
    """
    Function that prints an horizontal line to separate text or fields of the game
    """
    for _ in range(COLUMNS+1):
        print("+---", end="")
    print("+")

def print_line_with_numbers():
    """
    Prints the last line of the board with numbers in increments
    """
    print("|   ", end="")
    for x in range(COLUMNS):
        print(f"| {x+1} ", end="")
    print("|")

def if_sea(x, y, battlefield):
    """
    Let us know if there is SEA in the coordinates
    """
    return battlefield[y][x] == SEA
    
def history_mode():
    title()
    introduction_history_mode()
    instructions_history_mode()
    game()


def introduction_history_mode():
    """
    Provide background story for history mode
    """

    intro_history_mode = [
        "On the night of November 14th 1942 Admiral William Halsey " +
        "took the command of \na task force formed of battleships USS Washington, " +
        "USS South Dakota and 4 \ndestroyers. The mission: Protect Henderson " +
        "field from the Japanese Naval forces.\n"
        "\nThe Admiral has entrusted you with the command of the fleet. Sadly, after " +
        "the \nfirst encounter on November 13th, we have lost track of the enemy ships. " +
        "We know \nfrom intelligence reports Japanese Vice Admiral Kondo have a fleet of:\n"
        "\n1 Battle Cruiser, that occupy 3 cells\n"
        "2 Heavy Cruisers, that occupy 2 cells\n"
        "3 Destroyers that occupy 1 cell each\n"
    ]
    print(LINE_BREAK)
    for i in intro_history_mode:
        print_slow(i)
    print(LINE_BREAK)
    continue_key()

def continue_key():
    input("Press Enter to continue...")
    

def instructions_history_mode():
    """
    Intructions to play the game
    """

    instructions = [
        "You must input two coordinates in order to select the" +
        "grid you want to fire upon:\n" +
        "\n1. Select the grid ROW by choosing a NUMBER" +
        "\n2. Select the grid COLUMN by choosing a LETTER\n" +
        "\n* If a ship is within the grid coordinates you have selected, " +
        "a hit will be \nregistered.",
        "\n* If the grid is empty, it will be registered as a miss"

    ]
    clear_screen()
    title()
    print("\n *** INSTRUCTIONS ***")
    print(LINE_BREAK)
    for i in instructions:
        print_slow(i)
    print(LINE_BREAK)
    continue_key()

def game():
    shells = 15
    enemy_ships = 5
    gamefield = get_initial_battlefield()
    gamefield = print_ships()
    


def get_initial_battlefield():
    battlefield = []
    for y in range(ROWS):
        battlefield.append([])
        for x in range(COLUMNS):
            battlefield[y].append(SEA)
    return battlefield

def horizontal_separator():
    for _ in range(COLUMNS+1):
        print("+---", end="")
    print("+")

def numbers_line():
    print("|   ", end="")
    for x in range(COLUMNS):
        print(f"| {x+1} ", end="")
    print("|")

def print_battlefield():
    letra = "A"
    for y in range(ROWS):
        horizontal_separator()
        print(f"| {letra} ", end="")
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            print(f"| {valor_real} ", end="")
        letra = incrementar_letra(letra)
        print("|",)  # Salto de línea
    horizontal_separator()
    numbers_line()
    horizontal_separator()


def menu_options():
    print("1. Play")
    print("2. About")
    print("3. Exit")

def menu():
    while True:
        title()
        print(LINE_BREAK)
        menu_options()
        menu_selection = input("\nPlease, choose an option: ")            
        if menu_selection == "1":
            clear_screen()
            history_mode()
        elif menu_selection == "2":
            about()
        elif menu_selection == "3":
            exit()
        else:
            print_slow_menu("\n *** Please, select a number from the menu ***")
            time.sleep(2)
            clear_screen()

menu()