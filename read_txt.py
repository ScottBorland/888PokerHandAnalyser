

def readFile(filePath):
    f = open(filePath,'r')
    lines = (f.readlines())
    linesToRemove = [];
    for i in range(0, len(lines) - 1):
        if lines[i][0] == "#" or lines[i][0] == "$":
            linesToRemove.append(lines[i])
    for j in linesToRemove:
        lines.remove(j)
    for line in lines:
        print(line)

readFile('sampleFile.txt')


        
