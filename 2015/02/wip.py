input = open('input.txt', 'r').read().strip()
inputList = input.splitlines()


feetsOfRibbon = 0

for x in inputList:
    sideList = x.split("x")
    length = int(sideList[0])
    width = int(sideList[1])
    height = int(sideList[2])
    sortedSides = sorted([length,width,height])
    ribbonForBow = height*length*width 
    feetsOfRibbon += (ribbonForBow + (sortedSides[0] + sortedSides[0] + sortedSides[1] + sortedSides[1]))



print(feetsOfRibbon)

print("Result: {}".format(feetsOfRibbon))
