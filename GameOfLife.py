import pygame
import os
import sys

width, height = 800, 800
size = (width, height)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
screen.fill(BLACK)


startCells = [[]]


cols = 40
rows = 40

dead = 0
alive = 1

cellSize = int(height/rows)


def drawGrid(cols, rows):
    #print(rows)
    for x in range(0, width, cellSize):
        for y in range(0, height, cellSize):
            #print("column", x, "row", y)
            border = pygame.Rect(x, y, cellSize, cellSize)
            pygame.draw.rect(screen, GREY, border, 1)

def drawCells(grid):
    for i in range(cols):
        for j in range(rows):
            cellCol = i * cellSize
            cellRow = j * cellSize
            if grid[j][i] == alive:
                #drawGrid(cols, rows)
                cellAlive = pygame.Rect(cellCol, cellRow, cellSize, cellSize)
                pygame.draw.rect(screen, WHITE, cellAlive)
            else:
                #drawGrid(cols, rows)
                cellDead = pygame.Rect(cellCol, cellRow, cellSize, cellSize)
                pygame.draw.rect(screen, BLACK, cellDead)








sample = [[1,2],[3,4]]

def arrayPrint(arr):
    for row in arr:
        print(row)
    print()




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

def gen(n):
    count = 0
    while count <= n:
        if count == 0:
            current = buildStart()
        else:
            current = evolve(current)
        count += 1
    return current


startCells = [
                [0,1], [1,2], [2,0], [2,1], [2,2],
                [2, 15], [2,16], [2,17]
            ]


def main():
    runCount = 0
    while True:

        #DOES NOT RUN drawGrid() BECAUSE OF TIME INEFFICIENCY

        #drawGrid(cols, rows)
        drawCells(gen(runCount))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(6)
        runCount +=1

main()
        