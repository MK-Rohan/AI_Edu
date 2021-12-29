#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import math
from math import ceil, floor
import math as m
from math import ceil as c
print(math.cos(10))
print(math.ceil(5.6))
print(math.floor(5.6))

from math import cos, ceil, floor

print(cos(10))
print(ceil(5.6))
print(floor(5.6)) 

import math as m
m.cos(10)


# In[ ]:


import random as rnd

print("random 모듈 : ")
print("random() : ", rnd.random())

print("uniform() : ", rnd.uniform(10,20))
print("randrange() : ", rnd.randrange(10,20))
print("choice() : ", rnd.choice(list(range(10))))
a = list(range(10))
print("shuffle() : ", rnd.shuffle(a), a)
print("sample() : ", rnd.sample(a,k=3))


# In[ ]:


# sys  모듈: 시스템 관련 정보를 가져 옴
import sys

print("copyright : ", sys.copyright)
print("version : ", sys.version)

# os 모듈: 운영체제와 관련되 명령어
import os

print("현재 운영체제 : ", os.name)
print("현재 작업 경로 : ", os.getcwd())
print("현재 폴더 리스트 : ", os.listdir())

os.mkdir('test_dir')
os.listdir()

os.rmdir('test_dir')
os.listdir()

os.rename('Untitled.ipynb', 'new.py')
os.listdir()

get_ipython().system('dir')


# In[ ]:


import datetime as dt

print(dt.datetime.now())
print(dt.datetime.today())

import time

print("time start ")
time.sleep(3)
print("\ntime end ")


# In[ ]:


from urllib import request

target = request.urlopen('http://www.google.com')
output = target.read()
print(output)


# In[ ]:


# <html> ~ </html> tag 형식으로 변환해 주는 모듈: BeautifulSoup
from bs4 import BeautifulSoup

target = request.urlopen('http://www.google.com')
soup = BeautifulSoup(target)
soup


# In[ ]:


soup.title
<title>The Dormouse's story</title>

soup.title.name
u'title'

soup.title.string
u'The Dormouse's story'

soup.title.parent.name
u'head'

soup.p
<p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
u'title'

soup.a
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')  # tag 명 


# In[ ]:


# 기상청 날씨 예보를 가져와서 보여 줌
# url에 연결 -> urllib.request.urlopen(url명)
# url에서 자료를 가져옴 -> <html> ~ </html> 태그 형식으로 
# BeautifulSoup(url open 정보)

from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId=108'
target = request.urlopen(url)
soup = BeautifulSoup(target)

for location in soup.select('td.midterm-province'):
    print(location.text)
    
for location in soup.find_all('tr'): 
    if location.find('td', class_='midterm-city'):
        print("도시명 : {}, 최저기온 :{}, 최대기온 :{}".format(location.find('td', class_='midterm-city').text, location.find('span', class_='tmn').text, location.find('span', class_='tmx').text)) 


# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!!"</h1>


# In[ ]:


def test(function):
    def wrapper():
        print("Hello start!!! ")
        print(function.__name__)
        function()
        print(function.__name__)        
        print("Hello  end !!!")
    print("000 :", function.__name__)         
    return wrapper

# 데코레이션 함수
@test
def hello():
    print("Hello")

hello()


# In[ ]:


import test_package.module_a as a
import test_package.module_b as b

print("module_a : ",a.variable_a)
print("module_b : ",b.variable_b)

from test_package import *

print("module_a : ",module_a.variable_a)
print("module_b : ",module_b.variable_b)

