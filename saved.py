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

ua_file = '/Users/mac/Documents/demo/paper/1.txt'
f=open(ua_file,'r')

ua_list = [line.strip() for line in f.readlines()]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-lang=en-US')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('log-level=3')
chrome_options.add_argument('user-agent=' + random.choice(ua_list))


#single
i = 1
prefix = ''
file_path = "/Users/mac/Documents/demo/paper/carton/"

driver=webdriver.Chrome(executable_path='/Users/mac/Documents/demo/paper/chromedriver')
driver.get('https://movie.douban.com/tag/#/?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1,%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86,%E5%8A%A8%E7%94%BB')
# 点击加载更多 
for i in range(16):
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/a').click()
    time.sleep(2)

# 抓取页面所有URL
url_list = []
for i in range(1, 301):
    url = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/a[%d]' % i).get_attribute('href')
    url_list.append(url)

#存html
for i in range(0,len(url_list)):
    driver.get(url_list[i])
    html = driver.page_source
    page_source = etree.HTML(html)
    html_file = file_path + prefix + '%d.html' % i
    h_file = open(html_file, 'w', encoding='utf-8')
    h_file.write(html)
    print('write success %s' % html_file)
    h_file.close()





