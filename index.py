
from flask import Flask, request

from webscraper import getTokenSentimentFromDataBase , getTokenList

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "jess is stinky"
@app.route("/api")
def hello_their():
    return "hi bayley"

@app.route("/getOneStockReview", methods=['GET'])
def getStockInfo():
    stockToGet = request.args.get('stock')
    token, positive , negative ,date = getTokenSentimentFromDataBase(stockToGet)
    stringToReturn =  " positive," + str(positive) + ","
    return stringToReturn
@app.route("/getTokenList")
def getTokenListReq():
    return getTokenList()