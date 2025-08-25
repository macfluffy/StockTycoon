import pytest
import stockTyGameEngine

def testPassed():
    print("Test Passed!")

def testStockName(stock, testCondition):
    print("Testing stock name...")
    assert stock.getBrandName() == testCondition, "The stock's brand name does not match!"
    testPassed()

def testStockType(stock, testCondition):
    print("Testing stock brand type")
    assert stock.getBrandType() == testCondition, "The stock's brand type does not match!"
    testPassed()
    
if __name__ == '__main__':
    Coke = stockTyGameEngine.Stock(brandName = "Coca-Cola", brandType = "Food & Beverage", rarity = "Common", value = 3000)
    testStockName(Coke, "Coca-Cola")
    testStockType(Coke, "Food & Beverage")

    print(Coke.getRarity())
    print(Coke.setRarity("Rare"))
    print(Coke.getRarity())

    Pepsi = stockTyGameEngine.Stock(brandName = "Pepsi", brandType = "Food & Beverage", rarity = "Uncommon", value = 3000)
    print(Pepsi.getRarity())
    print(Pepsi.setRarity("Legendary"))
    print(Pepsi.getRarity())

    Solo = stockTyGameEngine.Stock(brandName = "Solo", brandType = "Food & Beverage", rarity = "Rare", value = 4500)

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