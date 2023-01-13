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
    
def coordinates_in_range(x, y):
    """
    Let us know if the coordinates selected are within the range 
    of the initial array for the battlefield
    """
    return x >= 0 and x <= COLUMNS-1 and y >= 0 and y <= ROWS-1

def print_ships(battlefield, ships_amount, player):
    """
    Base on initial amount of ships, fills the array with the ships
    in their respective corrdenates
    """
    ships_one_cell = ships_amount-3
    ships_two_vertical_cells = ships_amount-5
    ships_two_horizontal_cells = ships_amount-4
    if player == P_1:
        print_slow("Placing ships for player 1 ")
    else:
        print_slow("Placing Ships for player 2 ")
    print_slow(f"\nOne cell ships: {ships_one_cell}\nTwo cells vertically ships: {ships_two_vertical_cells}\nTwo cells horizontally ships: {ships_two_horizontal_cells}\nTotal ships: {ships_one_cell+ships_two_vertical_cells+ships_two_horizontal_cells}\n")
    # First we put the 2 cells ships for better acommodation
    battlefield = print_ships_two_cells_horizontally(
        ships_two_horizontal_cells, HEAVY, battlefield)
    battlefield = print_ships_two_cells_vertically(
        ships_two_vertical_cells, CRUISER, battlefield)
    battlefield = print_ships_one_cell(ships_one_cell, DESTRUCTOR, battlefield)
    return battlefield

def print_ships_history(battlefield, ships_amount, player):
    """
    Base on initial amount of ships, fills the array with the ships
    in their respective corrdenates
    """
    ships_one_cell = ships_amount-3
    ships_two_vertical_cells = ships_amount-5
    ships_two_horizontal_cells = ships_amount-4
    print_slow("The air force have identify the following ships:\n")
    print_slow(f"\nOne cell ships: {ships_one_cell}\nTwo cells vertically ships: {ships_two_vertical_cells}\nTwo cells horizontally ships: {ships_two_horizontal_cells}\nTotal ships: {ships_one_cell+ships_two_vertical_cells+ships_two_horizontal_cells}\n")
    # First we put the 2 cells ships for better acommodation
    battlefield = print_ships_two_cells_horizontally(
        ships_two_horizontal_cells, HEAVY, battlefield)
    battlefield = print_ships_two_cells_vertically(
        ships_two_vertical_cells, CRUISER, battlefield)
    battlefield = print_ships_one_cell(ships_one_cell, DESTRUCTOR, battlefield)
    return battlefield

def RANDOM_X():
    """
    Select a random number within the number of colums
    """
    return random.randint(0, COLUMNS-1)

def RANDOM_Y():
    """
    Select a random number within the number of rows
    """
    return random.randint(0, ROWS-1)

def print_ships_one_cell(quantity, ship_type, battlefield):
    """
    Function to place one cell ships on the array if the place is fill with SEA
    """
    ship_placed = 0
    while True:
        x = RANDOM_X()
        y = RANDOM_Y()
        if if_sea(x, y, battlefield):
            battlefield[y][x] = ship_type
            ship_placed += 1
        if ship_placed >= quantity:
            break
    return battlefield

def print_ships_two_cells_horizontally(quantity, ship_type, battlefield):
    """
    Function to place two cells ships horizontally
    starting from X and following by X+1 as the next cell
    """
    ship_placed = 0
    while True:
        x = RANDOM_X()
        y = RANDOM_Y()
        x2 = x+1
        if (coordinates_in_range(x, y) and coordinates_in_range(x2, y) and
                if_sea(x, y, battlefield) and if_sea(x2, y, battlefield)):
                # We add extra indentation to the conditions as per PEP8
            battlefield[y][x] = ship_type
            battlefield[y][x2] = ship_type
            ship_placed += 1
        if ship_placed >= quantity:
            break
    return battlefield

