import os

def apiKy():
	api_key = os.environ.get('API_KEY')
	return api_key
