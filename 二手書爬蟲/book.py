from selenium import webdriver
import json

f =open("book.txt")
d = dict()

for book in f.readlines():

    print(book)

    driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    driver.get("http://nbinet3.ncl.edu.tw/search*cht/?searchtype=i&searcharg="+book) # 更改網址以前往不同網頁

    try :
        next = driver.find_element_by_xpath("/html/body/table[@class='browseScreen']/tbody/tr[2]/td/table[@class='browseList']/tbody/tr[@class='browseEntry'][1]/td[@class='browseEntryData']/a[2]")
        next.click()
        next = driver.find_element_by_xpath("/html/body/table[@class='browseScreen']/tbody/tr[2]/td/table/tbody/tr[@class='briefCitRow'][1]/td/table/tbody/tr/td[2]/span[@class='briefcitTitle']/a")
        next.click()
        title = driver.find_element_by_xpath("/html/body/div[@class='bibScreen']/div[@class='bibMain']/div[@class='bibInfo']/div[@class='bibContent'][1]/table/tbody/tr/td[1]/table[@class='bibDetail']/tbody/tr[@class='bibInfoEntry']/td/table/tbody/tr[2]/td[@class='bibInfoData']/strong")
        d[book] = title.text
    except :
        try :
            title = driver.find_element_by_xpath("/html/body/div[@class='bibScreen']/div[@class='bibMain']/div[@class='bibInfo']/div[@class='bibContent'][1]/table/tbody/tr/td[1]/table[@class='bibDetail']/tbody/tr[@class='bibInfoEntry']/td/table/tbody/tr[2]/td[@class='bibInfoData']/strong")
            d[book] = title.text
        except :
            driver.close()
            continue

    driver.close()

print(d)
j = json.dumps(d)
print(j)

f.close()
