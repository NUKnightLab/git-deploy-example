import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    example_var = os.environ.get('EXAMPLE_VAR', 'EXAMPLE_VAR not set') 
    return 'Hello, World! {{ example_var }}'
