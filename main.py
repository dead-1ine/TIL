from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index/')
def test():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=8081)