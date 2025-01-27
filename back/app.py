import sys
import os
sys.path.append(os.path.abspath('/Users/apple/Documents/0-Programming/jpword/data'))

# [ ] to-do: build simple flask application

from flask import Flask
from db_operator import Database_Operator
# It seems that the folder cannot be imported as module description but the module, which is the file, only. 

app = Flask(__name__)
# The variable "__name__" provides the method of how the scirpt is being runned. Normally, there are two categories, which are run directly or by other module. If it is run directly, the value should be "__main__". If it is run by other module, the value should be "my_module". 

do = Database_Operator("../data/jpword.csv", "../data/jpword.db")
content = do.execute_statement("SELECT * FROM jpword;")
element = content[0][1]

@app.route('/', methods=['GET'])
def home():
    return element

# done: return the value of 
# @ named route decorator and its function is to locate the function with the user accessment. 

# Method here defines the verb type which including GET, POST, PUT and PATCH. GET means getting data from server. POST means submitting data to the server. PUT means updating the resoource. PATCH means partically modifying the resource. DELETE is to delete one resource. 

# The content can be transferred from database to API. Currently the data is displayed directly, if it should be applied on the HTML with dynamic functionality, 

if __name__ == "__main__":
    app.run(debug=True)

