import random
def onePath(numberOfSlots):
    position = 0
    for i in range(numberOfSlots):
        if random.random() < 0.5:
            print("L",end ="")
        else:
            print("R",end="")
            position += 1
    print()
    return position


def printHistogram(slots):
    maxSlotHeight = max(slots)
    for h in range(maxSlotHeight,0,-1):
        for i in range(len(slots)):
            if slots[i] < h:
                print(" ",end="")
            else:
                print("0",end="")
        print()
    for i in range(len(slots)):
        print(i,end="")
        
            
numberOfBalls = eval(input("떨어뜨릴 공의 개수를 입력하세요: "))
numberOfSlots = eval(input("콩 기계의 슬롯 개수를 입력하세요: "))

slots = numberOfSlots * [0]

for i in range(numberOfBalls):
    slots[onePath(numberOfSlots)]+=1
printHistogram(slots)
