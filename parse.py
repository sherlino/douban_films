from selenium import webdriver
from lxml import etree
from pandas import DataFrame as df
import time
from urllib import request
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import requests
from requests.exceptions import RequestException
import random
import re
import os


#解析
def parse(html,page_source):
	title =html.xpath('//*[@id="content"]/h1/span[1]/text()')[0].strip()
	year = html.xpath('//*[@id="content"]/h1/span[2]/text()')[0].strip()
	try:
		pattern2 = re.compile(r'\u8bed\u8a00:</span>(.*?)<br>', re.S)
		language = re.findall(pattern2,page_source)
	except:
		language = ''
	try:
		time = html.xpath('//span[contains(text(),"片长:")]/following-sibling::span[1]/text()')[0].strip()
	except:
		time = ''
	try:
		rate = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0].strip()
	except:
		rate = ''
	try:
		people = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')[0].strip()
	except:
		people = ''
	return{'title':title,
	        'year':year,
	        'language':language,
	        'time':time,
	        'rate':rate,
	        'people':people}

df_list = []
# 循环打开每一个下载+并解析页面
file_path = "/Users/mac/Documents/demo/paper/carton/"
path = '/Users/mac/Documents/demo/paper/carton/'
files = os.listdir(file_path)

for file in files:
    f = open(path+"/"+file,'r',encoding="utf-8")
    page_source=f.read()
    html = etree.HTML(page_source)
    try:
        one_data = parse(html,page_source)
    except:
        continue
    for k, v in one_data.items():
        print(k,":",v)
    time.sleep(2)
    df_list.append(one_data)

    

from pandas import DataFrame as df
import pandas as pd
df = pd.DataFrame(df_list)  
data = df.to_csv('/Users/mac/Documents/demo/paper/carton_movies.csv',encoding='utf-8')




