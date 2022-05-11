from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://127.0.0.1:5000/list")  

bsObject = BeautifulSoup(html, "html.parser") 

selects1 = bsObject.select("td:nth-child(2)")
selects2 = bsObject.select("td:nth-child(4)")

for i in selects1:
    print("이름 : {}".format(i.text))
    

for i in selects2:
    print("주소 : {}".format(i.text))