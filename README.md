
# [噗浪機器人 - ES工程師](https://www.plurk.com/es_engineer)
![image](https://github.com/playhomelazy/plurk_es_engineer_public/blob/main/image/image-es_engineer-prod.jpg)
## 機器人製作者
HackMD－[@playhomelazy](https://hackmd.io/@playhomelazy)   
噗浪－[直到盡頭@playhomelazy](https://www.plurk.com/playhomelazy)  
簡介：為「偶像夢幻祭」查詢、抽卡、悄悄話等小工具，自動回覆噗浪機器人  
主要服務使用者：「偶像夢幻祭」製作人  
## 環境設置
* 程式語言：Python(3.0以上)
* Python pip：oauth2、requests
* API：Plurk API
* 資料交換格式：json
* 運行環境：Windows、Linux
## 機器人功能介紹
* 詳情請見此[連結](https://www.plurk.com/p/3fgt3at9g0)
## 啟動程式
#### 主程式
```
\bin\setup.py
```
#### 副程式(抽卡、攜手空間等功能)
```
\bin\search_data.py
```
## (必要)更新參數檔
```
\keys\API.keys
```
1. 先至[PlurkApp](https://www.plurk.com/PlurkApp/)申請API金鑰
2. 修改API.keys內容：
```
{"CONSUMER_SECRET": "App secret", "CONSUMER_KEY": "App key","ACCESS_TOKEN": "Token", "ACCESS_TOKEN_SECRET": "Secret"}
```
* CONSUMER_SECRET：對照下圖App Key的Secret
* CONSUMER_KEY：對照下圖App Key的Key
* ACCESS_TOKEN：對照下圖Token的Token
* ACCESS_TOKEN_SECRET：對照下圖Token的Secret 

![image](https://github.com/playhomelazy/plurk_es_engineer_public/blob/main/image/image-plurk_api.jpg)
## 資料檔說明
```
#偶像基本資料
\data\es_data.json
#偶像格言
\data\es_motto.json
#悄悄話
\data\es_secret.json
#YT歌曲資料
\data\es_songs.json
```
## member檔說明
```
#使用者卡片資料
#程式自動產檔，勿動
\member\*.json
```
## DEBUG紀錄
1. 如遇工程師未回覆之留言，請確認是否有觸發噗浪防洪機制
2. 程式放置過久未接收到訊息，會自動關閉回覆，可設置排程或systemd定期重啟(每15分鐘)