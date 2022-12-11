import fileinput

totalInRange = 0

def inRange(pair1, pair2):
    inRange = True
    pair1nr1 = int(pair1.split("-")[0])
    pair1nr2 = int(pair1.split("-")[1])
    pair2nr1 = int(pair2.split("-")[0])
    pair2nr2 = int(pair2.split("-")[1])

    if pair1nr2 < pair2nr1 or pair1nr1 > pair2nr2:
        inRange = False
    
    return inRange

for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input4-1.txt"):
    line = line.strip()
    firstPair = line.split(",")[0]
    secondPair = line.split(",")[1]
    if inRange(firstPair, secondPair):
        totalInRange += 1
        print(totalInRange)

print(totalInRange)