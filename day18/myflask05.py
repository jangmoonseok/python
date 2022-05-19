from flask import Flask,render_template,request,redirect,jsonify
# app = Flask(__name__)
app = Flask(__name__,  static_url_path="")


@app.route('/')
def emp():
    return render_template('babylonOmok.html')


if __name__ == '__main__':
    app.run(debug=True)