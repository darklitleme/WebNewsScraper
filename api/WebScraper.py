from talkToDataBase import getOneStock
import os.path

StockToSearch = "BTC-USD"


def getTokenSentimentFromDataBase(token):
    return getOneStock(token)

#positive , negative = getTokenSentiment(StockToSearch)
