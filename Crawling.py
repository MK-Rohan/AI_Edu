# 기상청 날씨 예보를 가져와서 보여줌
# url에서 자료를 가져옴 -> urllib.request.urlopen("url명")
# url에서 자료를 가져옴 -> <html> ~ </html> 태그 형식으로
# BeautifulSoup(url open 정보)
from urllib import request
from bs4 import BeautifulSoup

url = "https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=108"
target = request.urlopen(url)
soup = BeautifulSoup(target)

for location in soup.find_all('tr'):
    if location.find('td', class_='midterm-city'):
        print("도시명: {}, 최저 기온: {}, 최대 기온: {}".format(location.find('td', class_="midterm-city").text, location.find("span", class_='tmn').text, location.find("span", class_='tmx').text))
