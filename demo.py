import requests
from common.check import *
from common.open_target_url import *

def poc1(url):
    payload = ""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13904.16.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.25 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    try:
        res =  requests.post(target_url,headers=headers,timeout=3)
        if res.status_code == 200 and "pgo==0" in res.text:
            print(target_url)
            bingo.append(target_url)
    except requests.RequestException as e: #e为异常信息
        print ("请求异常：%s" %(target_url)) 

if __name__ == '__main__':
    target_path = "D://git/poccc/targets/1.txt"
    bingo = []

    url_list = open_url_file(target_path)

    for url in url_list:
        poc1(url_agreement_check(url))

    print(bingo)