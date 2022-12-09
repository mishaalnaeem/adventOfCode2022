def readFile():
    file = open('map.txt')
    lines = file.readlines()
    return lines

def checkRight(val, indX, indY):
    if(indX == len(forest[0])-2):
        if(val<=int(forest[indY][indX])):
            return False
        else:
            return True
    if(val<=int(forest[indY][indX])):
        return False
    else:
        holder = checkRight(val, indX+1, indY)
        if(holder):
            return True
        return False

def checkLeft(val, indX, indY):
    if(indX == 0):
        if(val<=int(forest[indY][indX])):
            return False
        else:
            return True
    if(val<=int(forest[indY][indX])):
        return False
    else:
        holder = checkLeft(val, indX-1, indY)
        if(holder):
            return True
        return False

def checkUp(val, indX, indY):
    if(indY == 0):
        if(val<=int(forest[indY][indX])):
            return False
        else:
            return True
    if(val<=int(forest[indY][indX])):
        return False
    else:
        holder = checkUp(val, indX, indY-1)
        if(holder):
            return True
        return False

def checkDown(val, indX, indY):
    if(indY == len(forest)-1):
        if(val<=int(forest[indY][indX])):
            return False
        else:
            return True
    if(val<=int(forest[indY][indX])):
        return False
    else:
        holder = checkDown(val, indX, indY+1)
        if(holder):
            return True
        return False
    

forest = readFile()
visibleTrees = ((2 * len(forest)) + (2 * (len(forest[0])-1))) - 4 #rectangle boundaries


for i in range(1,len(forest)-1):
    for j in range(1,len(forest[0])-2):
        isVisible = checkRight(int(forest[i][j]), j+1, i) or checkLeft(int(forest[i][j]), j-1, i) or checkDown(int(forest[i][j]), j, i+1) or checkUp(int(forest[i][j]), j, i-1)
        if(isVisible == True):
            visibleTrees = visibleTrees + 1
            isVisible = False
print(visibleTrees)