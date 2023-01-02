# Project      : Showcase Project
# Program Name : nasdaq_cpi_data.py
# Description  : Use API, download data from data.nasdaq.com
#              : Comsumer Price Index (CPI) for USA (from 2011 to 2014)
# Output       : usa_cpi.csv
# Developers   : Addison/ Vaness/ Samuel
###############################################################################################

import nasdaqdatalink
import pandas as pd
import os
from dotenv import load_dotenv

def get_usa_cpi():
    # Load environment variables
    load_dotenv()

    dataPath_data = os.environ.get("cpiPATH_data")
    fileName = dataPath_data + 'USA_CPI.csv'
    API_KEY = os.environ.get("api_key")

    # Get data via API from nasdaqdatalink
    nasdaqdatalink.ApiConfig.api_key = API_KEY
    cpiData = nasdaqdatalink.get('RATEINF/CPI_USA',start_date="2011-01-01", end_date="2014-12-31")
    cpiData.to_csv(fileName)

get_usa_cpi()