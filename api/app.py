from flask import Flask, request

#from webscraper import getTokenSentimentFromDataBase

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "jess is stinky"
@app.route("/api")
def hello_world():
    return "hi bayley"

@app.route("/getStockReview", methods=['GET'])
def getStockInfo():
    #stockToGet = request.args.get('stock')
    #positive , negative = getTokenSentimentFromDataBase(stockToGet)
    #return (
       # "positive = " , positive,
        #"negative = " , negative)
    return "bitcoin!"