import pytest
import stockTyGameEngine

class tester:
    def __init__(self, testType):
        self._testType = testType

    def testPassed(self):
        print("Test Passed!")


class stockTester(tester):
    def __init__(self, testType, brandName, brandType, rarity, value):
        super().__init__(testType)
        self._brandName = brandName
        self._brandType = brandType
        self._rarity = rarity
        self._value = value
        self._generatedStock = stockTyGameEngine.Stock(brandName = self._brandName,
                                                       brandType = self._brandType,
                                                       rarity = self._rarity,
                                                       value = self._value)

    def testStockName(self):
        print("Comparing the stock names.....")
        assert self._generatedStock.getBrandName() == self._brandName, "The stock's brand name does not match!"
        self.testPassed()

    def testStockType(self):
        print("Comparing the stock brand types.....")
        assert self._generatedStock.getBrandType() == self._brandType, "The stock's brand type does not match!"
        self.testPassed()

    def testStockRarity(self):
        print("Comparing the stock rarities.....")
        assert self._generatedStock.getRarity() == self._rarity, "The stock's rarity does not match!"
        self.testPassed()

    def testStockValue(self):
        print("Comparing the stock values.....")
        assert self._generatedStock.getValue() == self._value, "The stock's value is different!"
        self.testPassed()

    def testStockCreation(self):
        print("Testing Stock was created correctly.....")
        self.testStockName()
        self.testStockType()
        self.testStockRarity()
        self.testStockValue()


class playerCreationTester(tester):
    def __init__(self, testType, playerName, playerNumber):
        super().__init__(testType)
        self._playerName = playerName
        self._playerNumber = playerNumber
        self._generatedPlayer = stockTyGameEngine.Player(playerName = self._playerName,
                                                         playerNumber = self._playerNumber)
    
    def testPlayerName(self):
        print("Comparing the player names.....")
        assert self._generatedPlayer.getPlayerName() == self._playerName, "The player names do no match!"
        self.testPassed()

    def testPlayerNumber(self):
        print("Comparing the player numbers.....")
        assert self._generatedPlayer.getPlayerNumber() == self._playerNumber, "The player numbers do not match!"
        self.testPassed()

    def testPlayerCreation(self):
        print("Testing player was created correctly.....")
        self.testPlayerName()
        self.testPlayerNumber()

    def getGeneratedPlayer(self):
        return self._generatedPlayer


class portfolioTester(tester):
    def __init__(self, testType, owner):
        super().__init__(testType)
        self._owner = owner
        self._generatedPortfolio = stockTyGameEngine.Portfolio(self._owner)
        self._dummyTotalValue = 0

    def testPortfolioValue(self):
        print("Checking the total value of the generated portfolio.....")
        assert self._generatedPortfolio.getTotalValue() == self._dummyTotalValue, "The total values of the portfolios do not match!"
        self.testPassed()


if __name__ == '__main__':
    testBrandName = "Coca-Cola"
    testBrandType = "Food & Beverage"
    testRarity = "Common"
    testValue = 3000
    stockTest = stockTester(testType = "Stock Creation Tester",
                            brandName = testBrandName,
                            brandType = testBrandType,
                            rarity = testRarity,
                            value = testValue)
    stockTest.testStockCreation()
    
    dummyPlayerName = "Test Player"
    dummyPlayersNumber = 1
    playerCreationTest = playerCreationTester(testType = "Player Creation Tester",
                                              playerName = dummyPlayerName,
                                              playerNumber = dummyPlayersNumber)
    playerCreationTest.testPlayerCreation()
    
    portfolioCreationTest = portfolioTester(testType = "Portfolio Creation Tester",
                                            owner = playerCreationTest.getGeneratedPlayer())
    portfolioCreationTest.testPortfolioValue()
    
'''Pepsi = stockTyGameEngine.Stock(brandName = "Pepsi", brandType = "Food & Beverage", rarity = "Uncommon", value = 3000)
    Solo = stockTyGameEngine.Stock(brandName = "Solo", brandType = "Food & Beverage", rarity = "Rare", value = 4500)'''

'''    pack1 = stockTyGameEngine.Pack([Coke, Pepsi, Solo], 1, 2)
    pack1.displayPackContents()
    pack1.removeStock(Coke)
    print("        ")
    pack1.displayPackContents()
    print(pack1.getStock(0))
    print("        ")
    print("        ")
    
    player1 = stockTyGameEngine.Player("Josh", 1)
    portfolio1 = stockTyGameEngine.Portfolio(player1.getPlayerName())
    portfolio1.addStock(Coke)
    portfolio1.addStock(Pepsi)
    portfolio1.displayPortfolio()
    print("        ")
    print("        ")
    player1.assignPortfolio(portfolio1)
    player1.displayPortfolio()

    numberOfPlayers = int(input("How many players would you like to add?"))
    game = stockTyGameEngine.Game(numberOfPlayers)
    game.createPlayers()
    game.displayPlayers()
    print(game.displayPlayerValue(0))'''

'''for x in range(8):
    newGame.viewPlayersPack(x)'''

'''    newGame.nextRound()
    newGame.viewMyPack()
    newGame.askUserToPickStock()
    newGame.displayPlayerPortfolio()
    newGame.passPacks()'''

'''print(f"Pack {playerNumber}")
viewPlayersPack(playerNumber)'''

'''if self.isThisStartingPlayer():
            print(f"You've added {stockTaken.getBrandName()} to your portfolio!")'''