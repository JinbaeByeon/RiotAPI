def m1(i):
    Sum = 0.0
    for n in range(1,i+1):
        Sum += n/(n+(n+1)**(1/2))
    return Sum


def m2(i):
    if i==1:
        return 1/(1+2**(1/2))
    return m2(i-1) + i/(i+(i+1)**(1/2))

print(m1(624))

print(m2(624))
