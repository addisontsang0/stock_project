# Program Name : transform_stock_data.py
# Description  : Clean, Rename (columns), Reindex, Reformat (e.g. Format the decimal, etc)
#              : for four shocks :-
#              :    1) Market Capacity for Apple Inc.      (APPL)
#                   2) Market Capacity for VISA            (V)
#                   3) Market Capacity for Master Card     (MA)
#                   4) Market Capacity for Costco          (COST)
# Output       : then combine all stocks into one final .csv file
#
#################################################################################

import pandas as pd
import numpy as np
import csv
import os
from dotenv import load_dotenv

load_dotenv()
# Prepare the output path for consolidating stock prices into one file
dataPath_data = os.environ.get("stockPATH_data")
dataPath_db = os.environ.get("stockPATH_db")

def transform_stock():
    startDate = "2011-01-01"
    endDate = "2014-12-31"

    # Stock List
    stock_lists=['AAPL', 'V', 'MA', 'COST']

    # For market capacity, prepare and transform the data for each stock
    for stock in stock_lists:
        fileName_data = dataPath_data + stock + '.csv'
        fileName_db = dataPath_db + "Transformed_" + stock + '.csv' 
        df = pd.read_csv(fileName_data)
        df.columns = ['seqNo','ticker','date','open','high','low','close','ex_dividend','split_ratio','adj_open','adj_high','adj_low','adj_close','adj_volume']
        df = df.reindex(columns=['seqNo','ticker','date','open','high','low','close','ex_dividend','split_ratio','adj_open','adj_high','adj_low','adj_close','adj_volume'])
        pd.to_datetime(df.date)
        df.open = df.open.round(2)
        df.high = df.high.round(2)
        df.low = df.low.round(2)
        df.close = df.close.round(2)
        df.adj_open = df.adj_open.round(2)
        df.adj_high = df.adj_high.round(2)
        df.adj_low = df.adj_low.round(2)
        df.adj_close = df.adj_close.round(2)
        df.adj_volume = df.adj_volume.astype(np.int64)
        df.set_index('seqNo')
        df['seqNo'] = df.index + 1
        df.to_csv(fileName_db, index=False)
        fileName = ""
    
def merge_stock_data():
    # Stock List
    stock_lists=['AAPL', 'V', 'MA', 'COST']
 
    df_final = pd.DataFrame()
    for stock in stock_lists:
        fileName_data = dataPath_db + "Transformed_" + stock + '.csv' 
        fileName_db = dataPath_db + "Consolidate_Stocks" + '.csv' 
        df = pd.read_csv(fileName_data)
        df_final = df_final.append(df, ignore_index=True)

    df_final.set_index('seqNo')
    df_final['seqNo'] = df_final.index + 1
    df_final.to_csv(fileName_db, index=False)

transform_stock()
merge_stock_data()