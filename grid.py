
class Grid:

    #0 = unused square, white   (255, 255, 255)
    #1 = starting square, green    (0, 255, 0)
    #2 = target square, red     (255, 0, 0)
    #3 = searched squares, yellow   (255, 255, 0)
    #4 final path, blue     (0, 0, 255)
    #5 blocked square     (0, 0, 0)
    


    def __init__(self, size):
        self.grid = []
        self.size = size
        temp = []
        #Creates 2d array with all values set to 0
        for i in range(size):
            for j in range(size):
                temp.append(0)
            self.grid.append(temp)
            temp = []

    #returns rgb color based on value in array (colors listed above)
    def getColor(self, x, y):
        if self.grid[x][y] == 0:
            return (255, 255, 255)
        elif self.grid[x][y] == 1:
            return (0, 255, 0)
        elif self.grid[x][y] == 2:
            return (255, 0, 0)
        elif self.grid[x][y] == 3:
            return (255, 255, 0)
        elif self.grid[x][y] == 5:
            return (0, 0, 0)
        else:
            return (0, 0, 255)

    #Sets numerical value in array (value meanings listed above)
    def setValue(self, x, y, val):
        self.grid[x][y] = val

    #Returns row of the array
    def getRow(self, row):
        return self.grid[row]


    #Returns neighbors of a cell based on position and distance values, diagonal values found with Pythagorean Theorem
    def getNeighbors(self, x, y):
        if (0 < x < self.size - 1) and (0 < y < self.size - 1):
            return {(x, y + 1): 40, (x, y - 1): 40, (x + 1, y): 40, (x - 1, y): 40, (x - 1, y - 1): 56, (x - 1, y + 1): 56, (x + 1, y - 1): 56, (x + 1, y + 1): 56}

        if x == 0:
            if y == 0:
                return {(0, 1): 40, (1, 0): 40, (1, 1): 56}
            elif y == self.size - 1:
                return {(0, y - 1): 40, (1, y): 40, (1, y - 1): 56}
            else:
                return {(0, y - 1): 40, (0, y + 1): 40, (1, y): 40, (1, y - 1): 56, (1, y + 1): 56}
        elif x == self.size - 1:
            if y == 0:
                return {(x, 1): 40, (x - 1, 0): 40, (x - 1, 1): 56}
            elif y == self.size - 1:
                return {(x, y - 1): 40, (x - 1, y): 40, (x - 1, y - 1): 56}
            else:
                return {(x, y - 1): 40, (x, y + 1): 40, (x - 1, y): 40, (x - 1, y - 1): 56, (x - 1, y + 1): 56}
        else:
            if y == 0:
                return {(x - 1, y): 40, (x + 1, y): 40, (x, y + 1): 40, (x - 1, 1): 56, (x + 1, 1): 56}
            elif y == self.size - 1:
                return {(x - 1, y): 40, (x + 1, y): 40, (x, y - 1): 40, (x - 1, y - 1): 56, (x + 1, y - 1): 56}
            