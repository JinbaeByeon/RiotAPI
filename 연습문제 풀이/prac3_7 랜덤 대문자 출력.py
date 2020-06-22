import time

word = ord('A') + (int)(time.time())%(ord('Z')-ord('A')+1)

print(chr(word))
