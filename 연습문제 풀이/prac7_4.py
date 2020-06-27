SLOW =1
MEDIUM = 2
FAST = 3

class Fan:
    def __init__(self,speed = SLOW,radius = 5,color ="blue",on= False):
        self.Speed = speed
        self.Radius = radius
        self.Color = color
        self.On = on

    def getSpeed(self):
        return self.Speed

    def getRadius(self):
        return self.Radius

    def getColor(self):
        return self.Color

    def isOn(self):
        return self.On
