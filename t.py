print("test OK")
a="bbb"

import os

# Retrieve the environment variable
api_key = os.environ.get('API_KEY')
print(api_key)
if api_key:
	print("API Key successfully loaded!")
	# Use your key here
else:
	print("Error: API Key not found.")
