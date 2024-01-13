def check_horizontal_adjacent(index,lline,res):
    start = -1
    end = -1
    number = -1
    for j in range(len(lline)):
        character = lline[j]
        if character.isnumeric() == True:
            if start == -1:
                start = j
            elif start != -1:
                if j == (len(lline) -1):
                    end = j
        elif character.isnumeric() == False:
            if start != -1:
                end = j - 1
        if start != -1 and end != -1:
            # s = ''.join(lline[start:end+1])
            # print("the s is:",s)
            # print("the start",start,"the end",end)
            if start == 0:
                if lline[end+1] != ".":
                    number = ''.join(lline[start:end+1])
            elif end == (len(lline) -1):
                if lline[start-1] != ".":
                    number = ''.join(lline[start:end+1])
            else:
                if lline[start - 1] != "." or lline[end + 1] != ".":
                    number = ''.join(lline[start:end+1])
            if number != -1:
                # print("the number is",number)
                # print("the start is",start)
                # print("the end is",end)
                res.append(number)
                res.append([start,end,index])
                # print("wow, res here is",res)
                number = -1
            start = end = -1

def check_vertical_adjacent(matrix,index,lline,hRes,res):
    start = end = -1
    number = -1
    checked_lines = []
    flag = 0
    if index == 0 and len(matrix) != 1:
        nextLine = matrix[index+1]
    elif index == (len(matrix)-1):
        nextLine = matrix[index-1]
    elif index == 0 and len(matrix) == 1:
        nextLine = []
    else:
        prevLine = matrix[index-1]
        nextLine = matrix[index+1]
        checked_lines.append(prevLine)
    checked_lines.append(nextLine)
    # print("the index is",index)
    # print("the checked lines are",checked_lines,"for index = ",index)
    for j in range(len(lline)):
        character = lline[j]
        if character.isnumeric() == True:
            if start == -1:
                start = j
            elif start != -1:
                if j == (len(lline) -1):
                    end = j
        elif character.isnumeric() == False:
            if start != -1:
                end = j - 1
        if start != -1 and end != -1:
            # print("index = ",index)
            # print("start = ",start,"end = ",end)
            if start == 0:
                b = start
                e = end + 2
            elif end == (len(lline) -1):
                # print("index=",index)
                b = start -1
                e = end + 1
                # print("b=",b)
                # print("e=",e)
            else:
                b = start - 1
                e = end + 2
            for i in range(b,e):
                # print("the index again is",index)
                for line in checked_lines:
                    if line[i].isnumeric() == False and line[i] != ".":
                        number = ''.join(lline[start:end+1])
                        flag = 1
                        break
                if flag == 1:
                    break
            if number != -1:
                # if number in res:
                    # print("already there")
                    # print("the number is",number)
                # else:
                if (number in hRes) and hRes[hRes.index(number)+1][0] == start and hRes[hRes.index(number)+1][1] == end and hRes[hRes.index(number)+1][2] == index:
                    print("already there")
                    # print("the number in already there is",number)
                else:
                    res.append(number)
                    res.append(index)
                flag = 0
            start = end = number = -1

# each line of the input is scanned twice. once to check horizontal adjacency and second to get vertical (along with diagonal adjacency)     
def processMatrix(matrix):
    i = 0
    # result stores all the numbers that are adjacent to a symbol
    result = []
    # it stores all numbers adjacent to a symbol horizontally
    overallHorizRes = []
    # it stores all numbers adjacent to a symbol diagonally
    overallDiago = []
    # horiz_res stores the number adjacent to a symbol followed by a list containing start, end and index of the line. 
    # All this information is captured because in case a number is adjacent to two symbols both horizontally and vertically/diagonally. We do not count it twice
    horiz_res = []
    # same idea as horiz_res, but the number adjacent to a symbol is followed just by the line index. for debugging purposes only
    diago_res = []
    for i in range(len(matrix)):
        lline = matrix[i]
        check_horizontal_adjacent(i,lline,horiz_res)
        check_vertical_adjacent(matrix,i,lline,horiz_res,diago_res)
    for i in range(len(horiz_res)):
        if i % 2 == 0:
            overallHorizRes.append(horiz_res[i])
    for s in range(len(diago_res)):
        if s % 2 == 0:
            overallDiago.append(diago_res[s])
    result = overallHorizRes + overallDiago
    # print("the horizontal stuff is",horiz_res)
    # print("the diagonal stuff is",diago_res)
    # print("the final result is",result)
    return result

def calculateSum(res):
    sum = 0
    for number in res:
        sum = sum + int(number)
    return sum
        

### Starter program     

def start():
    print("starting by opening the file...")
    file = open("inputGear.txt")
    lines = file.readlines()
    matrix = []
    for line in lines:
        formattedLine = list(line)
        # print("the formatted line is",formattedLine)
        # very nasty to do it like that
        if formattedLine[len(formattedLine)-1] == '\n':
            formattedLine.pop()
        matrix.append(formattedLine)
    
    # print("printing the matrix...")
    i = 0
    # for i in range(len(matrix)):
        # print("the formatted line 2 is",matrix[i])
    res = processMatrix(matrix)
    s = calculateSum(res)
    print("the sum is",s)

start()