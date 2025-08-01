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