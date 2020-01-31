import os
import requests
from utils import log


def headers():
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Cookie': 'cookie' # cookie
    }
    return h


def cached_url(url):
    """
    缓存, 避免重复下载网页浪费时间
    """
    folder = 'zhihu_cached'
    filename = '{}.html'.format('zhihu')
    path = os.path.join(folder, filename)

    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
        return s
    else:
        # 建立 cached 文件夹
        if not os.path.exists(folder):
            os.makedirs(folder)
        # 发送网络请求, 把结果写入到文件夹中
        r = requests.get(url, headers=headers())
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content


def get(url):
    return cached_url(url)


def timeline_from_url(url):
    page = get(url)
    log(page)


def main():
    url = 'https://www.zhihu.com/'
    timeline_from_url(url)


if __name__ == '__main__':
    main()
