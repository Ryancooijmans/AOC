import fileinput

def compare(inputarr):
    i = 0
    while i < (len(inputarr)-14):
        buffer = inputarr[i:i+14]
        # newarr = []
        # j = 0
        # while j < len(buffer):
        #     if buffer[j] in newarr:
        #         break
        #     newarr.append(buffer[j])
        #     j += 1
        if len(set(buffer)) == len(buffer):
            return i + 14
        i += 1

for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input6-1.txt"):
    inputarr = list(line)
    marker = compare(inputarr)

print(marker)