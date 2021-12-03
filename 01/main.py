def loadFile(fileName):
    return open(fileName, "r").read()


def getCountOfHigherValues(dataStrArray: list[str]):
    oldData = int(dataStrArray[0])
    match = 0
    for i in range(0, len(dataStrArray)):
        if dataStrArray[i] == "":
            continue
        lineValue = int(dataStrArray[i])
        if lineValue > oldData:
            match += 1
        oldData = lineValue
    return match


def getSumOfThree(dataStrArray: list[str]):
    result = []
    for i in range(0, len(dataStrArray)):
        subArray = dataStrArray[i:i+3]
        value = 0
        for i in range(0, len(subArray)):
            if subArray[i] == "":
                continue
            value += int(subArray[i])
            value = value + int(subArray[i])
        result.append(value)
    return result


filePath = "input2.txt"
dataArrray = loadFile(filePath).split("\n")
print(getCountOfHigherValues(dataArrray))
print(getCountOfHigherValues(getSumOfThree(dataArrray)))
