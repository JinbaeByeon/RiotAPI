def sumColumn(m,columnIndex):
    return m[0][columnIndex] +m[1][columnIndex] +m[2][columnIndex]

matrix = []

for i in range(3):
    s = input("3X4 행렬의 행 "+ str(i) + "번에 대한 원소를 입력하세요: ")
    items = s.split()
    lst = [eval(x) for x in items]
    matrix.append(lst)

for i in range(4):
    print(sumColumn(matrix,i))
    
