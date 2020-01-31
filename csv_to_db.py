import sqlite3
import pandas as pd

# load data
df = pd.read_csv('top50.csv')

# strip whitespace from headers
df.columns = df.columns.str.strip()

con = sqlite3.connect("top50.db")

# drop data into database
df.to_sql("MyTable", con)

con.close()