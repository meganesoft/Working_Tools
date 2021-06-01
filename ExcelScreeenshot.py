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


def enum_link(url,driver):
    search =  driver.find_elements_by_class_name('fx-grid-formatters-svgtext')
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
        




url = 'https://portal.azure.com/#blade/Microsoft_Azure_Storage/ContainerMenuBlade/overview/storageAccountId/%2Fsubscriptions%2F44794bc3-c147-4412-9ffd-696e841bf459%2FresourceGroups%2Ftk-dev-v3%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Ftkdevv3gbkstor/path/backuptool/etag/%220x8D8C2BC75D19FBD%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride//defaultId//publicAccessVal/None'
driver = webdriver.Chrome()

driver.get(url)
driver.implicitly_wait(40)

login_id = driver.find_element_by_id('i0116')
login_id.send_keys("yuya.chishima@isb.co.jp")
sleep(1)
signin_btn = driver.find_element_by_id('idSIButton9')
signin_btn.click()
sleep(2)
login_pass = driver.find_element_by_id('i0118')
login_pass.send_keys("hm7Ewdjw$fKe)7W")
signin_btn = driver.find_element_by_id('idSIButton9')
signin_btn.click()
sleep(1)
signin_btn = driver.find_element_by_id('idBtn_Back')
signin_btn.click()

enum_link(url,driver)
#if __name__ == '__main__':
#    main()