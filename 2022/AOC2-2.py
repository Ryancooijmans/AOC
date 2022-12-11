import fileinput

totalscore =0

def point(input):
    if input == "A":     #rock
        point = 1
    elif input == "B":   #paper
        point = 2
    else:                               #scissor
        point = 3
        
    return point

def score(arr):
    score = 0
    if arr[1] == "X":
        score = point(arr[0])-1
        if score == 0:
            score = 3
    elif arr[1] == "Y":
        score = 3 + point(arr[0])
    else:
        score = 6 + point(arr[0]) + 1
        if score == 10:
            score = 7

    return score

for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input2-1.txt"):
    arr = line.split()
    totalscore += score(arr)

print(totalscore)