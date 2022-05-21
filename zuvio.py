import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass

print("請輸入帳號： ")
a = input()
print("請輸入密碼:")
b = input()
url = 'https://portal.stust.edu.tw/csls/Login.aspx?ReturnUrl=%2fcsls%2fPages%2fleader%2fLEP_leader.aspx'
# re = requests.get(url)
driver = webdriver.Chrome()
driver.get(url)
def Login():
    driver.find_element(By.XPATH ,"/html/body/form/div[3]/div[2]/table/tbody/tr[1]/td[2]/input").send_keys(a)
    driver.find_element(By.XPATH ,"/html/body/form/div[3]/div[2]/table/tbody/tr[2]/td[2]/input").send_keys(b)
    driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/table/tbody/tr[3]/td[2]/input").click()
    print("登入完成")

Login()
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/button").click()
driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/div/table/tbody/tr[1]/td[1]/button").click()

def index():
    for i in range(2,12):
        temp = driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/div/table/tbody/tr[5]/td/div/table/tbody/tr["+ str(i) +"]/td[2]/span").text
        print(temp+"@stust.edu.tw")
index()

def index_end():
    for i in range(2,7):
        temp_end = driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/div/table/tbody/tr[5]/td/div/table/tbody/tr["+ str(i) +"]/td[2]/span").text
        print(temp_end+"@stust.edu.tw")
def index_path():
    for i in range(2,3):
        driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/div/table/tbody/tr[5]/td/div/table/tbody/tr[12]/td/table/tbody/tr/td["+ str(i) +"]/a").click()
        index()

driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/div/table/tbody/tr[5]/td/div/table/tbody/tr[12]/td/table/tbody/tr/td[3]/a").click()
index_end()
print("雙號已完畢")
driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/div/table/tbody/tr[4]/td/div/span[2]/span[2]/label").click()
index()
index_path()
driver.find_element(By.XPATH,"/html/body/form/div[3]/div[2]/div/table/tbody/tr[5]/td/div/table/tbody/tr[12]/td/table/tbody/tr/td[3]/a").click()
index_end()