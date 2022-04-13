# 若要使用，"確認購買"註解須打開！

# WebDrivewait出錯機率大，不建議使用此程式碼，用try較佳。詳看autobuymachine2.py

import json
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


# 自動化網頁基本設定
def webSetting():

    options = Options()
    options.add_argument("--start-maximized")   # 視窗最大化
    prefs = {
        'profile.default_content_setting_values' :
            {
            'notifications' : 2
            }
}
    options.add_experimental_option('prefs',prefs)  # 禁止廣告/授權視窗彈出
    return options

# 清洗cookie、加入已儲存登入後cookie
def newCookie():
    browser.delete_all_cookies()
    time.sleep(3)

    with open('shopeeCookies.txt','r') as Newcookies:
        cookies = json.load(Newcookies)
    for cookie in cookies:
        browser.add_cookie(cookie)

# 蝦皮登入
def login(userName,passWord):
    
    if browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div/ul/a[3]'):
        browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div/ul/a[3]').click()
    
    username = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "loginKey")))
    password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    username.clear()
    password.clear()
    username.send_keys(userName)    # 輸入帳號
    password.send_keys(passWord)    # 輸入密碼
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button'))).click()    # 登入確認
    now = datetime.datetime.now()
    print('成功登入! 登入時間:', now.strftime('%Y-%m-%d %H:%M:%S.%f'))  # 紀錄登入時間

# 輸入折價券
def coupon(number):
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='_3rlAPA']"))).click()    # 選擇折價券

    coupon_number = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='全站折價券折扣碼']")))
    coupon_number.send_keys(number)     # 輸入折價碼     

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/button/span'))).click()   # 使用折扣碼
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal"]/div[2]/div/div[2]/div/div/div/div[3]/button[2]'))).click()   # 確定送出折價券

# 信用卡交易
def creditCardpay():
    select_credit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='信用卡/金融卡']")))
    select_credit.click()
    select_credit_2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='undefined']")))
    select_credit_2.click()

# 轉帳交易
def bankpay():
    select_bank = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='銀行轉帳']")))
    select_bank.click()

# 貨到付款
def cashpay():
    select_cash = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='貨到付款']")))
    select_cash.click()

# 購買流程
def buy(buyTimes):

    browser.get('https://shopee.tw/cart')   # 購物車網址
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now >= buyTimes:
            try:
                browser.refresh()   # 購物車網址重新更新(視情況可刪）

                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='_3eoyj7 clear-btn-style']"))).click()  # 全選按紐
    
                coupon(couponNumber)
    
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[2]'))).click()    # 去買單
    
                creditCardpay()
                #cashpay()
                #bankpay()
    
                buy_now = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='stardust-button stardust-button--primary stardust-button--large _1qSlAe']")))
                #buy_now.click()  # 確認下單
                now1 = datetime.datetime.now()
                print('結帳成功! 結帳時間:', now1.strftime('%Y-%m-%d %H:%M:%S.%f'))  # 紀錄結帳時間
                break
            except:
                pass

if __name__ == '__main__':
    
    userName = input('請輸入帳號:')
    passWord = input('請輸入密碼:')
    buyTimes = input('請輸入搶購時間,格式:2022-04-12 22:00:00.00000:')
    couponNumber = input('請輸入折價碼:')

    path = "C:/ChromeDriver/ChromeDriver.exe"
    options = webSetting()
    browser = webdriver.Chrome(executable_path=path,chrome_options=options)   
    browser.get("https://shopee.tw/")   # 蝦皮首頁
    
    # 等待頁面(可更改)
    time.sleep(0.1)
    
    pyautogui.moveTo(850,250)
    pyautogui.click()

    newCookie()
    login(userName,passWord)
    
    time.sleep(2)
    buy(buyTimes)

