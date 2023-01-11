import os
import random
import time
import sys

ROWS = 5
COLUMNS = 5
SEA = " "
LINE_BREAK = "\n" + str("-" * 80) + "\n"

def print_slow(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.005)

def print_slow_menu(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.1)

def title():
    print("\n <====>  BATTLESHIP: Guadalcanal 1942  <====>")

def history_mode():
    title()
    introduction_history_mode()
    instructions_history_mode()


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

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("clr")

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
        "\n* If the grid is empty, it will be registered as a miss",
        "\n* The size of the grid and the amount of shells you have " +
        "will be determined by \n  the difficulty level you choose"
    ]
    clear_screen()
    title()
    print("\n *** INSTRUCTIONS ***")
    print(LINE_BREAK)
    for i in instructions:
        print_slow(i)
    print(LINE_BREAK)
    continue_key()

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
        menu_options()
        menu_selection = input("Please, choose an option: ")             
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