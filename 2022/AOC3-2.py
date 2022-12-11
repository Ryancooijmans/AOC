import fileinput

totalpoints = 0
alllines = []

def compare(firstarr, secondarr, thirdarr):
    i = 0
    j = 0
    k = 0
    for i in range(len(firstarr)):
        for j in range(len(secondarr)):
            for k in range(len(thirdarr)):
                if firstarr[i] == secondarr[j] == thirdarr[k]:
                    return firstarr[i]
                k += 1
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
    alllines.append(line)

for i in range(0,len(alllines)-1,3):
    identical = compare(alllines[i], alllines[i+1], alllines[i+2])
    totalpoints += points(identical)

print(totalpoints)