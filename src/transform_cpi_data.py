# Program Name : transform_cpi_data.py
# Description  : Clean, Rename (columns), Reindex, Reformat (e.g. Format the decimal, etc)
#              : for CPI (USA) from file
# Output       : USA_CPI.csv
#
#################################################################################

import pandas as pd
import numpy as np
import csv
import os
from dotenv import load_dotenv

def transform_cpi():
    load_dotenv()
    dataPath_data = os.environ.get("cpiPATH_data")
    dataPath_db = os.environ.get("cpiPATH_db")

    startDate = "2011-01-01"
    endDate = "2014-12-31"

    # For market capacity, prepare and transform the data for each stock
    fileName_data = dataPath_data + 'USA_CPI.csv'
    fileName_db = dataPath_db + 'USA_Transformed_CPI.csv'
    cpiDF = pd.read_csv(fileName_data)
    cpiDF.columns = ['txDate','CPI']
    pd.to_datetime(cpiDF.txDate)
    cpiDF.CPI = cpiDF.CPI.round(2)
    cpiDF.to_csv(fileName_db, index=True)
    cpiDF = pd.read_csv(fileName_db)
    cpiDF.columns = ['seqNo','txDate','CPI']
    cpiDF.set_index('seqNo')
    cpiDF['seqNo'] = cpiDF.index + 1
    cpiDF.to_csv(fileName_db, index=False)

transform_cpi()