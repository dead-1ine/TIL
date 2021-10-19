from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/user/<user_name>/<user_id>')
def user(user_name, user_id):
    print("당신의 이름은" + user_name)


    result = {
        "message": "당신의 이름은" + user_name
    }

    return result


if __name__ == '__main__':
    app.run(debug=True)