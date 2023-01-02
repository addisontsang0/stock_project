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
