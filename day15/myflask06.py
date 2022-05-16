from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send
from random import random

app = Flask(__name__)
app.secret_key = "mysecret"


def myinit():
    com = ""
    arr9 = list(range(1,9 + 1))
    for i in range(100):
        rnd = int(random() * 9)
        temp = arr9[0]
        arr9[0] = arr9[rnd]
        arr9[rnd] = temp
    
    for i in arr9[0:3]:
        com += str(i)
        
    return  com

ans=myinit()
socket_io = SocketIO(app)

@app.route('/')
def strike():
    return render_template('strike.html')




@socket_io.on("message")
def request(message):
    print("message : "+ message)    
    arr = message.split(',')
    
    if(arr[0] == "check"):
        myinput = arr[1]
        result = check(myinput)
        to_client = dict()
        to_client['message'] = message + "," + result
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
        send(to_client, broadcast=False)
    else:         
        to_client = dict()
        to_client['message'] = message
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
        send(to_client, broadcast=True)


def check(myinput):
    strike = 0;
    ball = 0;
    for i in range(len(ans)):
        for j in range(len(myinput)):
            if ans[i] == myinput[j] and i == j:
                strike += 1
            elif ans[i] == myinput[j] and i != j:
                ball += 1
            else:
                pass
    result = "{}S {}B".format(str(strike), str(ball))
    return result
    if strike == 3:
        pass
if __name__ == '__main__':
    socket_io.run(app, debug=True, host="0.0.0.0", port="9999")
    