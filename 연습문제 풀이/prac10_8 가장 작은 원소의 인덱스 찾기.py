def indexOfSmallestElement(lst):
    idx = 0
    for i in range(1,len(lst)):
        if lst[i] < lst[idx]:
            idx = i
    return idx


s = input("정수를 입력하세요: ")
items = s.split()
lst = [int(x) for x in items]

print("최소값의 인덱스는 ",indexOfSmallestElement(lst),"입니다.")
