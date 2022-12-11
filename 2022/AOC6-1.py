import fileinput

def compare(inputarr):
    i = 0
    while i < len(inputarr):
        if(inputarr[i] == inputarr[i+1] or 
        inputarr[i] == inputarr[i+2] or 
        inputarr[i] == inputarr[i+3] or
        inputarr[i+1] == inputarr[i+2] or
        inputarr[i+1] == inputarr[i+3] or 
        inputarr[i+2] == inputarr[i+3]
        ):
            i += 1
        else:
            return i+4


for line in fileinput.input(files= "C:/Users/linde/Documents/AOC/2022/input6-1.txt"):
    inputarr = list(line)
    marker = compare(inputarr)

print(marker)