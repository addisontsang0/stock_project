/* database (load raw data via python) */
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