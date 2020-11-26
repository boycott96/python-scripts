from selenium import webdriver
import time
import os.path
from selenium.webdriver.chrome.options import Options


def webshot(url, saveImgName):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    chromedriver = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Scripts\chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=chromedriver)
    driver.maximize_window()
    # 返回网页的高度的js代码
    # js_height = "return document.body.clientHeight"
    picname = saveImgName
    link = url
    # driver.get(link)
    try:
        driver.get(link)
        # k = 1
        # height = driver.execute_script(js_height)
        # while True:
        #     if k * 500 < height:
        #         js_move = "window.scrollTo(0,{})".format(k * 500)
        #         print(js_move)
        #         driver.execute_script(js_move)
        #         time.sleep(0.2)
        #         height = driver.execute_script(js_height)
        #         k += 1
        #     else:
        #         break
        # scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        # scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(1920, 1080)
        driver.get_screenshot_as_file(picname + ".png")

        print("Process {} get one pic !!!".format(os.getpid()))
        time.sleep(0.1)
    except Exception as e:
        print(picname, e)


if __name__ == '__main__':
    t = time.time()  # 两个参数，前面url，后面保存地址
    webshot('https://www.google.com/', 'D:/webReptile/google')
    print("操作结束，耗时：{:.2f}秒".format(float(time.time() - t)))