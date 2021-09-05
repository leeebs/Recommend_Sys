from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.com/study')
study_list = []
tilte_list = []
title = []
dk = []

#스크롤 몇 번 할래
for i in range(10000):
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)

study_table = driver.find_element_by_css_selector('div.list')
study_list = study_table.find_elements_by_css_selector('a.item')
for study_item in study_list:
    completed = study_item.find_element_by_css_selector('span').text
    tags = study_item.find_element_by_css_selector('p.badges').text
    title = study_item.find_element_by_css_selector('h2').text
    info_table = study_item.find_element_by_css_selector('p.info')
    date = info_table.find_element_by_css_selector('span').text
    view = info_table.find_element_by_css_selector('span.viewcount').text
    data = {'completed': completed, 'tags' : tags, 'title' : title, 'date':date, 'view':view}
    dk.append(data)

df = pd.DataFrame(dk)
c = []
c = df['tags']
c[0].split(" ")[-1]

local =[]
tag = []
for i in c:
    local.append(i.split(" ")[-1])
    tag.append(i.split(' ')[0])
    
df.insert(1, 'tag', tag)
df.insert(2, 'local', local)
del df['tags']

df.to_csv('study.csv', encoding='utf-8-sig')
