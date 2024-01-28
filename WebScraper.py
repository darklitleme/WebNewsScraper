import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from finbert_utils import estimate_sentiment

StockToSearch = "BTC-USD"


def get_sentiment(news):
    probability, sentiment = estimate_sentiment(news)
    return probability, sentiment 


def searchYahoo(Token):
    no_of_pagedowns = 20
    URL = "https://finance.yahoo.com/quote/" + Token
    driver = webdriver.Firefox()
    # Navigate to Url
    driver.get(URL)
    time.sleep(1)
    elem = driver.find_element(By.TAG_NAME, 'body')
    moreDown = no_of_pagedowns

    while no_of_pagedowns:
        counter = no_of_pagedowns
        while counter < moreDown:

            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            counter = counter+1

        time.sleep(1)
        no_of_pagedowns-=1
        # Get all the elements available with tag name 'p'

    elements = driver.find_elements(By.TAG_NAME, 'h3')

    count = 0

    while count < 18:
        del elements[count]
        count = count+1
    return elements

def getTokenSentiment(token):
    headlines = searchYahoo(token)
    numberOfHeadlines = len(headlines)
    positive = 0
    negative = 0
    neutral = 0

    for headline in headlines:
        probability, sentiment = get_sentiment(headline.text)
        if sentiment == "positive":
            positive =  positive+1
        elif sentiment == "negative":
            negative=negative+1
        else:
            neutral = neutral + 1

    percentageOfPos = ( positive / numberOfHeadlines) * 100
    percentageOfNeg = ( negative /numberOfHeadlines) * 100
        
    return percentageOfPos, percentageOfNeg



#positive , negative = getTokenSentiment(StockToSearch)

