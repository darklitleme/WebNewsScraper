
from flask import Flask, request , jsonify

from webscraper import getTokenSentimentFromDataBase , getTokenList ,getAllInfo

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
    ret = getTokenList()
    return jsonify( {"listOfTokens" :ret })

@app.route("/getNewConfeidence")
def getStockListReq():
    ret = getAllInfo()
    
    return jsonify( ret)
