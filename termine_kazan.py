import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from openpyxl import Workbook, load_workbook
import datetime
import time



# расположение chromedriver.exe
path_chromedriver = r'chromedriver.exe'

def etap(driver):
        driver.get('http://217.25.93.13:5555/tasks')
        time.sleep(10)
        #залогинилсь
        driver.find_element_by_xpath('//*[@id="afabd19a-ed93-404f-92b4-8ea1b7e2e9c2"]/td[2]/a').click()
        driver.find_element_by_xpath('//*[@id="task-page"]/div/div/div[1]/h2/button').click()
        print('Клик по завершено произведен')

# 1ый этап: создание задачи для выгрузки оплат
def create_task():
   

    driver = webdriver.Chrome(path_chromedriver)
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(60)
    
    for i in range(200):
        print('Запуск итерация -', i)
        etap(driver)

create_task()
