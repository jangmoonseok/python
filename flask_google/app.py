from oauth2client.contrib.flask_util import UserOAuth2
from flask import Flask,render_template
import flask
from flask.globals import request
from flask.helpers import make_response

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abc123'

app.config['GOOGLE_OAUTH2_CLIENT_ID'] = '307160482243-ps081822s35qlbce6p2uea5e29jup7fk.apps.googleusercontent.com'
app.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = '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'

oauth2 = UserOAuth2(app)

@app.route("/")
def init():
    return render_template('login.html')

@app.route('/login')
@oauth2.required
def login():
    if oauth2.has_credentials(): 
        print('login OK')
        return render_template('success.html', email=oauth2.email)
    else: 
        print('login NO') 



app.run()