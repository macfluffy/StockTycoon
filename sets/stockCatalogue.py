class StockOptions:
    def __init__(self):
        self._catalogueSetNumber = 1
        self._stockCatalogue = {"Solo": "Food & Beverage",
                                "Pepsi": "Food & Beverage",
                                "Coca-Cola": "Food & Beverage",
                                "McDonald's": "Food & Beverage",
                                "KFC": "Food & Beverage",
                                "Burger King": "Food & Beverage",
                                "Wendy's": "Food & Beverage",
                                "Uniqlo": "Fashion",
                                "H&M": "Fashion",
                                "Politix": "Fashion",
                                "Forever 21": "Fashion",
                                "G-Star": "Fashion",
                                "Just Jeans": "Fashion",
                                "Rolex": "Fashion",
                                "Playstation": "Gaming",
                                "Xbox": "Gaming",
                                "Nintendo": "Gaming",
                                "Steam": "Gaming",
                                "Ubisoft": "Gaming",
                                "Minecraft": "Gaming",
                                "Bandai": "Gaming",
                                "LG": "Appliances",
                                "Dyson": "Appliances",
                                "Soniq": "Appliances",
                                "Hisense": "Appliances",
                                "Westinghouse": "Appliances",
                                "Fisher & Paykel": "Appliances",
                                "Electrolux": "Appliances",
                                "Herald Sun": "News",
                                "The Daily Telegraph": "News",
                                "The Australian": "News",
                                "Sydney Morning Herald": "News",
                                "Australian Financial Review": "News",
                                "The Age": "News",
                                "The Sunday Times": "News"}
        
        self._stockRarities = {"Common": 1000,
                               "Uncommon": 1500,
                               "Rare": 2000,
                               "Epic": 2500,
                               "Legendary": 3000}
        
    def getFullCatalogue(self):
        return (self._stockCatalogue)
    
    def getAllRarities(self):
        return (self._stockRarities)
    
    def getCatalogueSetNumber(self):
        return (self._catalogueSetNumber)