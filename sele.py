from selenium import webdriver
from time import sleep
import os

f = open("book.txt")
count = 0
for book in f.readlines():
    
    driver = webdriver.Safari()

    driver.get("https://www.google.com.tw/imghp?hl=zh-TW")  # 更改網址以前往不同網頁
    driver.maximize_window()
    # 定位搜尋框
    element = driver.find_element_by_class_name("gLFyf.gsfi")
    # 傳入字串
    element.send_keys(book)

    button = driver.find_element_by_class_name("zgAlFc")
    button.click()

    sleep(1)

    print(driver.current_url)
    driver.find_element_by_class_name("rg_i.Q4LuWd").click()
    sleep(0.2)
    driver.get_screenshot_as_file(
        os.path.abspath(os.getcwd())+"//ssimg//"+book+".png")

    driver.close()  # 關閉瀏覽器視窗

f.close()
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from time import sleep
#
# service = Service('/usr/local/bin/msedgedriver')
# service.start()
# dr = webdriver.Remote(service.service_url)
#
# dr.get('https://www.google.com.tw/imghp?hl=zh-TW')
#
# dr.find_element('id', 'kw').send_keys('博客园 韩志超')
# dr.find_element('id', 'su').click()
# sleep(3)

# dr.quit()


# http://nbinet3.ncl.edu.tw/screens/opacmenu_cht.html
