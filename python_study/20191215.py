from urllib.parse import urljoin

import pickle
import re
import requests
import zlib

import pymongo



def main():
    # 正则表达式匹配所有的question连接  (?<=<a\s+.*(?<=href="))(?=/question)[^"]*
    pattern = re.compile('(?!=<a\s+.*(?<=href="))(?=/question)[^"]*')

    # 指定种子页面
    base_url = 'https://www.zhihu.com'
    seed_url = urljoin(base_url, 'explore')

    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['python']
    mycol = mydb['test']

    # 设置用户代理(否则访问会被拒绝)
    headers = {'user-agent': 'Baiduspider'}
    # 通过requests模块发送GET请求并指定用户代理
    resp = requests.get(seed_url, headers=headers)
    # 创建BeautifulSoup对象并指定使用lxml作为解析器
    web_sources = resp.text
    web_sources_lit = re.findall(pattern, web_sources,)

    for t in web_sources_lit:

        # 如果Redis的键'zhihu'对应的hash数据类型中没有URL的摘要就访问页面并缓存
        html_page = requests.get(base_url + t, headers=headers).text
        # 对页面进行序列化和压缩操作
        # zipped_page = zlib.compress(pickle.dumps(html_page))
        # 使用hash数据类型保存URL摘要及其对应的页面代码
        mydict = {"key": t, "value": html_page}
        mycol.insert_one(mydict)


if __name__ == '__main__':
    main()