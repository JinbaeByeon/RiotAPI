def printChars(ch1, ch2, numberPerLine):
    cnt = 0
    for i in range(ord(ch1),ord(ch2)+1):
        cnt+=1
        print(chr(i),end=" ")
        if cnt% numberPerLine == 0:
            print()
        
printChars('1','Z',10)
