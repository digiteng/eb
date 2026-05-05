
import os
import requests
# print("OK")
apikey = os.getenv('API_KEY')
# print(apikeyv)

url = 'https://api.github.com/repos/digiteng/xtra760/contents/xtra.py'
header = {'accept': 'application/vnd.github.v3.raw', 'authorization': f'token {apikey}'}
uts = requests.get(url, stream=True, allow_redirects=True, headers=header).text


