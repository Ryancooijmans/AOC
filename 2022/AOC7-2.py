import fileinput

beginNode = None
currentNode = None
totalcount = 0
dirsize = []
spacetofree = 0

class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.file = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent

    def add_file(self, file):
        self.file.append(file)

    def name_node(self, name):
        self.name = name

    def getindex(self, name):
        i = 0
        while i < len(self.children):
            if(self.children[i].name == name):
                return i
            i += 1
        return "getindex sucks"

def makenewnode(name):
    newnode = Node(name)
    currentNode.add_child(newnode)
    newnode.add_parent(currentNode)


def gettotalsize(dir, dirsize):
    sum = 0

    i = 0
    while i < len(dir.file):
        sum += int(dir.file[i][0])
        i += 1

    if(len(dir.children) > 0):
        j = 0
        while j < len(dir.children):
            size = gettotalsize(dir.children[j], dirsize)
            sum += size[0]
            j += 1

    dirsize.append(sum)
    print("Dir {} is: {}".format(dir.name, sum))
    return sum, dirsize

def getsmallestdir(dirarray):
    index = 0
    bestsize = max(dirarray)
    while index < len(dirarray):
        if(dirarray[index] >= spacetofree and dirarray[index] < bestsize):
            bestsize = dirarray[index]
        index += 1
    return bestsize

for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/AOC/2022/input7-1.txt"):
    line = line.strip()
    line = line.split(" ")

    if(line[0] == "$"):
        if(line[1] == "cd"):
            if(line[2] == "/"):
                if(beginNode == None):
                    beginNode = Node("begin")
                currentNode = beginNode
            
            elif(line[2] == ".."):
                currentNode = currentNode.parent

            else:
                currentNode = currentNode.children[currentNode.getindex(line[2])]

    elif(line[0] == "dir"):
        makenewnode(line[1])

    else:
        currentNode.add_file(line)

print(gettotalsize(beginNode, dirsize))
spacetofree = 30000000-(70000000-max(dirsize))
print(getsmallestdir(dirsize))