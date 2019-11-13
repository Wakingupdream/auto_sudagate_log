from urllib import request, parse
import requests
while(1):
 # 请求头
 headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'onnection': 'keep-alive',
  'Content-Length': '66',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'sunriseUsername=20174227023; sunriseDomain=campus; think_language=zh-CN; PHPSESSID=g53e83of8ek8n55ir8vuh4tdi6',
  'Host': 'a.suda.edu.cn',
  'Origin': 'http://a.suda.edu.cn',
  'Referer': 'http://a.suda.edu.cn/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
  'X-Requested-Wit': 'XMLHttpRequest'}
 post_data = {
  'username': '20174227023',
  'password': '',#加密后的密码，需自己网页源代码找
  'enablemacauth': '0'}
 # 发送post请求登录网页
 requests.post('http://a.suda.edu.cn/index.php/index/login', data=post_data, headers=headers)

 import time

 time.sleep(18000)

 #######退出
 header1 = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Content-Length': '0',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'sunriseDomain=campus; think_language=zh-CN; sunriseUsername=20175227073; PHPSESSID=mgl9kk6to4vl8i68n4lgbghvh6',
  'Origin': 'http://a.suda.edu.cn',
  'Referer': 'http://a.suda.edu.cn/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
 }

 requests.post('http://a.suda.edu.cn/index.php/index/logout', headers=header1)
