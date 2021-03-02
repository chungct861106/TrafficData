import requests
from requests.auth import HTTPBasicAuth
url = "https://traffic.transportdata.tw/MOTC/v2/Road/Traffic/SectionShape/Highway?$top=30&$format=JSON"
params = { '$top':30,'$format':'JSON'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get(url, headers=headers).json()
print(res.status_code)