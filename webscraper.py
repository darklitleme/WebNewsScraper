from talktodatabase import getOneStock , getListOfTokens , getAllStock
import os.path

StockToSearch = "BTC-USD"

def getTokenList():
    re = list( getListOfTokens())

    return re

def getAllInfo():
    return getAllStock()

 
def getTokenSentimentFromDataBase(token):
    reply = getOneStock(token)
    if reply == False:
        return 0,0,0,0
    return reply
#positive , negative = getTokenSentiment(StockToSearch)
print (getAllInfo())