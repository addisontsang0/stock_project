

<h3>Data Collection and ETL</h3>
<p>Three data tables were generated in the “stock_db” by a series of python programs.  Data flew from the state of extraction, transformation and finally uploading. During the extraction stage, the data files stock, market capacity and cpi would be collected through API from data.nasdaq.com.  Afterwards, selected data would be transformed to suitable format and uploaded onto the Cloud database via MySQL with MySQL-Connector.</p>

Database
1.	stock_db. /* for captured and transformed data (with API) from data.nasdaq.com */

Table Schema for stock_db
1.	stocks - Stock Table
2.	market_capacity - Market Capacity Tables
3.	cpi - Consumer Price Index (CPI)
