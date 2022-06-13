import pygame
import os



while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

sample = [[1,2],[3,4]]

def arrayPrint(arr):
    for row in arr:
        print(row)
    print()


startCells = [[]]


cols = 10
rows = 10

dead = 0
alive = 1


def make2DArray(cols, rows):
    array = []
    for i in range(rows):
        array.append([])
        for j in range(cols):
            array[i].append(0)
    return array


def buildStart():

    grid = make2DArray(cols, rows)
    for i in range(cols):
        for j in range(rows):
            if [i,j] in startCells:
                grid[j][i] = alive
            else:
                grid[j][i] = dead

    return grid




def checkLeft(i, j):
    return i == 0

def checkRight(i, j):
    return i == cols - 1

def checkTop(i, j):
    return j == 0

def checkBottom(i, j):
    return j == rows - 1

def buildNext(grid):
    tempArray = make2DArray(cols, rows)
    #add +1 to all nearby cells

        #check if edge
    for i in range(cols):
        for j in range(rows):
            isLeftEdge = False
            isRightEdge = False
            isTopEdge = False
            isBottomEdge = False
            if grid[j][i] == alive:
                
                if not checkLeft(i,j):
                    tempArray[j][i-1] += 1
                    if not checkTop(i,j):
                        tempArray[j-1][i-1] += 1
                    if not checkBottom(i,j):
                        tempArray[j+1][i-1] += 1
                
                if not checkRight(i,j):
                    tempArray[j][i+1] += 1
                    if not checkTop(i,j):
                        tempArray[j-1][i+1] += 1
                    if not checkBottom(i,j):
                        tempArray[j+1][i+1] += 1

                if not checkTop(i,j):
                    tempArray[j-1][i] += 1
                if not checkBottom(i,j):
                    tempArray[j+1][i] += 1
    return tempArray
            
            
def evolve(grid):
    tempArray = buildNext(grid)
    nextGrid = make2DArray(cols, rows)
    for i in range(cols):
        for j in range(rows):

            nextGrid[j][i] = dead

            #stay alive
            if grid[j][i] == alive:
                if tempArray[j][i] >= 2 and tempArray[j][i] <= 3:
                    nextGrid[j][i] = alive
            
            #born
            elif grid[j][i] == dead:
                if tempArray[j][i] == 3:
                    nextGrid[j][i] = alive
            
    return nextGrid

def run(gens):
    count = 0
    while count < gens:
        if count == 0:
            current = buildStart()
        else:
            current = evolve(current)
        count += 1
    return current


startCells = [[0,1], [1,2], [2,0], [2,1], [2,2]]

startGrid = buildStart()

arrayPrint(run(1))
arrayPrint(run(2))
arrayPrint(run(3))
arrayPrint(run(4))
arrayPrint(run(5))
arrayPrint(run(6))