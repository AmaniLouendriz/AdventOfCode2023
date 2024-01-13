import re

############ This is my day 1 of AOC ######################

### calculateNumber takes a line and return the INDEXES of first and last digit 
### if there's just one digit in the line then the position of that digit is being returned twice

def calculateNumber(line):
    counter = 0
    indexes = []
    # I want first to determine the first number
    while counter < len(line):
        if line[counter].isnumeric():
            #I found the first number !
            indexes.append(counter)
            break
        counter += 1

    # Then I want to get the last one

    counter = len(line) - 1
    while counter >= 0:
        if line[counter].isnumeric():
            # I found the last number
            #value = value + line[counter]
            indexes.append(counter)
            break
        counter -= 1

    return indexes

### since actual alphanumeric numbers should be taken into account, like one, two. This method 
### takes the line and extracts all numbers from 0-9; then returns the numbers(in letters) with their position in the line input

def getEmbeddedNumberWithIndex(line):
    alphaNumericList = []
    threeChar = ["one","two","six"]
    fourChar = ["four","five","nine"]
    fiveChar = ["three","seven","eight"]
  
    counter = 0
    ## It may seem confusing why I am incrementing by 2,3,4 instead of 3,4,5. It's because of a case like 
    ## pbnfrxblk3sevenxjcmcvhlgrghpbgdnpl8xsr3fiveoneightq
    ## the last eight won't have been taken into account since the e is embedded in the "one" before. so we should consider the last letter 
    ## as well
    while counter < len(line):
        if line[counter].isnumeric():
            counter += 1
        elif line[counter:(counter+3)] in threeChar:
            alphaNumericList.append(line[counter:(counter+3)])
            alphaNumericList.append(counter)
            counter = counter + 2
        elif line[counter:(counter+4)] in fourChar:
            alphaNumericList.append(line[counter:(counter+4)])
            alphaNumericList.append(counter)
            counter = counter + 3
        elif line[counter:(counter+5)] in fiveChar:
            alphaNumericList.append(line[counter:(counter+5)])
            alphaNumericList.append(counter)
            counter = counter + 4
        else:
            counter += 1


    return alphaNumericList


############## Calculating the sum of the values in the list##############

def calculateSum(result,sum):
    for number in result:
        sum += int(number)
    return sum

### Taking a digit in letter and converting it to a number ##############

def getActualNumber(alphaNumber):
    if alphaNumber == "one":
        return 1
    elif alphaNumber == "two":
        return 2
    elif alphaNumber == "three":
        return 3
    elif alphaNumber == "four":
        return 4
    elif alphaNumber == "five":
        return 5
    elif alphaNumber == "six":
        return 6
    elif alphaNumber == "seven":
        return 7
    elif alphaNumber == "eight":
        return 8
    elif alphaNumber == "nine":
        return 9
    return -1

#### processLine takes the list of result that contains all numbers found so far, and the line.
#### it then retrieves all numbers (both in letters and actual digits), concatenate the digit at the smallest position to the one 
#### at the biggest position


def processLine(result,line):
    numbersIndexes = calculateNumber(line)
    alphaNumbers = getEmbeddedNumberWithIndex(line)
    indexList = []
    numberRes = ""
    counter = 0

    ## adding alpha numbers indexes

    while counter < len(alphaNumbers):
        if counter % 2 == 1:
            indexList.append(alphaNumbers[counter])
        counter += 1

    ## adding int number indexes
    
    for number in numbersIndexes:
        indexList.append(number)

    mini = min(indexList)
    maxi = max(indexList)

    if line[mini].isnumeric():
        numberRes = numberRes + line[mini]
    else:
        numberRes = numberRes + str(getActualNumber((alphaNumbers[alphaNumbers.index(mini) - 1])))

    if line[maxi].isnumeric():
        numberRes = numberRes + line[maxi]
    else:
        numberRes = numberRes + str(getActualNumber((alphaNumbers[alphaNumbers.index(maxi) - 1])))

    result.append(numberRes)

    
############### Main #################################
def start():
    print("Starting by opening the file ...")
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    resultSum=[]
    for line in lines:
        processLine(resultSum,line)

    # Now calculate the sum of the numbers in the result list

    sum = 0
    sumR = calculateSum(resultSum,sum)


    print("the sum is",sumR)


    ####### Some tests ####################

    # print("the length of numbers",len(resultSum))

    # processLine("abcd9efg")
    # processLine("twofiveqxfivezpkvfvxt5eightjhnpl")
    #processLine("fpfqp7three7")
    #processLine("1hvhqqmrs1bgttshthg6")
    #processLine("4bvnccbdh4onefztdrpq62vvbnvpxxvgrngnfjgfk")
    #processLine("653spgrvd")
    #processLine("sixctlhkjmmxh2fourfivenine37")
    #processLine("229mjp3txmqsxxqdbnnnbrtrcctgzseven")
    # processLine("jfourdbpcjc39bhglgnine")
    # processLine("bvnltxdmsp7twoxzpdjdvkxeight4twothree")
    # processLine("418oneeight")
    # processLine("114sixone1eight2")
    # processLine("xrbtzbklqsl11")
    # processLine("twovhjpdxmcxshnhv5vs")
    # processLine("pbnfrxblk3sevenxjcmcvhlgrghpbgdnpl8xsr3fiveoneightq")
    


start()





