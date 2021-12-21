

def readFileAndFilter(filePath):
    f = open(filePath,'r')
    lines = (f.readlines())

    filteredLines = []
    for line in lines:
        if len(line) > 2 and line[0] != "$" and line [0] != "#":
            filteredLines.append(line)
    return filteredLines

def 

class Hand( object ):
    def __init__(self, number, table, players, events):
        self.number = number
        self.table = table
        self.players = players
        self.events = events

readFileAndFilter('sampleFile.txt')
