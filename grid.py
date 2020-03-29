
class Grid:

    #0 = unused square, white   (255, 255, 255)
    #1 = starting square, green    (0, 255, 0)
    #2 = target square, red     (255, 0, 0)
    #3 = searched squares, yellow   (255, 255, 0)
    #4 final path, blue     (0, 0, 255)
    


    def __init__(self, size):
        self.grid = []
        self.size = size
        temp = []
        for i in range(size):
            for j in range(size):
                temp.append(0)
            self.grid.append(temp)
            temp = []

    def getColor(self, x, y):
        if self.grid[x][y] == 0:
            return (255, 255, 255)
        elif self.grid[x][y] == 1:
            return (0, 255, 0)
        elif self.grid[x][y] == 2:
            return (255, 0, 0)
        elif self.grid[x][y] == 3:
            return (255, 255, 0)
        else:
            return (0, 0, 255)

    def setValue(self, x, y, val):
        self.grid[x][y] = val

    def getRow(self, row):
        return self.grid[row]


    def getNeighbors(self, x, y):

        if (0 < x < self.size - 1) and (0 < y < self.size - 1):
            return {(x, y + 1): 10, (x, y - 1): 10, (x + 1, y): 10, (x - 1, y): 10}

        if x == 0:
            if y == 0:
                return {(0, 1): 10, (1, 0): 10}
            elif y == self.size - 1:
                return {(0, y - 1): 10, (1, y): 10}
            else:
                return {(0, y - 1): 10, (0, y + 1): 10, (1, y): 10}
        elif x == self.size - 1:
            if y == 0:
                return {(x, 1): 10, (x - 1, 0): 10}
            elif y == self.size - 1:
                return {(x, y - 1): 10, (x - 1, y): 10}
            else:
                return {(x, y - 1): 10, (x, y + 1): 10, (x - 1, y): 10}
        else:
            if y == 0:
                return {(x - 1, y): 10, (x + 1, y): 10, (x, y + 1): 10}
            elif y == self.size - 1:
                return {(x - 1, y): 10, (x + 1, y): 10, (x, y - 1): 10}
            