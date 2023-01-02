# Program Name : transform_market_capacity.py
# Description  : Clean, Rename (columns), Reindex, Reformat (e.g. Format the decimal, etc)
#              : for four shocks :-
#              :    1) Market Capacity for Apple Inc.      (APPL)
#                   2) Market Capacity for VISA            (V)
#                   3) Market Capacity for Master Card     (MA)
#                   4) Market Capacity for Costco          (COST)
#
#################################################################################

import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
# stock_lists = os.environ.get("stocks")
dataPath_data = os.environ.get("marketcapacityPATH_data")
dataPath_db = os.environ.get("marketcapacityPATH_db")

def transform_market_capacity():
    startDate = "2011-01-01"
    endDate = "2014-12-31"

    # Stock List
    stock_lists=['AAPL', 'V', 'MA', 'COST']

    for stock in stock_lists:
        fileName_data = dataPath_data + "Market_Capacity_" + stock + '.csv'
        fileName_db = dataPath_db + "Market_Capacity_" + stock + '.csv'
        df = pd.read_csv(fileName_data)
        df.columns = ['txDate','shortVol','totVol','ticker']
        df = df.reindex(columns=['ticker','txDate','shortVol','totVol'])
        
        pd.to_datetime(df.txDate)
        df.shortVol = df.shortVol.astype(np.int64)
        df.totVol = df.totVol.astype(np.int64)
        df.to_csv(fileName_db, index=True)
        df = pd.read_csv(fileName_db)
        df.columns = ['seqNo','ticker','txDate','shortVol','totVol']
        df.set_index('seqNo')
        df['seqNo'] = df.index + 1        
        df.to_csv(fileName_db, index=False)

def merge_market_capacity():
    # Stock List
    stock_lists=['AAPL', 'V', 'MA', 'COST']
 
    df_final = pd.DataFrame()
    for stock in stock_lists:
        fileName_data = dataPath_db + "Market_Capacity_" + stock + '.csv' 
        fileName_db = dataPath_db + "Consolidate_Market_Capacity" + '.csv' 
        df = pd.read_csv(fileName_data)
        df_final = df_final.append(df, ignore_index=True)
        # df.columns = ['seqNo','ticker','txDate','shortVol','totVol']
        df_final.to_csv(fileName_db, index=False)

    # Create Index
    df_final = pd.read_csv(fileName_db)
    df_final.columns = ['seqNo','ticker','txDate','shortVol','totVol']
    df_final.set_index('seqNo')
    df_final['seqNo'] = df_final.index + 1
    df_final.to_csv(fileName_db, index=False)

transform_market_capacity()
merge_market_capacity()