def getRightmostLowestPoint(points):
    point = [points[0][0],points[0][1]]
    for i in range(1,len(points)):
        if point[0] <= points[i][0] and point[1] >= points[i][1]:
                point = [points[i][0],points[i][1]]
        
    return point


line = input("6개의 점을 입력하세요: ").split()
p = [[eval(line[i]),eval(line[i+1])] for i in range(0,12,2)]

point = getRightmostLowestPoint(p)
print("최우측하단의 점은 (",point[0],", ", point[1],") 입니다.")