def print_ships_two_cells_vertically(quantity, ship_type, battlefield):
    """
    Function to place two cells ships vertically
    starting from y and following by y+1 as the next cell
    """
    ship_placed = 0
    while True:
        x = RANDOM_X()
        y = RANDOM_Y()
        y2 = y+1
        if (coordinates_in_range(x, y) and coordinates_in_range(x, y2) and 
                if_sea(x, y, battlefield) and if_sea(x, y2, battlefield)):
                # We add extra indentation to the conditions as per PEP8
            battlefield[y][x] = ship_type
            battlefield[y2][x] = ship_type
            ship_placed += 1
        if ship_placed >= quantity:
            break
    return battlefield

def print_shells_left(shells_left, player):
    print(f"Remaining shells for {player}: {shells_left}")

def print_shells_left_history(shells_left, player):
    print(f"We still have {shells_left} shells left")

def print_battlefield(battlefield, show_ships, player):
    print(f"This is the field for: {player}")
    letter = "A"
    for y in range(ROWS):
        print_horizontal_separator()
        print(f"| {letter} ", end="")
        for x in range(COLUMNS):
            CELL = battlefield[y][x]
            real_value = CELL
            if not show_ships and real_value != SEA and real_value != SHOT_MISSED and real_value != GOOD_SHOOT:
                real_value = " "
            print(f"| {real_value} ", end="")
        letter = INCREMENT(letter)
        print("|",)  # Line break
    print_horizontal_separator()
    print_line_with_numbers()
    print_horizontal_separator()

def print_battlefield_history(battlefield, show_ships, player):
    print(f"The radar is picking up the following signal")
    letter = "A"
    for y in range(ROWS):
        print_horizontal_separator()
        print(f"| {letter} ", end="")
        for x in range(COLUMNS):
            CELL = battlefield[y][x]
            real_value = CELL
            if not show_ships and real_value != SEA and real_value != SHOT_MISSED and real_value != GOOD_SHOOT:
                real_value = " "
            print(f"| {real_value} ", end="")
        letter = INCREMENT(letter)
        print("|",)  # Line break
    print_horizontal_separator()
    print_line_with_numbers()
    print_horizontal_separator()

def request_coordinates(player):
    print(f"Requesting coordinates to {player}")
    # Infinite loop until a correct option its choosen
    y = None
    x = None
    while True:
        letter_row = input(
            "\nChoose a letter from the board to indicate the ROW: ")
        # We need a letter of 1 character, if not we continue to ask
        if len(letter_row) != 1:
            print_slow("\n *** You should select a valid option *** ")
            continue
        # Convert the input into a upper case first
        letter_row = letter_row.upper()
        # We convert the input into ASCII, A = 65 B= 66 etc we substrac 65 so A = 0
        y = ord(letter_row) - 65
        # Check if it is within the scope
        if coordinates_in_range(0, y):
            break
        else:
            print("\nInvalid Row")
    # Same for columns
    while True:
        try:
            x = int(input("\nChoose a number from the board to indicate the Column: "))
            if coordinates_in_range(x-1, 0):
                x = x-1 
                break
            else:
                print("\n *** The number is not valid ***")
        except:
            print("\n *** Please, choose a valid number")
    return x, y

def request_coordinates_history(player):
    print(f"Requesting coordinates Captain")
    # Infinite loop until a correct option its choosen
    y = None
    x = None
    while True:
        letter_row = input(
            "\nChoose a letter from the board to indicate the ROW: ")
        # We need a letter of 1 character, if not we continue to ask
        if len(letter_row) != 1:
            print_slow("\n *** You should select a valid option *** ")
            continue
        # Convert the input into a upper case first
        letter_row = letter_row.upper()
        # We convert the input into ASCII, A = 65 B= 66 etc we substrac 65 so A = 0
        y = ord(letter_row) - 65
        # Check if it is within the scope
        if coordinates_in_range(0, y):
            break
        else:
            print("\nInvalid Row")
    # Same for columns
    while True:
        try:
            x = int(input("\nChoose a number from the board to indicate the Column: "))
            if coordinates_in_range(x-1, 0):
                x = x-1 
                break
            else:
                print("\n *** The number is not valid ***")
        except:
            print("\n *** Please, choose a valid number")
    return x, y

