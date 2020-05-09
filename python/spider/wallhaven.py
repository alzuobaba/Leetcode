import os
import requests
from bs4 import BeautifulSoup
def get_urlList(index):
    url ='https://alpha.wallhaven.cc/search?'
    params ={
    'q':"",
    'categories':'001',
    'purity':'110',
    'atleast':'1920x1080',
    'topRange':'1M',
    'sorting':'toplist',
    'order':'desc',
    'page':index
    }
    response = requests.get(url,params)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    litag = soup.select(".preview")
    url_list =[item.attrs['href'] for item in litag]

    # print(url_list.__len__())
    return url_list

def get_picurl(list):
    host ='https:'
    for i in range(len(list)):
        # print(i)
        response = requests.get(urlList[i])
        pic_html = response.text
        soup =BeautifulSoup(pic_html,'lxml')
        pic_tag = soup.select("#wallpaper")
        picurl =host+pic_tag[0].attrs["src"]
        pic_id =pic_tag[0].attrs['data-wallpaper-id']
        downloadpic(picurl,pic_id)

def  downloadpic(url,id):
    print("开始下载")
    dirpath = 'D:/wallpaper/'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    path =dirpath+id+'.jpg'
    if not os.path.exists(path):
        response =requests.get(url)
        if response.status_code ==200:
            with open(path,'wb') as c:
                c.write(response.content)
                print("下载成功")

if __name__ == '__main__':
    for i in range(1,5):
        print('第{}页'.format(i))
        urlList =get_urlList(i)
        downurl =get_picurl(urlList)
