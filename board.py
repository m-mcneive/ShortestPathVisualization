import pygame
from grid import Grid
import finder
import time


pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 840

cellWidth, cellHeight = 40, 40
cellMargin = 2
totalCellDimension = cellWidth + cellMargin

numCellsInRow = SCREEN_WIDTH // totalCellDimension

g = Grid(numCellsInRow)
print(g.getNeighbors(19, 4))

startCell, targetCell = None, None
start = False
target = False
done = False
searched = False


lst = []

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
while True:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
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

        if event.type == pygame.KEYDOWN:
            if not start:
                start = True
                continue
            elif not target:
                target = True
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            
            if not start:
                pos = pygame.mouse.get_pos()
                x = pos[0] // totalCellDimension
                y = pos[1] // totalCellDimension
                g.setValue(x, y, 1)
                startCell = (x, y)
                print(g.getNeighbors(x, y))
            elif not target:
                pos = pygame.mouse.get_pos()
                x = pos[0] // totalCellDimension
                y = pos[1] // totalCellDimension
                g.setValue(x, y, 2)
                targetCell = (x, y)

        if start and target and not searched:
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
            
            

    if searched:
        for ele in lst[1:]:
            g.setValue(ele[0], ele[1], 4)
        
    
time.sleep(3)

            
