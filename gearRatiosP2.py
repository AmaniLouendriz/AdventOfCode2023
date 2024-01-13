## it checks horizontal adjacency
def check_horizontal_adjacent(line,index):
    chars = []
    number = ""
    res = []
    # index is the index of a special character in a line
    if index == 0:
        nextChar = line[index+1]
        # first case: *467...114..
        # nextChar concept is being used
        if nextChar.isnumeric():
            i = index
            while line[i+1].isnumeric():
                number += line[i+1]
                i+=1
            res.append(number)
    elif index == (len(line)-1):
        prevChar = line[index-1]
        # second case: ......123*
        # prevChar concept is being used
        if prevChar.isnumeric():
            i = index
            while line[i-1].isnumeric():
                number += line[i-1]
                i-=1
            # reverse the number
            number = number[::-1]
            res.append(number)
    else:
        # case here: first case: .2*467...114..
        chars.append(line[index-1])
        chars.append(line[index+1])
        j = 0
        for j in range(len(chars)):
            # chars contains the previous and next characters
            if j != 0:
                # nextChar concept is being used
                # for example, here chars are [2,4]
                if chars[j].isnumeric():
                    i = index
                    while line[i+1].isnumeric():
                        number += line[i+1]
                        if (i+1) == (len(line)-1):
                            break
                        i+=1
                    ## number is done being formatted
                    res.append(number)
                    number = ""
            else:
                # prevChar concept is being used
                if chars[j].isnumeric():
                    i = index
                    while line[i-1].isnumeric():
                        number += line[i-1]
                        i-=1
                    # reverse the number
                    number = number[::-1]
                    res.append(number)
                    number = ""
    return res

def check_diagonal_adjacent(matrix,line,charIndex,lineIndex):
    lines_to_check = []
    # res will store the numbers adjacents to a symbol diagonally (vertically included)
    res = []
    if lineIndex == 0:
        nextLine = matrix[lineIndex+1]
    elif lineIndex == (len(matrix)-1):
        nextLine = matrix[lineIndex-1]
    else:
        prevLine = matrix[lineIndex-1]
        nextLine = matrix[lineIndex+1]
        lines_to_check.append(prevLine)
    lines_to_check.append(nextLine)
    for line in lines_to_check:
            if charIndex == (len(line)-1):
                if line[charIndex].isnumeric() or line[charIndex-1].isnumeric():
                    # adjacent to sth
                    number = ''
                    if line[charIndex].isnumeric():
                        i = charIndex
                    elif line[charIndex-1].isnumeric():
                        i = charIndex -1
                    while line[i].isnumeric():
                        number += line[i]
                        i-=1
                    number = number[::-1]
                    res.append(number)
                    number = ''
            elif charIndex == 0:
                if line[charIndex].isnumeric() or line[charIndex+1].isnumeric():
                    number = ''
                    if line[charIndex].isnumeric():
                        i = charIndex
                    elif line[charIndex+1].isnumeric():
                        i = charIndex + 1
                    while line[i].isnumeric():
                        number+= line[i]
                        if i == (len(line)-1):
                            break
                        i+=1
                    res.append(number)
                    number = ''
            else:
                # symbol is in the middle
                #  ...*....   ...*..
                #  ..12....   !..222
                if line[charIndex].isnumeric():
                    right_part = ''
                    i = charIndex
                    while line[i].isnumeric():
                        right_part += line[i]
                        if i == (len(line)-1):
                            break
                        i+=1 
                    i = (charIndex -1)
                    left_part = ''
                    while line[i].isnumeric():
                        left_part += line[i]
                        if i == 0:
                            break
                        i-=1
                    left_part = left_part[::-1]
                    number = left_part + right_part
                    res.append(number)
                elif line[charIndex-1].isnumeric():
                    # ..*...
                    # 12....
                    i = charIndex -1
                    number = ''
                    while line[i].isnumeric():
                        number += line[i]
                        if i == 0:
                            break
                        i-=1
                    number = number[::-1]
                    res.append(number)

                    # now let's deal with this case:
                    # .!.
                    # 1.1

                    # if thos condition isn't added, then the second 1 one the right will not be considered as adjacent

                    if line[charIndex+1].isnumeric():
                        i = charIndex + 1
                        number = ''
                        while line[i].isnumeric():
                            number += line[i]
                            if i == (len(line)-1):
                                break
                            i+=1
                        res.append(number)
                elif line[charIndex+1].isnumeric():
                    # ..*...
                    # ...12.
                    i = charIndex + 1
                    number = ''
                    while line[i].isnumeric():
                        number += line[i]
                        if i == (len(line)-1):
                            break
                        i+=1
                    res.append(number)
    return res




def parse_matrix(matrix):
    index = 0
    # gears store the symbols of a "gear"
    gears = []
    result = []
    # gearRatios stores the product of two part numbers adjacent to a gear
    gearRatios = []
    for index in range(len(matrix)):
        line = matrix[index]
        j = 0
        for j in range(len(line)):
            character = line[j]
            if (character in ['0','1','2','3','4','5','6','7','8','9','.']) == False:
                ## a symbol is found, let's check whether it's a gear or not?
                # res will store the numbers adjacent to a specific symbol
                resH = check_horizontal_adjacent(line,j)
                resD = check_diagonal_adjacent(matrix,line,j,index)
                res = resH + resD
                if len(res) == 2:
                    # then our symbol is adjacent ot exactly two part numbers
                    gears.append(character)
                    gearR = int(res[0]) * int (res[1])
                    gearRatios.append(gearR)
                # this commented part is we wanted to compute part1
                # for number in resH:
                #     result.append(number)
                # for number in resD:
                #     result.append(number)
    return gearRatios

def sum(res):
    s = 0
    for number in res:
        s += int(number)
    return s




def start():
    print("Starting by opening the file...")
    file = open("inputGear.txt")
    lines = file.readlines()
    matrix = []
    for line in lines:
        # line.strip() this doesn't work for some reqson on the first line.. TODO
        formattedLine = list(line)
        if formattedLine[len(formattedLine)-1] == '\n':
            formattedLine.pop()
        matrix.append(formattedLine)
    
    res = parse_matrix(matrix)
    s = sum(res)
    print("the sum is ",s)

start()


################ test 1 #####################
# !23..............776..............552........968..................589
# ...............*.................!2345...............................

# resultHor = [23,2345]

################### test 2 #####################
# 23..............776..............552........968.................!589
# ...............*.................!2345..............................
# resultHor = [589,2345]

############ test 3 ############################
# !23..............776..............552........968..................589!
# ...............*.................!2345...............................?
# resultHor = ['23', '589', '2345']

############ test4 ###############################
# !23..............776..............552........968..................589!
# ...............*.................!2345?..............................?