def shoot(x, y, battlefield) -> bool:
    if if_sea(x, y, battlefield):
        battlefield[y][x] = SHOT_MISSED
        return False
    elif battlefield[y][x] == SHOT_MISSED or battlefield[y][x] == GOOD_SHOOT:
        return False
    else:
        battlefield[y][x] = GOOD_SHOOT
        return True

def oponent_current_player(player):
    if player == P_1:
        return P_2
    else:
        return P_1

def are_all_ships_sunk(battlefield):
    for y in range(ROWS):
        for x in range(COLUMNS):
            CELL = battlefield[y][x]
            # if its not SEA, GOOD SHOT or SHOT MISSED means there is still a ship alive
            if CELL != SEA and CELL != GOOD_SHOOT and CELL != SHOT_MISSED:
                return False
    # if True we have been through all the array or battlefiel and all ships are sunk
    return True

def VICTORY(player):
    """
    Print victory message
    """
    print(f"End of game\n{player} is the winner")

def VICTORY_history(player):
    """
    Print victory message
    """
    print(f"We did it Captain, we defend Henderson field")

def DEFEAT(player):
    print(
        f"End of game\n{player} has lost. No more shells remain")

def DEFEAT_history(player):
    print(
        f"Captain we should retreat. We need more shells to keep shooting.")

def print_field_with_ships(field_p1, field_p2):
    print("Showing fields with all ships on the battlefield from both players:")
    print_battlefield(field_p1, True, P_1)
    print_battlefield(field_p2, True, P_2)

def print_field_with_ships_history(field_p2):
    print("Final radar report will show the battleship with all ships:")
    print_battlefield_history(field_p2, True, P_2)

def MULTIPLAYER():
    clear_screen()
    shells_left_j1 = STARTING_SHELLS
    shells_left_j2 = STARTING_SHELLS
    ships_amount = 6
    field_p1, field_p2 = STARTING_BATTLEFIELD(), STARTING_BATTLEFIELD()
    field_p1 = print_ships(
        field_p1, ships_amount, P_1)
    field_p2 = print_ships(
        field_p2, ships_amount, P_2)
    current_turn = P_1
    print_slow("\n*** Get ready ***")
    continue_key()
    clear_screen()
    title()
    print("\n======================")
    while True:
        print(f"Current turn > {current_turn} \n")
        shells_left = shells_left_j2
        if current_turn == P_1:
            shells_left = shells_left_j1
        print_shells_left(shells_left, current_turn)
        oponent_field = field_p1
        if current_turn == P_1:
            oponent_field = field_p2
        print_battlefield(oponent_field, False,
                        oponent_current_player(current_turn))
        x, y = request_coordinates(current_turn)
        correct = shoot(x, y, oponent_field)
        #decrease shells depending on current turn
        if current_turn == P_1:
            shells_left_j1 -= 1
        else:
            shells_left_j2 -= 1

        print_battlefield(oponent_field, False,
                        oponent_current_player(current_turn))
        if correct:
            print_slow("\nYou hit a ship")
            continue_key()
            clear_screen()
            if are_all_ships_sunk(oponent_field):
                VICTORY(current_turn)
                print_field_with_ships(field_p1, field_p2)
                break
        else:
            print_slow("\nYou miss\n")
            continue_key()
            clear_screen()
            if shells_left-1 <= 0:
                DEFEAT(current_turn)
                print_field_with_ships(field_p1, field_p2)
                break
            current_turn = oponent_current_player(current_turn)
"""
HISTORY MODE
"""

