# First_ETL
my first simple stock data ETL project

This project is a simple data pipeline that fetches stock price data from the Alpha Vantage API, processes it into a clean and structured format, and stores it in a PostgreSQL database for further analysis. 

Key features:

+  Data Fetching: Retrieves stock data (e.g., "TSLA") using the Alpha Vantage API.
+  Data Transformation: Converts raw JSON into a structured Pandas DataFrame, processes the data (e.g., converts to numeric values, computes a 5-day moving average), and ensures timestamps are correctly formatted.
+  Database Integration: Stores the processed data into a PostgreSQL database table for persistence and scalability.
+  Logging: Implements a robust logging mechanism to monitor pipeline progress and handle errors effectively.


-  Future updates will include Apache Airflow to automate and orchestrate the entire pipeline, enabling scheduling, monitoring, and enhanced workflow management.


