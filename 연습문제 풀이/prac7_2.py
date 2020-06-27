class Stock:
    def __init__(self,name,symbol,previousPrice,currentPrice):
        self.__name = name
        self.__symbol = symbol
        self.__previousePrice = previousPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPreviousPrice(self):
        return self.__previousePrice

    def getCurrentPrice(self):
        return self.__currentPrice


    def getChangePercent(self):
        return (self.__currentPrice - self.__previousePrice)/self.__previousePrice

stock =Stock("Intel","INTC",20500,20350)

print(stock.getChangePercent())