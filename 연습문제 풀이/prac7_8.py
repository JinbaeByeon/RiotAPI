import time


class StopWatch:
    def __init__(self):
        self.startTime = time.time()

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def start(self):
        self.startTime = time.time()

    def stop(self):
        self.endTime = time.time()

    def getElapsedTime(self):
        return int(1000*(self.endTime-self.startTime))

limit = 1000000
stopWatch = StopWatch()
dummy = 0
for i in range(1,limit+1):
    dummy += 1
stopWatch.stop()

print(stopWatch.getElapsedTime(),"ms")
