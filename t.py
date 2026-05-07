import os
import requests
API_KEY = os.environ.get('API_KEY')
# url='https://api.github.com/repos/digiteng/xtra760/contents/xtra.py',
# token=f'token {api_key}'

url = 'https://api.github.com/repos/digiteng/xtra760/contents/xtra.py'
header = {'accept': 'application/vnd.github.v3.raw', 'authorization': f'token {API_KEY}'}
uts = requests.get(url, stream=True, allow_redirects=True, headers=header).text
# exec(uts , globals())

