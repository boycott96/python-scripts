import re
import time
import requests
from bs4 import BeautifulSoup
import os

root = 'D:/壁纸/'


def get_html_url(url):  # 获取网址
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("服务器链接失败。。。。。。。。。。。。")
        print("等待五秒。。。。。。。。。。。。。。。。")
        time.sleep(5)
        return get_html_url(url)


def get_pic(html):  # 获取图片地址并下载
    try:
        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find('table').find('img')
        print(img)
        if img is not None:
            img_url = img['src']
            img_name = re.sub('[\\\|/:"*<>?\t]', '_', img['title'])
            path = root + img_name + '.jpg'
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(img_url)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print(img_name + "保存成功")
            else:
                print(img_name + "文件已存在")
    except:
        print("网页获取图片失败--等待两秒......")
        time.sleep(2)


def run():
    i = 14446
    while i <= 23046:
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$开始' + str(i) + '页')
        url = 'http://www.netbian.com/desk/' + str(i) + '-1920x1080.htm'
        html = (get_html_url(url))
        i += 1
        if html is None or html.find('无适合您分辨率的壁纸') > 0:
            continue
        else:
            get_pic(html)


if __name__ == '__main__':
    run()
