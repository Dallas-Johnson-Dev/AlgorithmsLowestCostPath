"""
Python Program written to find the lowest cost path from the bottom row of a grid to the top.
Written by Dallas Johnson
Requires one input which is the size of the grid. The grid is an N x N size grid, so only one positive integer is needed.
"""

import random
from sys import argv


class GridTile:
    value = None
    cache = None

    def __init__(self):
        self.value = random.randrange(1, 20)

    def __add__(self, other):
        return self.value + other.value


def main():
    if len(argv) < 1:
        print("Usage: python3 lowestcost.py size")
        print("Grid size needed for algorithm to run on.")
        return
    grid = buildGrid(4)
    print("our answer should be: ")
    print(findLowestPath(grid,0,0,4))
    print(str(grid))


def buildGrid(size):
    algorithmgrid = [[0 for x in range(size)] for x in range(size)]
    for x in range(0, size):
        for y in range(0, size):
            algorithmgrid[x][y] = GridTile()
    return algorithmgrid


def findLowestPath(grid,x,y,size):
    if y == size:
        return
    lowestx = x
    lowestvalue = grid[x][y].value
    for i in range(0,size-1):
        if grid[i+1][y].value < lowestvalue:
            lowestvalue = grid[i+1][y].value
            lowestx = i+1
    else:
        return lowestvalue + solveLowestPath(grid, lowestx, y+1, size)


def solveLowestPath(grid, x, y, size):
    lowestValue = grid[x][y].value
    lowestx = x
    if x-1 in range(-1,size):
        if grid[x-1][y].value < lowestValue:
            lowestValue = grid[x][y].value
            lowestx = x-1
    if x+1 in range(-1,size):
        if grid[x+1][y].value < lowestValue:
            lowestValue = grid[x+1][y].value
            lowestx = x+1
    if y+1 == size:
        return lowestValue
    else:
        return lowestValue + solveLowestPath(grid, lowestx, y+1, size)

def printGrid(gridToPrint, size):
    for x in range(0,size):
        print("\n")
        for y in range(0,size):
            print(gridToPrint[x][y].value)


if __name__ == "__main__":
    main()
