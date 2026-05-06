import os

# def apiKy():
api_key = os.environ.get('API_KEY')
	# return api_key
uh=[
'https://api.github.com/repos/digiteng/xtra760/contents/xtra.py',
f"{'accept': 'application/vnd.github.v3.raw', 'authorization': 'token {api_key}'}"
]
