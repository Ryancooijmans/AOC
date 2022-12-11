import fileinput


mostCalories = 0
currentCalories = 0
for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input1-1.txt"):

    if line.strip() == "":
        if currentCalories > mostCalories:
            mostCalories= currentCalories
        currentCalories = 0
    else:
        currentCalories += int(line)


print(mostCalories)