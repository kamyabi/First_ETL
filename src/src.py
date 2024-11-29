#!/usr/bin/env python
# coding: utf-8


def extract_data(Api_key , symbol , url):
    
    try:
        response = req.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        logging.info("Data fetched successfully.")
        
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        raise
    
    return(data)


# In[8]:


def Transform_data (df):
    
    try:
        df = pd.DataFrame.from_dict(data['Time Series (Daily)'],orient='index')
        df.columns = ['open' , 'high' , 'low' , 'close' , 'volume']
        df.index = pd.to_datetime(df.index)
        df = df.apply(pd.to_numeric)
        df['Moving_avg'] = df['close'].rolling(window=5).mean()
    
    except Excemption as e:
        logging.error(f"Data processing failed! : {e}")
        
        
    return(df)


# In[9]:


def Load_data(db_name , db_user , db_password , db_host , db_port):
    
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    try:
        with engine.connect() as connection:
            logging.info("Connection successful!")
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
    
    df.to_sql('stock_prices', engine, if_exists='replace', index=True)
    logging.info("Data stored in PostgreSQL successfully!")


# In[10]:


def plot_data(df):
    
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['close'], label='Close Price')
    plt.plot(df.index, df['Moving_avg'], label='5-Day Moving Average', linestyle='--')
    plt.legend()
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
    


# In[11]:


#main
import requests as req
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import logging

Api_key = "#your api key"
symbol = "#type your symbol"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&interval=5min&apikey={Api_key}'

db_name = '#your db name'
db_user = '#your user name'
db_password = '#your password'
db_host = '#your db host address'
db_port = '#your db port'

logging.basicConfig(
    level=logging.INFO,  # Set the level of detail for logs (INFO and above will be shown)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of log messages
    handlers=[
        logging.FileHandler("project.log"),  # Save logs to a file named project.log
        logging.StreamHandler()             # Also print logs to the console
    ]
)


data = extract_data(Api_key , symbol , url)
df = Transform_data(data)

Load_data(db_name , db_user , db_password , db_host , db_port)

plot_data(df)

