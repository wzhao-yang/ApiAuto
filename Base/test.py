import requests
import json

# url = "http://gouta-www-qa-01.gouta.cn/api/v1/login/loginWithSms?"
url = "http://gouta-www-qa-01.gouta.cn/api/v1/order/myOrderList?1591183607545"
# body = "{'mobile':'15801081111','captchaCode':'9527','mobileCode':'952700'}"
body1 = {"mobile": "15677964433", "captchaCode": "9527", "mobileCode": "952700"}

body = {
    'appId': '20190222302079100001',
    'secretKey': '0aa49921a32e4ec0b3f0e49b75122c96',
    'grant_type': 'client_credentials'
}
data = json.dumps(body1)
print(type(data))

headers = {"Content-Type":"application/json","Accept":"application/json,*/*","x-device-info": "1.0/nil/1/1.0"}
res = requests.get(url=url, data=data, headers=headers).text
print(res)
print((headers))


