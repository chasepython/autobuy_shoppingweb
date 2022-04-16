# 若要使用，"確認購買"註解須打開！

# 須將物品事先放置購物車
# 登入 → 購物車 → 折價券 → 選擇付費方式 → 確認購買

import json
import pyautogui
from selenium import webdriver
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

    with open('XXXXCookies.txt','r') as Newcookies:
        cookies = json.load(Newcookies)
    for cookie in cookies:
        browser.add_cookie(cookie)

# 帳號登入
def login(userName,passWord):
    
    while True:
        try:
            if  browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div/ul/a[3]'):
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
        except:
            pass
        
        break

# 輸入折價券
def coupon(Number):

    while True:
        # 選擇折價券
        try:
            if  browser.find_element_by_css_selector("span[class='_3rlAPA']"):      
                browser.find_element_by_css_selector("span[class='_3rlAPA']").click()
#                print('選擇折價券成功!')
                break
        except:
#            print('選擇折價券失敗')
            pass

    while True:
        # 輸入折價碼 
        try:
            if  browser.find_element_by_css_selector("input[placeholder='全站折價券折扣碼']"):      
                browser.find_element_by_css_selector("input[placeholder='全站折價券折扣碼']").send_keys(Number)
#                print('輸入折價碼成功!')
                break
        except:
#            print('輸入折價券失敗')
            pass

    while True:
        # 使用折扣碼
        try:
            if  browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/button/span'):      
                browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/button/span').click()
                #print('使用折扣碼成功!')
                break
        except:
#            print('使用折價券失敗')
            pass

    while True:
        # 確定送出折價券
        try:
            if  browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div[2]/div/div/div/div[3]/button[2]'):      
                browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div[2]/div/div/div/div[3]/button[2]').click()
#                print('送出折價券成功!')
                break
        except:
#            print('送出折價券失敗')
            pass


        
    
# 信用卡交易
def creditCardpay():

    while True:
        # 選擇信用卡/金融卡
        try:
            if  browser.find_element_by_css_selector("button[aria-label='信用卡/金融卡']"):      
                browser.find_element_by_css_selector("button[aria-label='信用卡/金融卡']").click()
                break
        except:
#            print('選擇信用卡/金融卡失敗')
            pass

    while True:
        # 細選信用卡/金融卡
        try:
            if  browser.find_element_by_css_selector("div[class='undefined']"):      
                browser.find_element_by_css_selector("div[class='undefined']").click()
                break
        except:
#            print('細選信用卡/金融卡失敗')
            pass

# 轉帳交易
def bankpay():

    while True:
        # 選擇銀行轉帳
        try:
            if  browser.find_element_by_css_selector("button[aria-label='銀行轉帳']"):      
                browser.find_element_by_css_selector("button[aria-label='銀行轉帳']").click()
                break
        except:
#            print('選擇轉帳失敗')
            pass

# 貨到付款
def cashpay():
    
    while True:
        # 選擇貨到付款
        try:
            if browser.find_element_by_css_selector("button[aria-label='貨到付款']"):
                browser.find_element_by_css_selector("button[aria-label='貨到付款']").click()
                break
        except:
#            print('選擇轉帳失敗')
            pass

# 購買流程
def buy(buyTimes):

    browser.get('https://')
  
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now >= buyTimes:
            
            browser.refresh()   # 搶購時間一到，重刷頁面(視情況可刪)。

            # 全選按紐
            while True:
                try:
                    if browser.find_element_by_css_selector("button[class='_3eoyj7 clear-btn-style']"):
                        browser.find_element_by_css_selector("button[class='_3eoyj7 clear-btn-style']").click()
#                        print('勾選全選按紐')
                        break
                except:
                    pass

            # 執行coupon
            coupon(couponNumber)
            
            # 去買單
            while True:
                try:
                    if browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[2]'):
                        browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[2]').click()
#                        print('點選"去購買"')
                        break
                except:
                    pass
            
            creditCardpay()
            #cashpay()
            #bankpay()

            # 確認結帳
            while True:
                try:
                    if browser.find_element_by_css_selector("button[class='stardust-button stardust-button--primary stardust-button--large _1qSlAe']"):
                        #browser.find_element_by_css_selector("button[class='stardust-button stardust-button--primary stardust-button--large _1qSlAe']").click()
                        now = datetime.datetime.now()
                        print('結帳成功! 結帳時間:', now.strftime('%Y-%m-%d %H:%M:%S.%f'))  # 紀錄結帳時間
                        break
                except:
                    pass

            break

if __name__ == '__main__':
    
    userName = input('請輸入帳號:')
    passWord = input('請輸入密碼:')
    buyTimes = input('請輸入搶購時間,格式:2022-04-12 22:00:00.00000:')
    couponNumber = input('請輸入折價碼:')

    path = "C:/ChromeDriver/ChromeDriver.exe"
    options = webSetting()
    browser = webdriver.Chrome(executable_path=path,chrome_options=options)   
    browser.get("https://")
    
    # 等待頁面(可更改)
    time.sleep(0.1)
    
    pyautogui.moveTo(850,250)
    pyautogui.click()

    newCookie()
    login(userName,passWord)

    time.sleep(2)
    buy(buyTimes)
    
