import os
import sys
import urllib.request
from bs4 import BeautifulSoup as bs
client_id = "SpXNBDoPlP7PpQW6aXqU"
client_secret = "akmG94jcSk"
encText = urllib.parse.quote("오류동 맛집")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText# json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    # response_body = json.dumps(json.load(response), indent=4, ensure_ascii=False)
    # print(response_body)

    response_body = response.read()
    soup = bs(response_body.decode('utf-8'), "html.parser")
    titles = soup.find_all("title")
    # for i in titles:
    #     print(i.text)
    # print(titles[1].text)
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)