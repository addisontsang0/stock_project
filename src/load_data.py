# Project      : Showcase Project
# Program Name : load_data.py
# Description  : Load the transformed data to database/AWS
#              : Load a consolidated stock csv files to database
#              :    1) Consolidate_Stocks.csv
#              :    2) USA_CPI.csv
#              :    3) A market capacity csv file consolidates AAPL, V, MA & COST
# Outputs      : Data in the remote database (e.g. MySQL/RDS under AWS)
# Developers   : Addison/ Vaness/ Samuel
###############################################################################################

import pandas as pd
import mysql_connector as db
import os
from dotenv import load_dotenv

def insert_to_stock_db():
    load_dotenv()

    # Establish the database connection
    connection = db.mysql_connect()

    ############### Upload Consolidated Stock Prices #############
    dataPath_db = os.environ.get("stockPATH_db")
    fileName = dataPath_db + 'Consolidate_Stocks.csv'
    # inserting stocks data to MySQL database (or to RDS in AWS)
    stockData = pd.read_csv (fileName)  
    print("Begin") 
    row_count=1
    for row in stockData.itertuples():
        sql = """
        INSERT INTO stocks (
            seq_number, ticker, txDate, open_price, day_high,
            day_low, close_price, ex_dividend,
            split_ratio, adj_open, adj_high,
            adj_low, adj_close, adj_volume)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """ 
        val = (row.seqNo, row.ticker, 
        row.date, row.open, row.high,
        row.low, row.close, row.ex_dividend,
        row.split_ratio, row.adj_open, row.adj_high,
        row.adj_low, row.adj_close, row.adj_volume)
        cursor = connection.cursor()
        cursor.execute(sql, val)
        row_count +=1
        print("--"+str(row_count))

    ####################### Upload CPI Data #####################
    # inserting CPI data to MySQL database (or to RDS in AWS)
    dataPath_db = os.environ.get("cpiPATH_db")
    fileName = dataPath_db + 'USA_Transformed_CPI.csv'
    cpiData = pd.read_csv (fileName)   
    print("Begin5")
    for row in cpiData.itertuples():
        sql = """
        INSERT INTO cpi (
            seq_number, txDate, cpi)
            VALUES (%s,%s,%s)
        """ 
        val = (row.seqNo, row.txDate, row.CPI)
        cursor = connection.cursor()
        cursor.execute(sql, val)

    ####################### Upload Market Capacity #####################
    # For four selected stocks, inserting market capacity data 
    # to MySQL database (or to RDS in AWS)
    dataPath_db = os.environ.get("marketcapacityPATH_db")
    fileName = dataPath_db + 'Consolidate_Market_Capacity.csv'
    marketcapacityData = pd.read_csv (fileName)   
    for row in marketcapacityData.itertuples():
        sql = """
        INSERT INTO market_capacity (
            seq_number, ticker, txdate, short_vol, total_vol)
            VALUES (%s,%s,%s,%s,%s)
        """ 
        val = (row.seqNo, row.ticker, row.txDate, row.shortVol, row.totVol)
        cursor = connection.cursor()
        cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    print("All Data Uploaded!.")

def load_data_to_db():
    # Upload all data to MySQL/ RDS in AWS
    # 1) Stocks data
    # 2) CPI data
    # 3) Single table which consolidates the market capacity 
    #    for stocks : AAPL, V, MA and COST
    insert_to_stock_db()

load_data_to_db()