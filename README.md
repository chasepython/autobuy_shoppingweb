# autobuy_shoppingweb

透過selenium進行線上商城自動化購買，提供三種應對版本參考，可自行饌改。


使用步驟：     
1.先開啟getlogincookie，紀錄帳號登入後的cookie。     
2.提供兩種自動化版本：        
　a.WebDriverWait為主的運行方式      
　b.try為主的運行方式      
              ##***建議以try方式進行自動化運行。try比wait速度更快且穩定！***##
  
  其中，自動化步驟主要分為兩種模式：
            
            a.---購物車模式---
              事先將預購商品放置購物車
 
            b.---直接購買模式---
              考量商品有時間搶購限制，無法先行放置購物車。
       
       兩種自動化主要步驟：
       登入購物主頁 => 登入帳號 => "購物車模式" or "直接購買模式"
       => 購物車全選商品並送出折價券 => 選擇付費方式(付現、信用卡、轉帳) => 確認結帳
       

未來將持續優化程式運行，簡化並整合函數。
若有任何問題與建議地方歡迎提點，謝謝！
