def painting(matrix):
    cnt = 0
    for i in range(1,M+1):
        for j in range(1,N+1):
            left = matrix[i][j] - matrix[i][j-1]
            right = matrix[i][j] - matrix[i][j+1]
            top = matrix[i][j] - matrix[i-1][j]
            bottom = matrix[i][j] - matrix[i+1][j]
            if left > 0:
                cnt += left
            if right >0:
                cnt += right
            if top >0:
                cnt += top
            if bottom>0:
                cnt += bottom
    cnt += N*M
    return cnt

MN = input("행과 열을 입력하세요: ").split()

M = int(MN[0])
N = int(MN[1])

matrix = []
matrix_pading =[]
for i in range(N+2):
    matrix_pading.append(0)

matrix.append(matrix_pading)

for i in range(M):
    lst = [int(x) for x in input().split()]
    lst.append(0)
    lst.insert(0,0)
    matrix.append(lst)

matrix.append(matrix_pading)

area = painting(matrix)
print(area)

