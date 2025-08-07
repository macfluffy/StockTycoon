import classes
from bots import botNames
from sets import stockCatalogue

def getDefaultPlayerCount():
    defaultNumberOfPlayers = 8
    return defaultNumberOfPlayers

def wantToPlayAgain(playAgain):
    return True if playAgain else False

if __name__ == '__main__':
    gameOver = False
    playToken = True
    
    while playToken:
        # Initialise the Game
        newGame = classes.Game(getDefaultPlayerCount())
        newGame.displayGameBanner()

        # Create the lobby
        nameGenerator = botNames.PlayerNames()
        randomNames = nameGenerator.getAllNames()
        newGame.createPlayers(randomNames)
        newGame.displayGameLobby()

        # Core game loop
        while not gameOver:
            # Generate the packs for the round
            stockGenerator = stockCatalogue.StockOptions()
            stockOptions = stockGenerator.getFullCatalogue()
            stockRarities = stockGenerator.getAllRarities()
            newPack = newGame.generatePacks(stockOptions, stockRarities)
            packsEmpty = newGame.isPackEmpty()
            
            # Show the current round number
            newGame.displayCurrentRound()

            # Draft packs and pass it on until there are no more picks
            while not packsEmpty:
                newGame.viewMyPack()
                newGame.draftStock()
                newGame.displayPlayerPortfolio()
                newGame.passPacks()
                packsEmpty = newGame.isPackEmpty()
                if packsEmpty:
                    gameOver = newGame.gameIsOver()
                    newGame.nextRound()

        # Show the scoreboard
        newGame.displayRankings()

        # Would you like to play again?
        playToken = newGame.playAgain()
        if wantToPlayAgain(playToken):
            gameOver = False