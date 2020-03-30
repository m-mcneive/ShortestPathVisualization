import pygame
from grid import Grid
import finder
import time
import sys


pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 840


cellWidth, cellHeight = 40, 40
cellMargin = 2
totalCellDimension = cellWidth + cellMargin

numCellsInRow = SCREEN_WIDTH // totalCellDimension

g = Grid(numCellsInRow)

#Vairbales to track where the user is in the cell selection process
startCell, targetCell = None, None
start = False
target = False
blocked = False
done = False
searched = False

#Final path list
lst = []

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
while True:
    #Creates the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))

    #Goes through every cell and sets the correct colors
    row = 0
    for x in range(cellMargin // 2, SCREEN_WIDTH, totalCellDimension):
        col = 0
        for y in range(cellMargin//2, SCREEN_HEIGHT, totalCellDimension):
            rect = pygame.Rect(x , y, cellHeight, cellWidth)
            pygame.draw.rect(screen, g.getColor(row, col), rect)
            col += 1
        row += 1
    pygame.display.update()



    ev = pygame.event.get()
        # proceed events
    for event in ev:

        #If red close button pressed in wondow, program exits
        if event.type == pygame.QUIT:
            sys.exit(0)

        # Down arrow used to move to next step
        # Step 1: Selecting start point
        # Step 2: Select target
        # Step 3: Select barriers
        # Step 4: Run algorithm
        if event.type == pygame.KEYDOWN:
            if not start:
                start = True
            elif not target:
                target = True
            elif not blocked:
                blocked = True

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            
            #Selects start cell and sets color to green
            if not start:
                #If a start cell has been selected, deselect the original
                if startCell:
                    g.setValue(startCell[0], startCell[1], 0)
                pos = pygame.mouse.get_pos()
                x = pos[0] // totalCellDimension
                y = pos[1] // totalCellDimension
                g.setValue(x, y, 1)
                startCell = (x, y)
                continue

            #Selects target cell and sets color to red
            elif not target:
                #If a target cell has been selected, deselect the original
                if targetCell:
                    g.setValue(targetCell[0], targetCell[1], 0)
                pos = pygame.mouse.get_pos()
                x = pos[0] // totalCellDimension
                y = pos[1] // totalCellDimension
                g.setValue(x, y, 2)
                targetCell = (x, y)
                continue

            #Selects barriers and sets them to black
            elif not blocked:
                pos = pygame.mouse.get_pos()
                x = pos[0] // totalCellDimension
                y = pos[1] // totalCellDimension
                g.setValue(x, y, 5)


        #Once all cells have been set, run the algorithm
        if start and target and blocked and not searched:
            print('searching\n\n')
            a, b = finder.dijkstra(g, startCell)
            currentCell = targetCell
            while not done:
                lst.append(b[currentCell])
                currentCell = lst[-1]
                if currentCell == startCell:
                    done = True
            lst.reverse()
            print(lst)
            searched = True
            
            
    #After the search, sets the final path to blue
    if searched:
        for ele in lst[1:]:
            g.setValue(ele[0], ele[1], 4)
        
        


            
