def reverse(number):
    result = 0
    while number != 0:
        result = result*10 + number%10
        number //= 10

    return result

def isPalindrome(number):
    return number == reverse(number)


i = int(input("정수를 입력하세요: "))

if isPalindrome(i):
    print("대칭수")
else:
    print("대칭수 아님")
