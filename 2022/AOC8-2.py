import fileinput
import numpy as np
grid = []

def treecheck():
    x = 0
    transgrid = []
    bestscene = 0
    while x < len(grid):
        y = 0
        while y < len(grid[0]):
            vis1 = treehidden(x,y,grid)
            transgrid = np.array(grid)
            transgrid = transgrid.T.tolist()
            vis2 = treehidden(y,x,transgrid)
            
            if(vis1*vis2 > bestscene):
                bestscene = vis1*vis2
            y += 1
        x += 1
    return bestscene

def treehidden(x,y,array):
    i = x 
    i -= 1
    treevis1 = 0
    treevis2 = 0
    
    while i >= 0:
        if(array[i][y] >= array[x][y]):
            treevis1 += 1
            break
        treevis1 += 1
        i -= 1
    
    i = x + 1
    while i < len(array[x]):
        if(array[i][y] >= array[x][y]):
            treevis2 += 1
            break
        treevis2 += 1
        i += 1

    return treevis1*treevis2

for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/AOC/2022/input8-1.txt"):
    line = line.strip()
    array = list(line)
    grid.append(array)

print(treecheck())