# coding*utf-8
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import re
from tqdm import tqdm
import os
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


def enum_link(url,driver,target):
    search =  driver.find_elements_by_class_name(target)
    #urls = [_.get_attribute('href') for _ in search
    urls = [_.text for _ in search]
    if urls == []:
        print("リンクがカラ")
    for url in urls:
        try:
            Alert(driver).accept()
        except:
            pass
        print(url)
        #driver.get(url)
        
        #print(driver.find_element_by_css_selector('.fxs-blade-title-titleText.msportalfx-tooltip-overflow').text)
        #driver.save_screenshot(driver.title + ".png")
def enum_shot(urls):
    index = 0
    for url in urls:
        print(url)
        driver.get(url)
        driver.save_screenshot(str(index) + '.png')
        index += 1

def get_table(driver,target):
    tableElem = driver.find_elements_by_class_name(target)
    #trs = tableElem.find_elements(By.TAG_NAME, "tr")
    trs = [_.tr for _ in tableElem]
    for i in range(1,len(trs)):
        tds = trs[i].find_elements(By.TAG_NAME, "td")
        line = ""
        for j in range(0,len(tds)):
            if j < len(tds)-1:
                line += "%s\t" % (tds[j].text)
            else:
                line += "%s" % (tds[j].text)
        print(line +"\r\n")



url = ['https://tk-dev-v3:dev100kg@v3.okp-tdk-dev.tk/','https://tk-dev-v3:dev100kg@v3.okp-tdk-dev.tk/faq/','https://tk-dev-v3:dev100kg@v3.okp-tdk-dev.tk/faq/about/application/','https://tk-dev-v3:dev100kg@v3.okp-tdk-dev.tk/faq/about/prescription/']
target = "azc-grid-cellContent"
driver = webdriver.Chrome()
enum_shot(url)

#driver.get(url)
#driver.implicitly_wait(40)

#Azure
#login_id = driver.find_element_by_id('i0116')
#login_id.send_keys("yuya.chishima@isb.co.jp")
#sleep(1)
#signin_btn = driver.find_element_by_id('idSIButton9')
#signin_btn.click()
#sleep(2)
#login_pass = driver.find_element_by_id('i0118')
#login_pass.send_keys("hm7Ewdjw$fKe)7W")
#signin_btn = driver.find_element_by_id('idSIButton9')
#signin_btn.click()
#leep(1)
#signin_btn = driver.find_element_by_id('idBtn_Back')
#signin_btn.click()

#get_table(driver,target)
#enum_link(url,driver,target)
#if __name__ == '__main__':
#    main()