# Project      : Showcase Project
# Program Name : nasdaq_stock_data.py
# Description  : Use API, download data from data.nasdaq.com
#              : Five types of historical data will be downloaded:
#              :    1) Apple Inc.              (APPL)
#                   2) VISA                    (V)
#                   3) Master Card             (MA)
#                   4) Costco                  (COST)
#                The data (12 fields) download for each stock include:
#                   1) Transaction Date 2) Open Price 3) High Price and 4) Low Price for the data
#                   5) Closing Price for the date 6) Ex-Dividend 7) Split Ration
#                   8) Adjust Open Price 9) Adjust High Price 10) Adjust Low Price
#                   11) Adjust Close Price and 12) Adjust Volumn for the date
# Outputs      : Generate four csv files, namely : APPL.csv, V.csv, MA.csv, COST.csv
# Developers   : Addison/ Vaness/ Samuel
###############################################################################################

import os
from dotenv import load_dotenv
# Official Nasdaq Data Link API Client for Python
# https://pypi.org/project/Nasdaq-Data-Link/
# pip install Nasdaq-Data-Link
import nasdaqdatalink

import pandas as pd
import csv

def get_data_from_nasdaq():

    # Load environment variables
    load_dotenv()
    API_KEY = os.environ.get("api_key")
    nasdaqdatalink.ApiConfig.api_key = API_KEY
    dataPath = os.environ.get("stockPATH_data")

    # Create a required list to collect the data via the API from data.nasdaq.com
    # Namely, APPL, V, MA, COST

    # stock_lists = ['AAPL', 'V', 'MA', 'COST']  Original wanted stock but
    # MA and COST return no data!!!!!
    stock_lists = ['AAPL', 'V', 'MA', 'COST']

    strDate = '2011-01-01'
    endDate = '2014-12-31'

    for stock in stock_lists:
        fileName = dataPath + stock + '.csv'
        # Get data via API from nasdaqdatalink
        tempData = nasdaqdatalink.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'open', 'high', 'low','close','ex-dividend','split_ratio','adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume'] }, ticker = [stock], date = { 'gte': strDate, 'lte': endDate })
        tempData.to_csv(fileName)
        fileName = ''

get_data_from_nasdaq()