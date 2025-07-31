import random

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
     
    def changeBrandName(self, newName):
        self._brandName = newName

    def changeBrandType(self, newType):
        self._brandType = newType


class Pack:
    def __init__(self, stocks, packNumber, stocksRemaining):
        self._stocks = stocks
        self._packNumber = packNumber
        self._stocksRemaining = stocksRemaining

    def removeStock(self, stock):
        self._stocks.remove(stock)
        self._stocksRemaining -= 1
          
    def displayPackContents(self):
        stockNumber = 1
        print("Your pack contents:")
        for stocks in self._stocks:
            print(f"{stockNumber}.  {stocks.getBrandName()} | {stocks.getBrandType()} | {stocks.getRarity()} | {stocks.getValue()}")
            stockNumber += 1
        
    def getStock(self, selectedStock):
        stockIndex = selectedStock - 1
        return (self._stocks[stockIndex])

    def getStocksRemaining(self):
        return (self._stocksRemaining)


class Portfolio:
    def __init__(self, owner):
        self._owner = owner
        self._stocks = []
        self._totalValue = 0

    def addStock(self, stock):
        self._stocks.append(stock)
        self.updateValue(stock)
        
    def updateValue(self, stock):
        self._totalValue += stock.getValue()

    def getTotalValue(self):
        return (self._totalValue)
    
    def displayPortfolio(self):
        stockNumber = 1
        print(f"Total portfolio value: ${self.getTotalValue()}")
        for stocks in self._stocks:
            print(f"{stockNumber}.  {stocks.getBrandName()} | {stocks.getBrandType()} | {stocks.getRarity()} | ${stocks.getValue()}")
            stockNumber += 1


class Player:
    def __init__(self, playerName, playerNumber):
        self._playerName = playerName
        self._playerNumber = playerNumber
        self._portfolio = "empty"
        self._currentPack = "empty"

    def getPlayerName(self):
        return (self._playerName)
    
    def getPlayerNumber(self):
        return (self._playerNumber)
    
    def getTotalValue(self):
        return (self._portfolio.getTotalValue())
    
    def assignPortfolio(self, portfolio):
        self._portfolio = portfolio
    
    def displayPortfolio(self):
        self._portfolio.displayPortfolio()

    def viewCurrentPack(self):
        self._currentPack.displayPackContents()

    def setCurrentPack(self, pack):
        self._currentPack = pack

    '''def passPack(self, pack, nextPack, nextPlayer):'''


class Game:
    def __init__(self, numberOfPlayers):
        self._numberOfPlayers = numberOfPlayers
        self._players = []
        self._currentRound = 0
        self._stockGenerator = []
        self._startingPlayerID = 0

    def getCurrentRound(self):
        return (self._currentRound)
    
    def nextRound(self):
        self._currentRound += 1

    def whatIsYourName(self):
        return input(f"Please enter your name: ")
    
    def addPlayers(self, player):
        self._players.append(player)

    def thisIsStartingPlayer(self, playerNumber):
        return True if playerNumber == 0 else False
    
    def generateRandomNames(self, generatedNames, numberOfNamesToGenerate):
        return random.sample(generatedNames, numberOfNamesToGenerate)

    def createPlayers(self, generatedNames):
        indexingOffset = 1
        playerName = ""
        randomlyGeneratedNames = self.generateRandomNames(generatedNames, self._numberOfPlayers)
        print("Generating players....")
        for playerNumber in range(self._numberOfPlayers):
            playerName = self.whatIsYourName() if self.thisIsStartingPlayer(playerNumber) else randomlyGeneratedNames[playerNumber]
            player = Player(playerName, (playerNumber + indexingOffset))
            portfolio = Portfolio(player)
            player.assignPortfolio(portfolio)
            self.addPlayers(player)

    def displayPlayers(self):
        indexingOffset = 1
        print(f"Player Lobby:")
        for playerNumber in range(self._numberOfPlayers):
            print(f"Player {playerNumber + indexingOffset}: {self._players[playerNumber].getPlayerName()}")

    def displayPlayerValue(self, playerNumber):
        indexingOffset = 1
        print(f"Player {playerNumber + indexingOffset} ({self._players[playerNumber].getPlayerName()}): ${self._players[playerNumber].getTotalValue()}")

    def getRandomStock(self, stockCatalogue, stockRarities):
        randomStock = random.choice(list(stockCatalogue.items()))
        randomRarity = random.choice(list(stockRarities.items()))
        stockName = randomStock[0]
        stockType = randomStock[1]
        stockRarity = randomRarity[0]
        stockValue = randomRarity[1]
        '''print(f"You picked a {stockRarity} {stockName}! This stock is classed as a {stockType} category stock and has a value weighting of {stockValue}!")'''
        return stockName, stockType, stockRarity, stockValue

    def generatePacks(self, stockCatalogue, stockRarities):
        indexingOffset = 1
        stocksInPack = 15
        randomlyGeneratedStocks = []
        for playerNumber in range(self._numberOfPlayers):
            for stockNumber in range(stocksInPack):
                stockName, stockType, stockRarity, stockValue = self.getRandomStock(stockCatalogue, stockRarities)
                newStock = Stock(brandName = stockName, brandType = stockType, rarity = stockRarity, value = stockValue)
                randomlyGeneratedStocks.append(newStock)
                stockNumber += 1
                
            thisPackNumber = playerNumber + indexingOffset
            pack = Pack(stocks = randomlyGeneratedStocks, packNumber = thisPackNumber, stocksRemaining = stocksInPack)
            player = self._players[playerNumber]
            player.setCurrentPack(pack)
            randomlyGeneratedStocks = []

    def viewMyPack(self):
        self._players[self._startingPlayerID].viewCurrentPack()

    def viewPlayersPack(self, playerNumber):
        self._players[playerNumber].viewCurrentPack()

    '''def displayRankings(self):
        playerRankings = []
        highestValue = 0
        for player in self._players:
            highestValuePlayer = player if player.getTotalValue() > highestValue and not in playerRankings
            playerRankings.append(highestValuePlayer)
        Get all the players total values and then sort them, double for loop. for each iteration in player rankings, sub for loop the players to find the highest value then return that, repeat...'''