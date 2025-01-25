import sys
import os
sys.path.append(os.path.abspath('/Users/apple/Documents/0-Programming/jpword/data'))

from flask import Flask
from db_operator import Database_Operator
# It seems that the folder cannot be imported as module description but the module, which is the file, only. 




# app = Flask(__name__)
# The variable "__name__" provides the method of how the scirpt is being runned. Normally, there are two categories, which are run directly or by other module. If it is run directly, the value should be "__main__". If it is run by other module, the value should be "my_module". 

'''
@app.route('/')
def home():
    return "This is the home page."
'''

# to-do: return the value of 

# @ named route decorator and its function is to locate the function with the user accessment. 


