import sys
import os
sys.path.append(os.path.abspath('/Users/apple/Documents/0-Programming/digart/3-data'))

from flask import Flask
from db_operator import Database_Operator

app = Flask(__name__)
do = Database_Operator("../3-data/articles.db")
content = do.execute_statement("SELECT * FROM articles;")
element = content[0][1]

@app.route('/', methods=['GET'])
def home():
    return element

if __name__ == "__main__":
    app.run(debug=True)

