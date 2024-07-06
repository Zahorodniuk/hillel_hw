testinput1 = [12, 3, 4, 10]
testinput2 = [1]
testinput3 = []
testinput4 = [12, 3, 4, 10, 8]

inputList = testinput4
listLen = len(inputList)

if listLen > 1:
    x = inputList.pop(listLen - 1)
    inputList.insert(0, x)

print(inputList)