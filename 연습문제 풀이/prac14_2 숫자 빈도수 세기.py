s= input("정수를 입력하세요: ")
numbers = [int(x) for x in s.split()]
dic ={}
for num in numbers:
    if num not in dic:
        dic[num] = numbers.count(num)

Max = max(dic.values())
        
for k,v in dic.items():
    if Max == v:
       print(k,end=" ")



    
