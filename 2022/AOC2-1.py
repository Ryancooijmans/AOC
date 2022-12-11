import fileinput

totalscore = 0

def point(input):
    if input == "X" or input == "A":     #rock
        point = 1
    elif input == "Y" or input == "B":   #paper
        point = 2
    else:                               #scissor
        point = 3
        
    return point

def score(opponent, you):
    opponent = point(opponent)
    you = point(you)
    score = you

    if opponent+1 == you or opponent-2 == you:
        score += 6
    elif opponent == you:
        score += 3
    
    return score

for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input2-1.txt"):
    opponent = line.split()[0]
    you = line.split()[1]
    totalscore += score(opponent, you)

print(totalscore)