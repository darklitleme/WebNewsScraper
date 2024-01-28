
import psycopg
import os
from dotenv import dotenv_values

from datetime import datetime


def getOneStock(token):
    # Connect to an existing database
    dbURL=config = dotenv_values(".env.development.local") 

    with psycopg.connect(dbURL["POSTGRES_URL"]) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            try:
                # Execute a command: this creates a new table
                cur.execute("SELECT * FROM stockreview")
                return cur.fetchone()
            except:
                return False

def getListOfTokens():
    # Connect to an existing database
    dbURL=config = dotenv_values(".env.development.local") 

    with psycopg.connect(dbURL["POSTGRES_URL"]) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            try:
                # Execute a command: this creates a new table
                cur.execute("select stocktoken  from stockreview ")
                return cur.fetchone()
            except:
                return False


def addStockToDataBase(token , positive, negative):
    
    if getOneStock(token) != False:
        return False
    # Connect to an existing database
    dbURL=config = dotenv_values(".env.development.local") 

    with psycopg.connect(dbURL["POSTGRES_URL"]) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            cur.execute(
                "INSERT INTO stockreview  values (%s, %s, %s, %s) "),(token , positive, negative, datetime.today().strftime('%Y-%m-%d'))

            # Make the changes to the database persistent
            conn.commit()
            return True

addStockToDataBase("etc" , 44, 72)