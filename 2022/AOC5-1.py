import fileinput

stack = [["T","D", "W", "Z", "V", "P"], 
["L", "S", "W", "V", "F", "J", "D"], 
["Z", "M", "L", "S", "V", "T", "B", "H"],
["R", "S", "J"],
["C", "Z", "B", "G", "F", "M", "L", "W"],
["Q", "W", "V", "H", "Z", "R", "G", "B"],
["V", "J", "P", "C", "B", "D", "N"],
["P", "T", "B", "Q"],
["H", "G", "Z", "R", "C"]]

def moveBox(moves, fromStack, toStack):
    fromStack -= 1
    toStack -= 1
    i = 0
    while i < moves:
        box = stack[fromStack][-1]
        stack[toStack].append(box)
        stack[fromStack].pop()
        i += 1        


for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input5-1.txt"):
    action = line.split()
    moves = int(action[1])
    fromStack = int(action[3])
    toStack = int(action[5])

    moveBox(moves, fromStack, toStack)

print([s[-1] for s in stack])