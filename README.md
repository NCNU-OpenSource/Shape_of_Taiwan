# Shape of Taiwan

## About
It's a Chrome Extension, which can translate Chinese words into Taiwanese words.

By analyzing web content, the extension will translate Chinese words into Taiwanese words, and highlight which words were translated, and show what the original words and english words are.

It allows users to open menu to add a feedback by a right-click.

這是一個能夠翻譯並標示出大陸用語的 Chrome 瀏覽器擴充套件

透過分析網頁內容，將大陸用語直接換成台灣用語，並在頁面中標示出哪些是已經被置換過，且顯示原本使用的用語和英文用語是為何。

允許使用者透過點擊右鍵開啟選單來新增回饋。

## Installation
### If you only want to use this extension
It will release on Extension Store
You can find it on Extension Store

### If you want build your own extension

#### Step 1 : Clone this repo
`git clone https://github.com/NCNU-OpenSource/Shape_of_Taiwan.git`

#### Step 2 : 進入 Chrome 的擴充功能選單
1. 開啟 "開發人員模式"
2. 載入未封裝的擴充功能，選擇專案資料夾
3. 預設擴充功能為開啟狀態，若要關閉功能，點擊擴充功能的 icon 即可

### Step 3 : 建立後端(本機執行)
1. 安裝專案所需的軟體和套件
2. 執行 `backend` 資料夾中的 `shape_of_taiwan_backend.py`
3. 將 `content.js` 中 `ajax` 的 `url` 改成本機的 `url`

### Other Intro

#### 相關技術
1. Chrome Extensions Framework
2. JavaScript
3. JSON
4. Regular Expression
5. Python Flask
6. uwsgi
7. certbot
8. nginx proxy pass
9. XMLHttpRequest
10. Cross Origin Resource Sharing
11. Jieba

#### 用詞對照資料範例(以 Json 格式儲存)
```json=
{
  "內存": {
    "zh_TW": "記憶體",
    "en_US": "RAM"
  },
  "報文": {
    "zh_TW": "封包",
    "en_US": "Packet"
  },
  "光驅": {
    "zh_TW": "光碟機",
    "en_US": ""
  }
}
```
#### 套件執行流程
![](https://i.imgur.com/KLeqUcn.png)

## About Backend
The backend folder should not put in production
It's here only for development

## 專案討論共筆
[見此](https://hackmd.io/GXm0RCNWSRGyPMsWsT23TA)
