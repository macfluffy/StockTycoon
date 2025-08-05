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

    def getStock(self, selectedStock):
        stockIndex = selectedStock - 1
        return (self._stocks[stockIndex])

    def getStocksRemaining(self):
        return (self._stocksRemaining)
    
    def isPackEmpty(self):
        return True if self._stocksRemaining == 0 else False
    
    def takeStock(self, stockNumber):
        takenStock = self._stocks.pop(stockNumber)
        self._stocksRemaining -= 1
        return takenStock
          
    def displayPackContents(self):
        stockNumber = 1
        print("Your pack contents:")
        for stocks in self._stocks:
            print(f"{stockNumber}.  {stocks.getBrandName()} | {stocks.getBrandType()} | {stocks.getRarity()} | {stocks.getValue()}")
            stockNumber += 1


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
    
    def getMostRecentPick(self):
        return self._stocks[-1].getBrandName()
    
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
    
    def getCurrentPack(self):
        return (self._currentPack)
    
    def getMostRecentPick(self):
        return self._portfolio.getMostRecentPick()
    
    def isPackEmpty(self):
        return True if self._currentPack.isPackEmpty() else False
    
    def assignPortfolio(self, portfolio):
        self._portfolio = portfolio
    
    def displayPortfolio(self):
        self._portfolio.displayPortfolio()

    def viewCurrentPack(self):
        self._currentPack.displayPackContents()

    def setCurrentPack(self, pack):
        self._currentPack = pack

    def takeStockFromPack(self, stockNumber):
        indexingOffset = 1
        stockTaken = self._currentPack.takeStock(stockNumber - indexingOffset)
        self._portfolio.addStock(stockTaken)


class Game:
    def __init__(self, numberOfPlayers):
        self._numberOfPlayers = numberOfPlayers
        self._players = []
        self._currentRound = 1
        self._stockGenerator = []
        self._startingPlayerID = 0

    def getCurrentRound(self):
        return (self._currentRound)
    
    def getRandomStock(self, stockCatalogue, stockRarities):
        randomStock = random.choice(list(stockCatalogue.items()))
        randomRarity = random.choice(list(stockRarities.items()))
        stockName = randomStock[0]
        stockType = randomStock[1]
        stockRarity = randomRarity[0]
        stockValue = randomRarity[1]
        return stockName, stockType, stockRarity, stockValue
    
    def isPackEmpty(self):
        return True if self._players[self._startingPlayerID].isPackEmpty() else False
    
    def thisIsStartingPlayer(self, playerNumber):
        return True if playerNumber == self._startingPlayerID else False
    
    def thisIsLastPlayer(self, playerNumber):
        indexingOffset = 1
        playerNumber += indexingOffset
        return True if playerNumber == self._numberOfPlayers else False
    
    def passingForwards(self):
        return True if not self._currentRound == 2 else False
    
    def gameIsOver(self):
        return True if self._currentRound == 3 and self.isPackEmpty() else False
    
    def addPlayers(self, player):
        self._players.append(player)   

    def nextRound(self):
        self._currentRound += 1

    def whatIsYourName(self):
        return input(f"Please enter your name: ")

    def displayGameLobby(self):
        indexingOffset = 1
        print(f"Game Lobby:")
        for playerNumber in range(self._numberOfPlayers):
            print(f"Player {playerNumber + indexingOffset}: {self._players[playerNumber].getPlayerName()}")

    def displayPlayerPortfolio(self):
        self._players[self._startingPlayerID].displayPortfolio()

    def displayPlayerValue(self, playerNumber):
        indexingOffset = 1
        print(f"Player {playerNumber + indexingOffset} ({self._players[playerNumber].getPlayerName()}): ${self._players[playerNumber].getTotalValue()}")

    def viewMyPack(self):
        self._players[self._startingPlayerID].viewCurrentPack()

    def displayPlayerPack(self, playerNumber):
        self._players[playerNumber].viewCurrentPack()

    def displayRankings(self):
        scoreboard = []
        for player in self._players:
            playerScores = (player.getPlayerName(), player.getTotalValue())
            scoreboard.append(playerScores)

        scoreboard = sorted(scoreboard, key = lambda score: score[1], reverse = True)
        indexingOffset = 1
        print(f"Scoreboard")
        print(f"Rank | Player Name | Portfolio Value ($)")
        for playerNumber in range(self._numberOfPlayers):
            rank = playerNumber + indexingOffset
            print(f"{rank}. {scoreboard[playerNumber]}")   
    
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

    def takeStockFromPack(self, playerNumber, stockNumber):
        self._players[playerNumber].takeStockFromPack(stockNumber)
        '''Try to pick a stock, if the'''

    def askUserToPickStock(self):
        userEntry = input("Which stock would you like to select? (Enter a number)")
        self.takeStockFromPack(self._startingPlayerID, int(userEntry))
        print(f"You have added {self._players[self._startingPlayerID].getMostRecentPick()} to your portfolio")
        '''Try to pass an int, if its not an int repeat'''
    
    def draftStock(self):
        indexingOffset = 1
        for player in self._players:
            playerNumber = player.getPlayerNumber() - indexingOffset
            if self.thisIsStartingPlayer(playerNumber):
                self.askUserToPickStock()
            else:
                stocksRemainingInPack = player.getCurrentPack().getStocksRemaining()
                randomStock = random.randrange(stocksRemainingInPack)
                self.takeStockFromPack(playerNumber, randomStock)

    def passPacks(self):
        indexingOffset = 1
        currentPacks = []
        for players in self._players:
            currentPacks.append(players.getCurrentPack())
        
        if self.passingForwards():
            for playerNumber in range(self._numberOfPlayers): 
                if self.thisIsStartingPlayer(playerNumber):
                    lastPlayer = self._numberOfPlayers - indexingOffset
                    self._players[playerNumber].setCurrentPack(currentPacks[lastPlayer]) 
                else:
                    previousPlayer = playerNumber - indexingOffset
                    self._players[playerNumber].setCurrentPack(currentPacks[previousPlayer])             
        else:
            for playerNumber in range(self._numberOfPlayers):
                if self.thisIsLastPlayer(playerNumber):
                    self._players[playerNumber].setCurrentPack(currentPacks[self._startingPlayerID]) 
                else:
                    nextPlayer = playerNumber + indexingOffset
                    self._players[playerNumber].setCurrentPack(currentPacks[nextPlayer]) 

    def playAgain(self):
        playToken = input("Would you like to play again? (y/n?)").lower()
        if playToken == "y":
            return True
        elif playToken == "n":
            return False
        else:
            print("Please enter y or n.")