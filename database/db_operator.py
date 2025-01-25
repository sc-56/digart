import pandas as pd
import sqlite3 
import csv

create_table = "CREATE TABLE jpword(word, pronunciation, explanation);"

check_table = "SELECT name FROM sqlite_master WHERE type='table';"

check_jpword = "SELECT * FROM jpword;"

check_schema = "PRAGMA table_info(jpword);"

value_insert = "INSERT into jpword (word, pronunciation, explanation) VALUES (?, ?, ?);" 

delete_values = "DELETE FROM jpword;"
# The question mark here works like one place holder for query. 

def execute_statement(con, cur, statement):
    print("###########")
    cur.execute(statement)
    print("The updated value:")
    print(cur.fetchall())
    con.commit()

    print("The value of jpword:")
    cur.execute("SELECT * FROM jpword;")
    print(cur.fetchall())

    return cur.fetchall()

def connect_db(file):
    # df = pd.read_csv(file) # ['word', ' pronunciation', ' explanation']
    con = sqlite3.connect(file)
    cur = con.cursor()
    return con, cur

def add_csv(csv_file, db_file, con, cur):
    with open(csv_file) as file:
        reader = csv.reader(file)
        for row in reader:
            word = row[0]
            pronunce = row[1]
            explain = row[2]
            cur.execute(value_insert, (word, pronunce, explain))
        con.commit()
        print("Values have been added.")

def main():
    con, cur = connect_db("./jpword.db")
    execute_statement(con, cur, delete_values)
    # add_csv("./jpword.csv", "./jpword.db", con, cur)
    
if __name__ == "__main__":
    main()

'''



## Add CSV file into database

### with statement in Python

The current task is to open the csv file. The with statement is always used in opening the file, network connect and database connect. The functionality of "with" is to ensure that the resource cannot be leaked. 

The __enter__() and __exit__() are two specific functions for the object "with". Two methods are named as context manager.

### file object 

file is returned by the function open(). File is one class. From its name, it can be deduced that it is one fundamental 

If the file existed, which means the database exists. Therefore, it could be usd to be connected. 

If everything is object, it could mean that every function could be added to one object, which is the action of that object. 

###  

After connection, you may need to check all the existed tables in the database. There is one command as below:

SELECT name FROM sqlite_master WHERE type='table';

After selection from table, it is found that the variable table is one 

The statement "PRAGMA" provides the list of columns. 

It seems that sqlite can totally be operated by python. 

一转眼回家20天了；还有20天又可以离开这里了；我在家乡放弃了一切，同时找到了自己想做的事情。

'''