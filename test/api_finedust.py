from bs4 import BeautifulSoup
import requests
import pandas as pd
#request  - scripts 폴더까지 이동 후 pip install requests, pip install beautifulsoup4

#

key = "7a4f4452736b6d7333384e747a466f"
url = "http://openapi.seoul.go.kr:8088/7a4f4452736b6d7333384e747a466f/xml/RealtimeCityAir/1/5/%EB%8F%99%EB%B6%81%EA%B6%8C/%EC%84%B1%EB%B6%81%EA%B5%AC" #성북구의 정보를 받아온다 

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

print(soup.pm10.get_text()+"㎍/㎥")