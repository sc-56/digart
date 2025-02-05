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
        "check_table" : "SELECT * FROM jpword;",
        "check_schema" : "PRAGMA table_info(jpword)",
        "value_insert" : "INSERT into jpword (word, pronunciation, explanation) VALUES (?, ?, ?);" 
        }

    def check_table(self):
        self.cur.execute(self.sql_dict["check_jpword"])
        print(self.cur.fetchall())

    def check_db(self):
        self.cur.execute(self.sql_dict["check_db"])
        print(self.cur.fetchall())

    def execute_statement(self, statement):
        print("###########")
        self.cur.execute(statement)
        #print("The updated value:")
        #print(self.cur.fetchall())
        self.con.commit()

        #print("The value of jpword:")
        self.cur.execute("SELECT * FROM jpword;")
        #print(self.cur.fetchall())
        return self.cur.fetchall()

    def add_csv(self, csv_file):
        with open(csv_file) as file:
            reader = csv.reader(file)
            for row in reader:
                word = row[0]
                pronunce = row[1]
                explain = row[2]
                self.cur.execute(self.sql_dict["value_insert"], value_insert, (word, pronunce, explain))
            self.con.commit()
            print("Values have been added.")

def main():
    do = Database_Operator("./jpword.db")
    do.check_db()
    
if __name__ == "__main__":
    main()
