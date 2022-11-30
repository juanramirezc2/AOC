input = open('input.txt', 'r').read().strip()
inputList = input.splitlines()


totalArea = 0

for x in inputList:
    sideList = x.split("x")
    length = int(sideList[0])
    width = int(sideList[1])
    height = int(sideList[2])
    totalGiftArea = 2*length*width + 2*width*height + 2*height*length
    sortedSides = sorted([length,width,height])
    totalArea += (totalGiftArea + sortedSides[0] * sortedSides[1])



print(totalArea)

print("Result: {}".format(totalArea))
