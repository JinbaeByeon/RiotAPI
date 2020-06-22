def sort_cow(cows):
    cnt = 0
    i = num_cow-1
    while i > 0:
        if cows[0] > cows[i]:
            cows.insert(i+1,cows[0])
            cows.pop(0)
            i=num_cow
            cnt += 1
        elif cows[i] < cows[i-1]:
            cows.insert(i,cows[0])
            cows.pop(0)
            i = num_cow
            cnt += 1
        i -= 1

    print("cnt: ",cnt," ", cows)

    return cnt

num_cow = eval(input("소의 수: "))

cows = [int(x) for x in input("소의 순서: ").split()]

sort_cow(cows)
