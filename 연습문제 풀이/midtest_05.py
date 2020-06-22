def f(cow1,cow2,cow3):
    if abs(cow1 - cow2) == 1:
        if abs(cow3 - cow1)==1 or abs(cow3- cow2)==1:
            print(0)
            print(0)
        else:
            print(1)
            print(2)
    elif abs(cow1- cow3) ==1:
        if abs(cow2 - cow1)==1 or abs(cow2- cow3)==1:
            print(0)
            print(0)
        else:
            print(1)
            print(2)
    elif abs(cow3 - cow2) ==1:
        if abs(cow1 - cow3)==1 or abs(cow1- cow2)==1:
            print(0)
            print(0)
        else:
            print(1)
            print(2)

    elif abs(cow1-cow2) ==2 or abs(cow1-cow3) ==2 or abs(cow3-cow2) ==2:
        print(1)
        print(2)

    return

places = input("소의 위치: ").split()
cow1 = int(places[0])
cow2 = int(places[1])
cow3 = int(places[2])

f(cow1,cow2,cow3)
