import mysql.connector
import pandas as pd
from datetime import datetime

df = pd.read_csv("BTC-USD.csv")

df["Date"] = pd.to_datetime(df["Date"])

database = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root1234"
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS PROJECTS")
cursor.execute("USE PROJECTS")

cursor.execute("CREATE TABLE IF NOT EXISTS BTC_TBL (DATE DATE, OPEN_PRICE FLOAT, CLOSE_PRICE FLOAT)")


df_cleaned = df.dropna(subset=["Date", "Open", "Close"])
df_cleaned["Date"] = pd.to_datetime(df_cleaned["Date"])


data_values = df_cleaned[["Date", "Open", "Close"]].values.tolist()

insert_query = "INSERT INTO BTC_TBL (DATE, OPEN_PRICE, CLOSE_PRICE) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, data_values)

database.commit()
database.close()
