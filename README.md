# crawler

### 1 抓包软件

- tcp 协议： 网络游戏 
    - 外挂： 
    1，解包工具
    2，抓包工具
    - 软件： wireshark
    
- http 通信

     - 前后端交互过程
     
     - 学习的作用 ：去对应公司面试
     
     - 模拟网络情况 
     
        1. 下载上限下限速度 
        2. 模拟用户真实看到的情况  
        3. 对于它优化，开发都有好处
     
     - http client server 一应一答 没有加密
     
     - https 证书（有权威机构） 非对称加密 抓包： 信任一个证书

### 2 爬虫

- 搜索引擎 
    - query -> page rank(类似 权重)
    - 数据统计
    
- 爬虫的分类：
    - 裸请求 百度 google
    - 反爬虫策略
    - js 频繁上新的页面 纯js

- 组成部分 程序的分离
    - Downloader 下载页面          requests
    - HTMLParser 解析页面          pyquery     lxml 类似操作 dom
    - DataModel 字段 - element     业务逻辑

- 注意
    - 先下载页面，如果没有更新过应该不在下载第二次 假如那个网站突然封掉了呢
    - 这个拆分可以方便逻辑的扩展
    - 那些内容不可以爬 （做一个文明的程序员）/robots.txt
   
    
    
    


