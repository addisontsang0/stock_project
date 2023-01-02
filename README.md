<h1>Analysis on US CPI and stock</h1>

<h3>Data Collection and ETL</h3>
<p>Three data tables were generated in the “stock_db” by a series of python programs.  Data flew from the state of extraction, transformation and finally uploading. During the extraction stage, the data files stock, market capacity and cpi would be collected through API from data.nasdaq.com.  Afterwards, selected data would be transformed to suitable format and uploaded onto the Cloud database via MySQL with MySQL-Connector.</p>

Database
1.	stock_db. /* for captured and transformed data (with API) from data.nasdaq.com */

Table Schema for stock_db
1.	stocks - Stock Table
2.	market_capacity - Market Capacity Tables
3.	cpi - Consumer Price Index (CPI)

<h3>Data Warehouse</h3>

<p>Amazon Relational Database Service (AWS RDS), along with the DB engine MySQL, was chosen to operate our relational databases in the AWS Cloud in our project. By connecting AWS RDS and MySQL workbench with the RDS DB instance endpoint, all data was securely uploaded onto the Cloud and successfully retrieved by other admin users for further data analysis. On RDS, two connected databases have been deployed using MySQL script, which respectively contains three tables for raw-data storage and three tables for transformed-data analysis. We designed to scale our databases separately because of better security and higher efficiency.</p>

Data Warehouse
1.	stock_warehouse /* Clean data for data analysis and data visualisation */

Table Schema for stock_warehouse
1.	BI_stocks – stocks for data analysis
2.	BI_stock_mth – consolidated stocks for analysis by month 
3.	BI_cpi – consolidated cpi data

<h3>Data Visualisation</h3>

<p>Microsoft Power BI is the data visualisation tool for presenting the behaviour of the dataset by creating a report for our project. It is only allowed to be installed on Microsoft Windows OS and needs to be connected with the MySQL database in our project. The three tables from MySQL data warehouse were imported for analysis. DAX (Data Analysis Expressions) was chosen to analyse the data because data can be better understood and interpreted. Through its library of functions and operators, it builds formulas and expressions to simplify the task.</p>

