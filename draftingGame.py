'''
use numpy module for calculations and randomness
use pytest for testing the code
use rich for prettier text (or use pygame for gui)
more itter tools ?

Class Game
A collection of players each with their own points.

A game consists of 8 players (7 AI). After each player has made 15 picks out of 3 packs, the total value of their portfolio/hand is added up. 
Packs are passed to the right in the first and last rounds. Second round packs are passed to the left. Bonus rewards are given out to players who collect sets.

Class Player
A player will have a hand or collection of stocks/cards, a seat number, a name

Class Hand/Portfolio
A hand consists of a collection of stocks/cards. We add cards/stock to this from packs.

Inside the hand class we calculation the value, based on set collections

Class Stock/Card
Each stock/card has a rarity, name, brand/type and a value.

Class Packs/OpenBids
A pack/open bids is similar to a hand. it consists of a collection of stocks or cards. However these are available to each player to pick one from. Using a round robin system, each person drafts 1 card/stock.

functions:
 initialise()
 Ask for the players name?
 They will be given a seat number

'''
class Stock:
    def __init__(self, brandName, brandType, rarity, value):
        self._brandName = brandName
        self._brandType = brandType
        self._rarity = rarity
        self._value = value

    def getBrandName(self):
        return (self._brandName)
    
    def getBrandType(self):
        return (self._brandType)
    
    def getRarity(self):
        return (self._rarity)
    
    def getValue(self):
        return (self._value)
    
    def setRarity(self, rarity):
        self._rarity = rarity

    def setValue(self, value):
        self._value = value


class Pack:
    def __init__(self, stocks, packNumber, stocksRemaining):
        self._stocks = stocks
        self._packNumber = packNumber
        self._stocksRemaining = stocksRemaining

    def removeStock(self, stock):
        self._stocks.remove(stock)
        self._stocksRemaining -= 1
        
    '''For each stock inside the pack, print out the stocks (brandname, brandtype, rarity and value)
        When the pack goes down to 1 stock, use a different method as lists are not iterable meaning it does
        not treat a list with only 1 item in it as a list.'''    
    def displayPackContents(self):
        stockNumber = 1
        for stocks in self._stocks:
            print(f"{stockNumber}.  {stocks.getBrandName()} | {stocks.getBrandType()} | {stocks.getRarity()} | {stocks.getValue()}")
            stockNumber += 1
        
    def getStocksRemaining(self):
        return (self._stocksRemaining)

Coke = Stock(brandName = "Coca-Cola", brandType = "Food & Beverage", rarity = "Common", value = 3000)
print(Coke.getRarity())
print(Coke.setRarity("Rare"))
print(Coke.getRarity())

Pepsi = Stock(brandName = "Pepsi", brandType = "Food & Beverage", rarity = "Uncommon", value = 3000)
print(Pepsi.getRarity())
print(Pepsi.setRarity("Legendary"))
print(Pepsi.getRarity())

pack1 = Pack([Coke, Pepsi], 1, 2)
pack1.displayPackContents()
pack1.removeStock(Coke)
print("        ")
pack1.displayPackContents()