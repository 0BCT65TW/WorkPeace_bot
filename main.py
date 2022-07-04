from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import requests
import time
from number import *
from bs4 import BeautifulSoup
# url ='http://124.219.116.138:8080/ftzbt/daily.aspx?a=2&g=1&t=18'
# re = requests.get(url)
# soup = BeautifulSoup(re.text,"html.parser")
# # print(re.status_code) #用來偵測網站是否有回應,通常會顯示200 表示連線正常
# driver = webdriver.Chrome()
# driver.get(url)
#
# selectA = driver.find_element(By.NAME,'t2id') #工號定位
# find_me = Select(selectA)
# find_me.select_by_value("IGB3-08490")
# time.sleep(5)
#
# selectB = driver.find_element(By.NAME,'loc') #廠區定位
# find_loc = Select(selectB)
# find_loc.select_by_value("HC")
# time.sleep(5)
#
# sendB = driver.find_element(By.XPATH,'/html/body/form/div[3]/div[11]/input')
# sendB.click() #測試送出
def Send_lunch_re():
    print('請輸入工號')
    number = input()
    url = "http://124.219.116.138:8080/ftzbt/daily.aspx?a=2&g=1&t=18"
    driver = webdriver.Chrome()
    driver.get(url)

    s_number = driver.find_element(By.NAME,'t2id')
    temp = Select(s_number)
    temp.select_by_value(number)
    time.sleep(3)
    print('已選擇工號' +number)
    driver.find_element(By.XPATH,'/html/body/form/div[3]/div[3]/div[2]/div[1]/span/input').click()
    s_loc = driver.find_element(By.NAME,'loc')
    local = Select(s_loc)
    local.select_by_value('HC')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/form/div[3]/div[11]/input').click()
    print('以結束訂餐')
    time.sleep(10)
def wei7018():
    url = "http://124.219.116.138:8080/ftzbt/daily.aspx?a=2&g=1&t=18"
    driver = webdriver.Chrome()
    driver.get(url)
    s_number = driver.find_element(By.NAME, 't2id')
    temp = Select(s_number)
    temp.select_by_value('IGB3-08490') # 已選擇工號
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/div[2]/div[1]/span/input').click()
    s_loc = driver.find_element(By.NAME, 'loc')
    local = Select(s_loc)
    local.select_by_value('HC') #已選擇廠區
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div[11]/input').click()
    time.sleep(10)

def all_lunch():
    url = "http://124.219.116.138:8080/ftzbt/daily.aspx?a=2&g=1&t=18"
    driver = webdriver.Chrome()
    driver.get(url)
    tempp=[temp_a, temp_b, temp_c, temp_d]
    for index in range(len(tempp)):
        s_number = driver.find_element(By.NAME, 't2id')
        temp = Select(s_number)
        temp.select_by_value(tempp[index])  # 已選擇工號
        time.sleep(3)
        name = driver.find_element(By.XPATH,'/html/body/form/div[3]/div[1]/div[4]/input')
        print(name.get_attribute('value'))
        # driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/div[2]/div[1]/span/input').click()
        # s_loc = driver.find_element(By.NAME, 'loc')
        # local = Select(s_loc)
        # local.select_by_value('HC')  # 已選擇廠區
        # time.sleep(3)
        # # driver.find_element(By.XPATH, '/html/body/form/div[3]/div[11]/input').click()
        # time.sleep(10)
all_lunch()



