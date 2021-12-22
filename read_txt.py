from collections import OrderedDict

def readFileAndFilter(filePath):
    f = open(filePath,'r')
    lines = (f.readlines())

    filteredLines = []
    for line in lines:
        if len(line) > 2 and line[0] != "$" and line [0] != "#" and line[3] != "*":
            filteredLines.append(line)
    return filteredLines

def splitHands(filteredLines):
    fl = filteredLines
    handNumber = 0
    hands = []
    for i in range(0, len(fl)-1):
        #print(fl[i])
        words = fl[i].split()
        if words[0] == "Table":
            handNumber += 1
            #assign hand number
            number = handNumber
            #assign table name
            table = words[1]
            #assign players list
            player1line = fl[i+3]
            l = player1line.split()
            player1 = l[2]
            player1stack = l[4]
            
            player2line = fl[i+4]
            l = player2line.split()
            player2 = l[2]
            player2stack = l[4]
            
            player3line = fl[i+5]
            l = player3line.split()
            player3 = l[2]
            player3stack = l[4]
            
            player4line = fl[i+6]
            l = player4line.split()
            player4 = l[2]
            player4stack = l[4]
            
            player5line = fl[i+7]
            l = player5line.split()
            player5 = l[2]
            player5stack = l[4]
            
            player6line = fl[i+8]
            l = player6line.split()
            player6 = l[2]
            player6stack = l[4]

            playerNames = (player1, player2, player3, player4, player5, player6)
            playerStacks = (player1stack, player2stack, player3stack, player4stack, player5stack, player6stack)
        
            #assign events list
            events = []
            for j in range(9, len(fl)-1):
                words = fl[j].split()
                if words[0] == "Table":
                    break
                else:
                    event = fl[j].strip()
                    events.append(event)
            #print(eventsList)

            newHand = Hand(number, table, playerNames, playerStacks, events)
            hands.append(newHand)
    return hands
                
    

class Hand( object ):
    def __init__(self, number, table, playerNames, playerStacks, events):
        self.number = number
        self.table = table
        self.playerNames = playerNames
        self.playerStacks = playerStacks
        self.events = events

#filteredLines = readFileAndFilter('sampleFile.txt')
#hands = splitHands(filteredLines)
