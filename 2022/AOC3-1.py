import fileinput

totalpoints = 0

def compare(firstarr, secondarr):
    i = 0
    j = 0
    for i in range(len(firstarr)):
        for j in range(len(secondarr)):
            if firstarr[i] == secondarr[j]:
                return firstarr[i]
            j += 1
        i += 1

def points(letter):
    ascii = ord(letter)
    if ascii > 90:
        points = ascii - 96
    else:
        points = ascii - 38
    return points

for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input3-1.txt"):
    arr = list(line)
    firsthalf = arr[:len(arr)//2]
    secondhalf = arr[len(arr)//2:len(arr)]
    identical = compare(firsthalf, secondhalf)
    totalpoints += points(identical)

print(totalpoints)