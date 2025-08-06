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

import draftingGame

Coke = classes.Stock(brandName = "Coca-Cola", brandType = "Food & Beverage", rarity = "Common", value = 3000)
print(Coke.getRarity())
print(Coke.setRarity("Rare"))
print(Coke.getRarity())

Pepsi = classes.Stock(brandName = "Pepsi", brandType = "Food & Beverage", rarity = "Uncommon", value = 3000)
print(Pepsi.getRarity())
print(Pepsi.setRarity("Legendary"))
print(Pepsi.getRarity())

Solo = classes.Stock(brandName = "Solo", brandType = "Food & Beverage", rarity = "Rare", value = 4500)

pack1 = classes.Pack([Coke, Pepsi, Solo], 1, 2)
pack1.displayPackContents()
pack1.removeStock(Coke)
print("        ")
pack1.displayPackContents()
print(pack1.getStock(0))
print("        ")
print("        ")

player1 = classes.Player("Josh", 1)
portfolio1 = classes.Portfolio(player1.getPlayerName())
portfolio1.addStock(Coke)
portfolio1.addStock(Pepsi)
portfolio1.displayPortfolio()
print("        ")
print("        ")
player1.assignPortfolio(portfolio1)
player1.displayPortfolio()

numberOfPlayers = int(input("How many players would you like to add?"))
game = classes.Game(numberOfPlayers)
game.createPlayers()
game.displayPlayers()
print(game.displayPlayerValue(0))

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