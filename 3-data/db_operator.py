import sqlite3 
import csv

class Database_Operator:

    def __init__(self, db_file):
        # super().__init__()
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        self.con, self.cur = con, cur
        self.db_file = db_file
        self.sql_dict = {
            "create_table" : "CREATE TABLE jpword(word, pronunciation, explanation);" ,
            "check_db" : "SELECT name FROM sqlite_master WHERE type='table';",  
            "check_table" : "SELECT * FROM {0};",
            "check_schema" : "PRAGMA table_info({0})",
            "value_insert" : "INSERT into jpword (word, pronunciation, explanation) VALUES (?, ?, ?);",
            "delete_table": "DROP TABLE IF EXISTS {0}"
        }

    def check_db(self):
        self.cur.execute(self.sql_dict["check_db"])
        print(self.cur.fetchall())
        return self.cur.fetchall()

    def check_table(self, table_name):
        query = self.sql_dict["check_table"].format(table_name)
        self.cur.execute(query)
        print(self.cur.fetchall())
        return self.cur.fetchall()

    def check_schema(self, table_name):
        query = self.sql_dict["check_schema"].format(table_name)
        self.cur.execute(query)
        print(self.cur.fetchall())

    def execute_statement(self, statement):
        self.cur.execute(statement)
        self.con.commit()
        return self.cur.fetchall()

    def add_csv(self, csv_file):
        with open(csv_file) as file:
            reader = csv.reader(file)
            for row in reader:
                word = row[0]
                pronunce = row[1]
                explain = row[2]
                self.cur.execute(self.sql_dict["value_insert"], (word, pronunce, explain))
            self.con.commit()
            print("Values have been added.")
    
    def delete_table(self, table_name):
        self.cur.execute(self.sql_dict["delete_table"].format(table_name))

def main():
    do = Database_Operator("./articles.db")
    do.check_table('articles')

if __name__ == "__main__":
    main()

