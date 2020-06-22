import time
population = 312032486

year_to_second = 365*24*60*60

born =  year_to_second//7
death = year_to_second//13
immigrant = year_to_second //45

cnt = 0
while 1:
    cnt = (cnt +1) % 5
    
    population = population + born - death + immigrant
    if cnt == 0:
        print(population)

    time.sleep(0.1)
