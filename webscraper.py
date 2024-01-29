from talktodatabase import getOneStock , getListOfToken
import os.path

StockToSearch = "BTC-USD"

def getTokenList():
    return getListOfToken()

def getTokenSentimentFromDataBase(token):
    reply = getOneStock(token)
    if reply == False:
        return 0,0,0,0
    return reply
#positive , negative = getTokenSentiment(StockToSearch)
