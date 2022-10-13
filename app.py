from flask import Flask
import logging
app = Flask(_name_)
logging.basicConfig(filename='dev.log', level=logging.INFO)
@app.route('/')
def hello():
    return 'hello world Dev!'

if _name== "main_":
    app.run(host='0.0.0.0', port=80)
