import json
from flask import Flask, render_template, request, make_response
import requests
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/oauth')
def oauth():
    # 사용자로부터 authorization code를 인자로 받음
    code = str(request.args.get('code'))
    print("code", str(code))

    # 전달받은 authorization code를 통해서
    # access_token, refresh_token을 발급
    auth_info = requests.post(
        url = "https://kauth.kakao.com/oauth/token",
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
        },
        data={
                    "grant_type": "authorization_code",
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "redirect_uri": REDIRECT_URI,
                    "code": code,
        }, 
    ).json()
    print("auth_info", auth_info)
    
    # access_token을 이용해서, Kakao에서 사용자 식별 정보 획득
    user = requests.post(
        url = "https://kapi.kakao.com/v2/user/me", 
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
            "Authorization": "Bearer " + auth_info['access_token']
        },
        #"property_keys":'["kakao_account.profile_image_url"]'
        data={}
    ).json()
    print("user", user)
    nickname=user["properties"]["nickname"]
    thumbnail_image=user["properties"]["thumbnail_image"]
    
    # 사용자 식별 id를 바탕으로 resp를 리턴
    resp = make_response(render_template('success.html', nickname=nickname, thumbnail_image=thumbnail_image))
    resp.set_cookie("logined", "true")
    resp.set_cookie("id", str(user["id"]))
    return resp

@app.route('/logout')
def logout():
    resp = make_response(render_template('index.html'))
    resp.delete_cookie('logined')
    resp.delete_cookie('id')
    return resp
    
if __name__ == '__main__':
    app.run(debug = True)