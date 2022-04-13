# 網路爬蟲，若遇到驗證問題，可先由這程式運行過一次並記錄cookie。
# 再將cookie導入自動化程式中，後續登入就不必驗證。

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

# 設定網頁介面
options = Options()
options.add_argument("--start-maximized")   # 視窗最大化
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)  # 拒絕彈跳視窗

path = "C:/ChromeDriver/ChromeDriver.exe"
browser = webdriver.Chrome(executable_path=path,chrome_options=options)
browser.maximize_window()


browser.get("https://shopee.tw/")
time.sleep(2)
    
pyautogui.moveTo(850,250)   #   "蝦皮"需要這個來跳脫初始廣告，可視情況刪除。
pyautogui.click()           

username = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "loginKey")))
password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))

username.clear()
password.clear()
username.send_keys("###")    # Your UserName
password.send_keys("###")    # Your Password
time.sleep(3)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button'))).click()    # 登入確認
time.sleep(60)  # 請在60秒內完成驗證，可自行更改秒數。

cookie = browser.get_cookies()
print("cookie已讀取成功")

with open('cookies.txt','w') as cookies:
    json.dump(cookie,cookies)   # 以json格式保存cookie資料
print("cookie已保存!")
browser.close()
