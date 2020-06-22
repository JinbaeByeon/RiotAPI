def f(K,N):
    if N==0 or N==1:
        return N
    else:
        if N % (2**(K)-1) == 0:
            return f(K-1,2**(K-1)-1)*2 + K

        i = 0
        while True:
            i += 1
            if N <= 2**(K-1) or (N-2**(K-1)) // (2**(K-i-1)) > 0 :
                break
        return f(K-1,2**(K-1)-1) + f(K-i,N-2**(K-1)) + K

numbers = input("K와 N을 입력하세요: ").split()

a= int(numbers[0])
b= int(numbers[1])
print("f(",a,",",b, ") = ",f(a,b))

