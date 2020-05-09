import codecs
import json
import re

import os
from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def search():
    try:

        browser.get('https://www.taobao.com')
        # imput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        # submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_SearchForm > button')))

        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total'))
                   )
        get_products()
        return  total.text
    except TimeoutException:
        search()

def nextPage(pageIndex):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))

        input.clear()
        input.send_keys(pageIndex)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(pageIndex))
                   )
        get_products()
    except TimeoutException:
        nextPage(pageIndex)


def savetotext(product):
    file = 'shops.txt'

    fp = codecs.open('output.txt', 'a+', 'utf-8')
    fp.write(json.dumps(file, ensure_ascii=False))


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html =browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product ={
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        jsonobj = json.dumps(product ,ensure_ascii=False)
        #print(product)
        savetotext(jsonobj)
        print('good')

if __name__ =='__main__':
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    print(total )
    for i in range(2,total + 1):
        print(i)
        nextPage(i)