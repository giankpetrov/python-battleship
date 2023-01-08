import os
import random

ROWS = 5
COLUMNS = 5
SEA = " "

print("<====>  BATTLESHIP: Guadalcanal 1942  <====>\n")

def get_initial_battlefield():
    battlefield = []
    for y in range(ROWS):
        battlefield.append([])
        for x in range(COLUMNS):
            battlefield[y].append(SEA)
    return battlefield

def main():
    introduction()

main()