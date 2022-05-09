from flask import Flask, request
import json


app = Flask(__name__)

@app.route('/', methods=["POST"])
def home():
    # a = request.args.get('a');
    value = request.form['a']
    return "Hello, Python! {}".format(value)


if __name__ == '__main__':
    app.run(debug=True)