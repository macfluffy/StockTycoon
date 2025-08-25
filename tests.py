import pytest
import stockTyGameEngine

def testPassed():
    print("Test Passed!")

def testStockName(stock, testCondition):
    print("Comparing the stock names.....")
    assert stock.getBrandName() == testCondition, "The stock's brand name does not match!"
    testPassed()

def testStockType(stock, testCondition):
    print("Comparing the stock brand types.....")
    assert stock.getBrandType() == testCondition, "The stock's brand type does not match!"
    testPassed()

def testStockRarity(stock, testCondition):
    print("Comparing the stock rarities.....")
    assert stock.getRarity() == testCondition, "The stock's rarity does not match!"
    testPassed()

def testStockValue(stock, testCondition):
    print("Comparing the stock values.....")
    assert stock.getValue() == testCondition, "The stock's value is different!"
    testPassed()

def testStock(stock, brandName, brandType, rarity, value):
    print("Testing Stock was created correctly.....")
    testStockName(stock, brandName)
    testStockType(stock, brandType)
    testStockRarity(stock, rarity)
    testStockValue(stock, value)
    
def testPlayerName(player, testCondition):
    print("Comparing the player names.....")
    assert player.getPlayerName() == testCondition, "The player names do no match!"
    testPassed()

def testPlayerNumber(player, testCondition):
    print("Comparing the player numbers.....")
    assert player.getPlayerNumber() == testCondition, "The player numbers do not match!"
    testPassed()

def testPlayerCreation(player, playerName, playerNumber):
    print("Testing player was created correctly.....")
    testPlayerName(player, playerName)
    testPlayerNumber(player, playerNumber)

if __name__ == '__main__':
    testBrandName = "Coca-Cola"
    testBrandType = "Food & Beverage"
    testRarity = "Common"
    testValue = 3000
    Coke = stockTyGameEngine.Stock(brandName = testBrandName,
                                   brandType = testBrandType,
                                   rarity = testRarity,
                                   value = testValue)
    testStock(stock = Coke,
              brandName = testBrandName,
              brandType = testBrandType,
              rarity = testRarity,
              value = testValue)
    
    dummyPlayerName = "Test Player"
    dummyPlayersNumber = 1
    testPlayer = stockTyGameEngine.Player(playerName = dummyPlayerName,
                                          playerNumber = dummyPlayersNumber)
    testPlayerCreation(player = testPlayer,
                       playerName = dummyPlayerName,
                       playerNumber = dummyPlayersNumber)
    
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