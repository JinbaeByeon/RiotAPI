def reverse(number):
    result = 0
    while number != 0:
        result = result*10 + number%10
        number //= 10

    return result


numbers = [int(x) for x in input("N과 K를 입력하세요: ").split()]
N = numbers[0]
K = numbers[1]

max = 0
for i in range(1,K+1):
    num = reverse(N*i)
    if num > max:
        max = num

print(max)