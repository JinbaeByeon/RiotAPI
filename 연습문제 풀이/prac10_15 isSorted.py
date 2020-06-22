def isSorted(lst):
    
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

s = input("리스트를 입력하세요: ")
items = s.split()
lst = [int(x) for x in items]

if isSorted(lst):
    print("리스트는 정렬되어 있습니다.")
else:
    print("리스트는 정렬되어 있지 않습니다.")
