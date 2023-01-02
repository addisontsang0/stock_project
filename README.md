Data Collection and ETL
Three data tables were generated in the “stock_db” by a series of python programs.  Data flew from the state of extraction, transformation and finally uploading. During the extraction stage, the data files stock, market capacity and cpi would be collected through API from data.nasdaq.com.  Afterwards, selected data would be transformed to suitable format and uploaded onto the Cloud database via MySQL with MySQL-Connector.  

Database
1.	stock_db. /* for captured and transformed data (with API) from data.nasdaq.com */

Table Schema for stock_db
1.	stocks - Stock Table
2.	market_capacity - Market Capacity Tables
3.	cpi - Consumer Price Index (CPI)

1) stocks (Consolidate_Stocks.csv)

Index	Field Name	Description
1	seq_number	Record sequence number
2	ticker	Stock code
3	txdate	Transaction date
4	open_price	Opening price
5	day_high	Day High
6	day_low	Day Low
7	close_price	Closing price
8	ex_dividend	Dividend
9	split_ratio	Stock split ratio
10	adj_open	Adjusted opening price
11	adj_high	Adjusted high price
12	adj_low	Adjusted low price
13	adj_close	Adjusted closing price
14	adj_volume	Adjusted transaction volume






2) market_capacity (Consolidate_Market_Capacity.csv)

Index	Field Name	Description
1	seq_number	Sequence number
2	ticker	Stock code
3	txdate	Transaction date
4	short_vol	Short volume
5	total_vol	Total volume

3) cpi (USA_Transformed_CPI.csv)

Index	Field Name	Description
1	seq_number	Sequence number
2	txdate	Transaction date
3	CPI	Consumer Price Index per month


Function Listing

	Function	Description
1	.env	Environment files
2	requirements.txt	Installation package requirement files
3	connect_db.py	Database connection
4	nasdaq_cpi_data.py	Collect CPI data
5	nasdaq_market_capacity.py	Collect market capacity data
6	nasdaq_stock_data.py	Collect stock data
7	transform_cpi_data.py	Transform CPI data
8	transform_market_capacity.py	Transform market capacity data
9	transform_stock_data.py	Transform stock data
10	load_data.py	Load data to database


 
Data Warehouse

Amazon Relational Database Service (AWS RDS), along with the DB engine MySQL, was chosen to operate our relational databases in the AWS Cloud in our project. By connecting AWS RDS and MySQL workbench with the RDS DB instance endpoint, all data was securely uploaded onto the Cloud and successfully retrieved by other admin users for further data analysis. On RDS, two connected databases have been deployed using MySQL script, which respectively contains three tables for raw-data storage and three tables for transformed-data analysis. We designed to scale our databases separately because of better security and higher efficiency.  

Data Warehouse
1.	stock_warehouse /* Clean data for data analysis and data visualisation */

Table Schema for stock_warehouse
1.	BI_stocks – stocks for data analysis
2.	BI_stock_mth – consolidated stocks for analysis by month 
3.	BI_cpi – consolidated cpi data

1) BI_stocks

Index	Field Name	Description
1	ticker	Stock code
2	txdate	Transaction date
3	open_price	Opening price
4	day_high	Day High
5	day_low	Day Low
6	close_price	Closing price
7	ex_dividend	Dividend
8	short_vol	Short volume
9	total_vol	Total volume













2) BI_stocks_mth

Index	Field Name	Description
1	ticker	Stock code
2	yearMonth	Transaction date
3	mth_open_price	Opening price
4	mth_day_high	Day High
5	mth_day_low	Day Low
6	mth_close_price	Closing price
7	mth_short_vol	Short volume
8	mth_total_vol	Total volume


3) BI_cpi

Index	Field Name	Description
1	txdate	Transaction date
2	cpi	Consumer Price Index per month


The SQL Scripts For The Database

/* database (raw data) */
Create database stock_db;
use stock_db;

/* Tables for Samuel's raw data: stocks, market_capacity, CPI */
Create table stocks (
	seq_number int UNSIGNED not null AUTO_INCREMENT,
	ticker VARCHAR(7),
txdate date,
open_price decimal(10, 3),
day_high decimal(10, 3),
day_low decimal(10, 3),
close_price decimal(10, 3),
ex_dividend decimal(5, 3),
split_ratio decimal(4, 2),
adj_open decimal(10, 3),
adj_high decimal(10, 3),
adj_low decimal(10, 3),
adj_close decimal(10, 3),
adj_volume int(15),
    PRIMARY KEY (seq_number)
);

Create table market_capacity (
	seq_number int UNSIGNED not null AUTO_INCREMENT,
    	ticker VARCHAR(7),
	txdate date,
    	short_vol int(15),
    	total_vol int(15),
    PRIMARY KEY (seq_number)
    );

Create table cpi (
	seq_number int UNSIGNED not null AUTO_INCREMENT,
	txdate date,
    	CPI decimal(10, 4),
    PRIMARY KEY (seq_number) 
);




The SQL Scripts For Data Warehouse

/* data warehouse (data analysis) */
CREATE DATABASE stock_warehouse;

USE stock_warehouse;
/* Tables Addison's BI analysis: BI_stocks, BI_stocks_mth, BI_cpi */
CREATE TABLE BI_stocks SELECT stocks.ticker, stocks.txdate, stocks.open_price, stocks.day_high, stocks.day_low, stocks.close_price, stocks.ex_dividend, market_capacity.short_vol, market_capacity.total_vol
	FROM stock_db.stocks
	LEFT JOIN stock_db.market_capacity
    USING (seq_number);  
    
Create table BI_stocks_mth 
	select ticker, DATE_FORMAT(`txdate`, '%Y-%m') AS yearMonth, 
    	CAST(avg(open_price) AS decimal(10, 3)) AS mth_open_price,
    	CAST(avg(day_high) AS decimal(10, 3)) AS mth_day_high, 
    	CAST(avg(day_low) AS decimal(10, 3)) AS mth_day_low, 
    	CAST(avg(close_price) AS decimal(10, 3)) AS mth_close_price, 
    	CAST(avg(short_vol) AS decimal(15, 2)) AS mth_short_vol, 
    	CAST(avg(total_vol) AS decimal(15, 2)) AS mth_total_vol
    	from BI_stocks
	group by ticker, yearMonth;

CREATE TABLE BI_cpi SELECT txdate, cpi FROM stock_db.cpi;

     



 
Data Visualisation

Microsoft Power BI is the data visualisation tool for presenting the behaviour of the dataset by creating a report for our project. It is only allowed to be installed on Microsoft Windows OS and needs to be connected with the MySQL database in our project. The three tables from MySQL data warehouse were imported for analysis. DAX (Data Analysis Expressions) was chosen to analyse the data because data can be better understood and interpreted. Through its library of functions and operators, it builds formulas and expressions to simplify the task.
![image](https://user-images.githubusercontent.com/84266759/210266787-8e0d8dbe-1c28-478d-8d85-6f50a5538285.png)
