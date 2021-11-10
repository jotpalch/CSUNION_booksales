# CSUNION_booksales
因應系學會辦公室整修 把裡面的書整理後拍賣 因為數量不小寫了個程式來處理

## 實作步驟
### 掃條碼
利用 pyhton 套件 `pyzbar` 加上手機的 ip camera  
實現相機掃條碼存入每本書的 ISBN 碼  
### 找書名
利用 pyhton 套件 `selenium` 動態爬蟲  
用 ISBN 碼找書名  
圖書資訊來源 : http://nbinet3.ncl.edu.tw/screens/opacmenu_cht.html
### 找書的封面照
利用 pyhton 套件 `selenium`   
google圖片搜尋 ISBN 碼 並截圖  
### 製作書單
利用 pyhton 套件 `pyimgur` 上傳圖片  
將對應的 ISBN 碼與圖片網址用 markdown 印出  
上傳至 HackMD  
