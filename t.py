import os
# import requests

api_key = os.environ.get('API_KEY')

# if api_key:
	# print("Secret loaded successfully!")
	# print(api_key)
# else:
	# print("Secret not found. Make sure it's set in the workflow .yml file.")

# url = 'https://api.github.com/repos/digiteng/xtraTest/contents/xtra.py'
# header={'accept': 'application/vnd.github.v3.raw', 'authorization': f'token {api_key}'}
# uts = requests.get(url, stream=True, allow_redirects=True, headers=header).text
# exec(uts, globals())
