import os
import re

import requests
import json
def get_name_url():
    params = {
        'format':'js',
        'idx':'0',
        'n':'1',
        'nc':'1514102397971',
        'pid':'hp',
        'video':'1',
        'og':'1'
    }
    url ='https://cn.bing.com/HPImageArchive.aspx?'
    response = requests.get(url, params=params)
    if  response.status_code ==200:
        rejson = response.json()
        # print(rejson)
        og =rejson.get("og").get('img')
        name=rejson.get("images")[0].get("copyright")
        namesearch = re.search(r'(.*)\(',name)
        picname = namesearch.group(1)
       # print(name)
        print(og)
        return {'url' : og , 'name':picname}

def download_pic(urldict):
    url =urldict.get("url")
    name =urldict.get("name")
    dir = 'D:/bing/'
    if not os.path.exists(dir):
        os.mkdir(dir)
    response = requests.get(url)
    if response.status_code==200:


        path =dir+name+'.jpg'
        with open(path,'wb')as code:
            code.write(response.content)
            print("下载成功")



if __name__ == '__main__':
    urldict  =get_name_url()
    download_pic(urldict)