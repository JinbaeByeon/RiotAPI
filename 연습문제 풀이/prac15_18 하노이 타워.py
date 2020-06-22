count =0

def moveDisks(n,fromTower,toTower,auxTower):
    global count

    if n==1:
        count += 1
    else:
        moveDisks(n-1,fromTower,auxTower,toTower)
        count +=1
        moveDisks(n-1,auxTower,toTower,auxTower)
                  


moveDisks(10,'A','B','C')
print(count)
