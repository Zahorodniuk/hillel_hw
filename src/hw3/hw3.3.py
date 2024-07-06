testinput1 = [1,2,3,4,5,6]
testinput2 = [1,2,3]
testinput3 = [1,2,3,4,5]
testinput4 = [1]
testinput5 = []

inputList = testinput1

size = len(inputList)
i = size - size // 2

result = [inputList[:i], inputList[i:]]
print(result)

