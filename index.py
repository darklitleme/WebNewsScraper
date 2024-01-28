from WebScraper import getTokenSentiment
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "jess is stinky"

@app.route("/getStockReview", methods=['GET'])
def getStockInfo():
    stockToGet = request.args.get('stock')
    positive , negative = getTokenSentiment(stockToGet)
    return (
        "positive = " , positive,
        "negative = " , negative)
