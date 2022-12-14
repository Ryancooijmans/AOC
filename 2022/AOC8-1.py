import fileinput
import numpy as np
grid = []

def treecheck():
    x = 0
    transgrid = []
    hiddentrees = []
    while x < len(grid):
        y = 0
        while y < len(grid[0]):
            if(treehidden(x,y,grid)):
                transgrid = np.array(grid)
                transgrid = transgrid.T.tolist()
                if(treehidden(y,x,transgrid)):
                    hiddentrees.append([x,y])

            y += 1
        x += 1
    return hiddentrees

def treehidden(x,y,array):
    i = x 
    if(x == 0 or x == len(array[x])-1):
        return False
    i -= 1
    while i >= 0:
        if(array[i][y] >= array[x][y]):
            i = x + 1
            while i < len(array[x]):
                if(array[i][y] >= array[x][y]):
                    return True
                i += 1
            return False
        i -= 1
    return False

for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/AOC/2022/input8-1.txt"):
    line = line.strip()
    array = list(line)
    grid.append(array)

gridlength = len(grid)
gridwidth = len(grid[0])
totaltrees = gridlength*gridwidth
print(totaltrees - len(treecheck()))