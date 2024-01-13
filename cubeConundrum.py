import re

# This function validates that the three colors are within the limit

def validate(red,blue,green):
    if red > 12 or green > 13 or blue > 14:
        return False
    return True

# This function processes the line, extracts the important informationa and stores results in the ids list (actual game ids for part one, and 
# the power of a bag in part 2)

def processLine(ids,line):
    regexGame = "^Game ([1-9]|[1-9][0-9]|100):"
    game = re.findall(regexGame,line)
    # print("The game is",game)
    sets = line.split("; ")
    # print("the sets are",sets)
    # regexColor = "[1-9][?=\s]red|[1-9][?=\s]blue|[1-9][?=\s]green|[1-9][0-9]\sred|[1-9][0-9]\sblue|[1-9][0-9]\sgreen"

    resP = True
    minGreen = 0
    minRed = 0
    minBlue = 0
    for i in range(len(sets)):
        # for each set
        redRegex = "([1-9]|[1-9][0-9])\sred"
        blueRegex = "([1-9]|[1-9][0-9])\sblue"
        greenRegex = "([1-9]|[1-9][0-9])\sgreen"
        red = re.findall(redRegex,sets[i])
        blue = re.findall(blueRegex,sets[i])
        green = re.findall(greenRegex,sets[i])
        if red != []:
            redNum = int(red[0])
        else:
            redNum = 0
        if blue != []:
            blueNum = int(blue[0])
        else:
            blueNum = 0
        if green != []:     
            greenNum = int(green[0])
        else:
            greenNum = 0
        # print("the red part is",redNum)
        # print("the blue part",blueNum)
        # print("the greenPart",greenNum)
        if redNum > minRed:
            minRed = redNum
        if greenNum > minGreen:
            minGreen = greenNum
        if blueNum > minBlue:
            minBlue = blueNum
        # res = validateAmount(redNum,blueNum,greenNum)
        # resP = res and resP
    power = minRed * minGreen * minBlue
    ids.append(power)

    
    # print("the resT is",resP)
    # if resP == True:
    #     gameId = int(game[0])
    #     ids.append(gameId)

   

    # regexSet1 = "[1-9][0-9]\s[a-z]+" as for now there are issues with regex...
    # regexSet2 = "[1-9]\s[a-z]+"
    # set1 = re.findall(regexSet1,line)
    # set2 = re.findall(regexSet2,line)
    # print("the set1 is",set1)
    # print("the set2 is",set2)
    # x = line.split("; ")
    # print("the x is",x)

def sum(ids):
    s = 0
    for id in ids:
        s = s + id
    return s


def start():
    print("Starting by opening file")
    file1 = open("inputCube.txt","r")
    lines = file1.readlines()
    ids = []
    for line in lines:
        processLine(ids,line)
    s = sum(ids)
    print("the sum is",s)
    # processLine("Game 4: 2 green, 3 blue, 1 red; 17 green, 1 blue, 1 red; 1 green, 5 red")
    # processLine("Game 1: 2 red, 2 green; 6 red, 3 green; 2 red, 1 green, 2 blue; 1 red")

start()
