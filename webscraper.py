from talktodatabase import getOneStock , getListOfTokens
import os.path

StockToSearch = "BTC-USD"

def getTokenList():
    re = list( getListOfTokens())

    return re

def getTokenSentimentFromDataBase(token):
    reply = getOneStock(token)
    if reply == False:
        return 0,0,0,0
    return reply
#positive , negative = getTokenSentiment(StockToSearch)
print (getTokenList())