def history_mode():
    title()
    introduction_history_mode()
    instructions_history_mode()
    game_history_mode()

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
        "\n1 Battle Cruiser, that occupy 2 cells\n"
        "2 Heavy Cruisers, that occupy 2 cells\n"
        "3 Destroyers that occupy 1 cell each\n"
    ]
    print(LINE_BREAK)
    for i in intro_history_mode:
        print_slow(i)
    print(LINE_BREAK)
    continue_key()

def instructions_history_mode():
    """
    Intructions to play the game
    """

    instructions = [
        "You must input two coordinates in order to select the " +
        "grid you want to fire upon:\n" +
        "\n1. Select the grid ROW by choosing a LETTER" +
        "\n2. Select the grid COLUMN by choosing a NUMBER\n" +
        "\n* If a ship is within the grid coordinates you have selected, " +
        "a hit will be \nregistered and you will continue your turn.",
        "\n* If the grid is empty, it will be registered as a miss."
    ]
    clear_screen()
    title()
    print("\n *** INSTRUCTIONS ***")
    print(LINE_BREAK)
    for i in instructions:
        print_slow(i)
    print(LINE_BREAK)
    continue_key()

def game_history_mode():
    """
    Function that execute battleship game on the Player vs Computer mode
    """
    clear_screen()
    title()
    print("\n======================")
    shells_left_j1 = 2
    ships_amount = 6
    field_p2 = STARTING_BATTLEFIELD()
    field_p2 = print_ships_history(
        field_p2, ships_amount, P_2)
    current_turn = P_1
    print_slow("\n*** Get ready ***\n")
    continue_key()
    clear_screen()
    title()
    print("\n======================")
    while True:
        print(f"\nCaptain where should we shoot?")
        if current_turn == P_1:
            shells_left = shells_left_j1
        print_shells_left_history(shells_left, current_turn)
        if current_turn == P_1:
            oponent_field = field_p2
        print_battlefield_history(oponent_field, False,
                        oponent_current_player(current_turn))
        x, y = request_coordinates_history(current_turn)
        correct = shoot(x, y, oponent_field)
        #decrease shells depending on current turn
        if current_turn == P_1:
            if shells_left_j1 == 0:
                DEFEAT_history(current_turn)
                print_field_with_ships_history(field_p2)
                continue_key()
                break
            shells_left_j1 -= 1
        print_battlefield_history(oponent_field, False,
                        oponent_current_player(current_turn))
        if correct:
            print_slow("\nYou hit them Captain... Well done")
            continue_key_history()
            clear_screen()
            if are_all_ships_sunk(oponent_field):
                VICTORY_history(current_turn)
                print_field_with_ships_history(field_p2)
                break
        else:
            print_slow("\nWe miss captain\n")
            print_slow("We should try different coordinates")
            continue_key_history()
            clear_screen()
            if shells_left-1 <= 0:
                DEFEAT_history(current_turn)
                print_field_with_ships_history(field_p2)
                continue_key()
                break
            current_turn = P_1
    clear_screen()

def about():
    """
    Prints a brief credit to the autor
    """
    title()
    print(LINE_BREAK)
    print_slow("This game was developed by Gianncarlo Ciampaglia")
    print(LINE_BREAK)
    print("You will go back to main menu in 4 seconds...")

def menu_options():
    """
    Prints all the options from the main menu
    """
    print("1. History Mode")
    print("2. Multiplayer")
    print("3. About")
    print("4. Exit")

def menu():
    """
    Infinite loop that execute the functions according to the
    selection made by the user.
    """
    while True:
        title()
        print(LINE_BREAK)
        menu_options()
        menu_selection = input("\nPlease, choose an option: ")            
        if menu_selection == "1":
            clear_screen()
            history_mode()
        elif menu_selection == "2":
            MULTIPLAYER()
        elif menu_selection == "3":
            clear_screen()
            about()
            time.sleep(5)
            clear_screen()
            menu()
        elif menu_selection == "4":
            exit()
        else:
            print_slow("\n *** Please, select a number from the menu ***")
            time.sleep(2)
            clear_screen()

menu()