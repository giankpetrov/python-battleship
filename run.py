import os
import random

ROWS = 5
COLUMNS = 5
SEA = " "

def get_initial_battlefield():
    battlefield = []
    for y in range(ROWS):
        battlefield.append([])
        for x in range(COLUMNS):
            battlefield[y].append(SEA)
    return battlefield