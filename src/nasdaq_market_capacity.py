# Program Name : nasdaq_market_capacity.py
# Description  : Use API, download data from data.nasdaq.com
#              : Five market capacities of particular shocks will be downloaded:
#              : 1) Market Capacity for Apple Inc.              (APPL)
#                2) Market Capacity for VISA                    (V)
#                3) Market Capacity for Master Card             (MA)
#                4) Market Capacity for Costco                  (COST)
#
#################################################################################

# Official Nasdaq Data Link API Client for Python
# https://pypi.org/project/Nasdaq-Data-Link/
# pip install Nasdaq-Data-Link
import nasdaqdatalink

import pandas as pd
import csv
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("api_key")
nasdaqdatalink.ApiConfig.api_key = API_KEY
dataPath = os.environ.get("marketcapacityPATH_data")
startDate = "2011-01-01"
endDate = "2014-12-31"

# Stock List
stock_lists=['AAPL', 'V', 'MA', 'COST']

for stock in stock_lists:
    marketCapStock = "BATS/BATS_" + stock
    fileName = dataPath + "Market_Capacity_" + stock + '.csv'
    tempData  = nasdaqdatalink.get(marketCapStock,start_date=startDate, end_date=endDate)
    tempData["ticker"] = stock  
    tempData.to_csv(fileName)
    fileName = ""
    marketCapStock = ""
