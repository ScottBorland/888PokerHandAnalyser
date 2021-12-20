

def readFile(filePath):
    f = open(filePath,'r')
    lines = (f.readlines())

    filteredLines = []
    for line in lines:
        if len(line) > 2 and line[0] != "$" and line [0] != "#":
            filteredLines.append(line)
    for line in filteredLines:
        print(line)

readFile('sampleFile.txt')


        
