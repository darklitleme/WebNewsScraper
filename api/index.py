
import json
from flask import Flask, request



from WebScraper import getTokenSentimentFromDataBase

app = Flask(__name__)

@app.route("/API")
def hello_world():
    return "jess is stinky"

@app.route("/getStockReview", methods=['GET'])
def getStockInfo():
    stockToGet = request.args.get('stock')
    positive , negative = getTokenSentimentFromDataBase(stockToGet)
    return (
        "positive = " , positive,
        "negative = " , negative)
