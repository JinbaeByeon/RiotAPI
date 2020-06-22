list1 = (input("10개의 숫자를 입력하세요: "))
list1 = list1.split()
list2 = list()
for i in list1:
    if list2.count(i) == 0:
        list2.append(i)


print(list2)
    
 
