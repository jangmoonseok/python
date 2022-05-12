import os
import sys
import urllib.request
from bs4 import BeautifulSoup as bs
from day11.dao_blog import DaoBlog

dao = DaoBlog()

client_id = "SpXNBDoPlP7PpQW6aXqU"
client_secret = "akmG94jcSk"
encText = urllib.parse.quote("대전 오류동 맛집")
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
    soup = bs(response_body.decode('utf-8'), "xml")
    items = soup.find_all("item")
    for i in items:
        title = i.find('title').text
        link = i.find('link').text
        description = i.find('description').text
        bloggername = i.find('bloggername').text
        bloggerlink = i.find('bloggerlink').text
        postdate = i.find('postdate').text
        
        values = [
            title, link, description, bloggername, bloggerlink, postdate
        ]
        
        
        cnt  = dao.myinsert(values)
        dao.conn.commit()
        
else:
    print("Error Code:" + rescode)