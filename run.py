import os
import random
import time

ROWS = 5
COLUMNS = 5
SEA = " "

def title():
    print("<====>  BATTLESHIP: Guadalcanal 1942  <====>\n")

def introduction_history_mode():
    """
    Provide background story for history mode
    """

    intro_history_mode = [
        "\nOn the night of November 14th 1942 Admiral William Halsey " +
        "took the command of a task force \nformed of battleships USS Washington, " +
        "USS South Dakota and 4 destroyers. The mission was to \nprotect Henderson " +
        "field from the Japanese Naval forces.\n"
        "\nThe Admiral has entrusted you with the command of the fleet. Sadly, after " +
        "the first \nencounter on November 13th, we have lost track of the enemy ships. " +
        "We know from intelligence \nreports Japanese Vice Admiral Kondo have a fleet of:\n"
        "\n1 Battle Cruiser, that occupy 3 cells\n"
        "2 Heavy Cruisers, that occupy 2 cells\n"
        "4 Destroyers that occupy 1 cell each"

    ]
    for i in intro_history_mode:
        print(i)
"""
def get_initial_battlefield():
    battlefield = []
    for y in range(ROWS):
        battlefield.append([])
        for x in range(COLUMNS):
            battlefield[y].append(SEA)
    return battlefield
"""
def main():
    title()
    introduction_history_mode()

main()