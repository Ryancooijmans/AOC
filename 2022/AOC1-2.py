import fileinput


totalCalories = 0
currentCalories = 0
top = 3
i = 0
array = []
for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input1-1.txt"):

    if line.strip() == "":
        array.append(currentCalories)
        currentCalories = 0
    else:
        currentCalories += int(line)

array.sort(reverse=True)
while i < top:
    totalCalories += array[i]
    i += 1

print(totalCalories)