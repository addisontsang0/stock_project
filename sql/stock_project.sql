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
LOAD DATA LOCAL INFILE '~/Desktop/AVS-Project/db/stock_price/Consolidate_Stocks.csv' INTO TABLE stocks
	 COLUMNS TERMINATED BY ','
     ignore 1 rows;

Create table market_capacity (
	seq_number int UNSIGNED not null AUTO_INCREMENT,
    ticker VARCHAR(7),
	txdate date,
    short_vol int(15),
    total_vol int(15),
    PRIMARY KEY (seq_number)
    );
LOAD DATA LOCAL INFILE '~/Desktop/AVS-Project/db/market_capacity/Consolidate_Market_Capacity.csv' INTO TABLE market_capacity
	 COLUMNS TERMINATED BY ','
     ignore 1 rows;

Create table cpi (
	seq_number int UNSIGNED not null AUTO_INCREMENT,
	txdate date,
    CPI decimal(10, 4),
	PRIMARY KEY (seq_number) 
);
LOAD DATA LOCAL INFILE '~/Desktop/AVS-Project/db/cpi/USA_Transformed_CPI.csv' INTO TABLE cpi
	 COLUMNS TERMINATED BY ','
     ignore 1 rows;
     
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
