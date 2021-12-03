def loadFile(fileName):
    return open(fileName, "r").read()


def deleteAllHaveCharAt(values: list[str], toDeleteValue: str, position: int):
    res = filter(lambda x: x[position] != toDeleteValue, values)
    return list(res)


def getCountsOf0And1(values: list[str], index: int):
    count0 = 0
    count1 = 0
    for line in values:
        if line == "":
            continue
        if line[index] == "0":
            count0 += 1
        if line[index] == "1":
            count1 += 1
    return count0, count1


lines = loadFile("input.txt").split("\n")
dataSize = len(lines[0])
possibleOxigenValue: list[str] = lines.copy()
print(len(lines), len(possibleOxigenValue))
possibleCO2Value: list[str] = lines.copy()


def step1():
    gammarate = ""
    epsilonrate = ""
    for i in range(0, dataSize):
        count0, count1 = getCountsOf0And1(lines, i)
        if count0 > count1:
            gammarate += "0"
            epsilonrate += "1"

        else:
            gammarate += "1"
            epsilonrate += "0"
    return gammarate, epsilonrate


def step2(listOfValues: list[str], positiveValue: str, negativeValue: str):
    tempList = listOfValues.copy()
    for i in range(0, dataSize):
        count0, count1 = getCountsOf0And1(tempList, i)

        if count1 >= count0:
            if (len(tempList) > 1):
                tempList = deleteAllHaveCharAt(
                    tempList, positiveValue, i)
        else:
            if (len(tempList) > 1):
                tempList = deleteAllHaveCharAt(
                    tempList, negativeValue, i)
    return tempList[0]

    # deleteAllHaveValueAt(possibleCO2Value, "1", i)


gammarate, epsilonrate = step1()
gammarateInt = int(gammarate, 2)
epsilonrateInt = int(epsilonrate, 2)
print("gamarate:", gammarate, "epsilonrate:", epsilonrate)
print("Solution step1: ", gammarateInt * epsilonrateInt)

oxigon = int(step2(lines, "0", "1"), 2)
co2 = int(step2(lines, "1", "0"), 2)

print("possibleOxigenValue:", oxigon)
print("possibleCO2Value:", co2)
print("Solution step2: ", oxigon * co2)
