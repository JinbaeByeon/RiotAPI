def m(i):
    Sum = 0
    for n in range(1,i+1):
        Sum += n/(n+1)

    return round(Sum,4)


print("i\t\tm(i)")
for i in range(1,21):
    print(i,"\t\t",m(i))
