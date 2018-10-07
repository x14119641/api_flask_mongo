from flask import Flask,jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/other')
def hello_other():
    return 'Hello Other!'
@app.route('/bye')
def bye():
    random_number = random.randint(1,100)
    json_output = {"result":{"bye":f"Random_bye number is {random_number}"}}
    return jsonify(json_output)

if __name__ =='__main__':
    app.run()
