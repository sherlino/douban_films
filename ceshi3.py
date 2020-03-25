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

driver_path = "/Users/mac/Documents/demo/paper/chromedriver"
driver=webdriver.Chrome(executable_path=driver_path)
driver.get('https://movie.douban.com/subject/27605698/')

html = driver.page_source

pattern2 = re.compile(r'\u8bed\u8a00:</span>(.*?)<br>', re.S)
item2 = re.findall(pattern2, html)
print(item2)