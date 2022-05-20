import requests
from flask import Flask, redirect, request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/naver") 
def NaverLogin():
    # developers에서 발급받은 client_id
    client_id = "zMkOhkDYiQM_zxV99Za1"
    # 로그인 기능을 위해 설정한 Redirect URI로 네이버 로그인 후 이동할 페이지 URL입니다.
    redirect_uri = "http://127.0.0.1:5000/callback"
    # url = f"https://nid.naver.com/oauth2.0/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    url = """https://nid.naver.com/oauth2.0/authorize?
        client_id=zMkOhkDYiQM_zxV99Za1&redirect_uri=http://127.0.0.1:5000/callback&response_type=code"""
    # 로그인이 정상이라면 127.0.0.1:5000/callback?code={코드}로 요청이 갈 것
    return redirect(url)

@app.route('/')
def emp():
    return render_template("login.html")


@app.route("/callback")
def callback():
    # 이때 query parameter인 code를 읽고, Client ID와 Client Secret와 함께 토큰을 요청한다.
    params = request.args.to_dict()
    code = params.get("code")

    client_id = "zMkOhkDYiQM_zxV99Za1"
    client_secret = "b2oF0ZKpRL"
    redirect_uri = "http://127.0.0.1:5000/callback"

    #naver/oauth/callback(REDIRECT_URI)에서는 request로 전달받은 authorization code를 통해서 access_token을 발급받는다.
    token_request = requests.get(f"""https://nid.naver.com/oauth2.0/token?
                grant_type=authorization_code&client_id=zMkOhkDYiQM_zxV99Za1&client_secret=b2oF0ZKpRL&code={code}""")
    token_json = token_request.json()
    print(token_json)
    
    # 결과 값에서 acccess_token(접근 토큰)을 사용하여 유저에 대한 정보를 받아온다. 토큰의 만료기간도 json값 안에 있다.
    access_token = token_json.get("access_token")
    profile_request = requests.get("https://openapi.naver.com/v1/nid/me", 
                                   headers={"Authorization" : f"Bearer {access_token}"},)
    # 이 접근 토큰을 이용해서 마지막으로 프로필 API를 호출하면 profile_data에 유저가 허락한 정보가 있음을 알 수 있다.
    profile_data = profile_request.json()

    print(profile_data)
    user_email = profile_data['response']['email']
    return render_template("success.html",email=user_email)
    
    
if __name__ == '__main__':
    app.run(debug=True)