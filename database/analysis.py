import pandas as pd
import sqlite3 

create_table = "CREATE TABLE jpword(word, pronunciation, explanation)"

def connect_db(file, ):

df = pd.read_csv("jp-word.csv") # ['word', ' pronunciation', ' explanation']
con = sqlite3.connect("create.db")
cur = con.cursor()
cur.execute(create_table)
con.commit()

'''
If the file existed, which means the database exists. Therefore, it could be using 
The file create.db is empty when only using connect(); However, 

'''