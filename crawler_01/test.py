import os
import requests
from pyquery import PyQuery as pq
from utils import log


#输出会出现：抱歉！页面无法访问....这就是限制爬虫了

#解决方法：加入headers，在requests.get（headers=headers）里面，添加headers
#构建headers

headers={
"Host": "www.dianping.com",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
res=requests.get("http://www.dianping.com/",headers=headers)
print(res.text)

