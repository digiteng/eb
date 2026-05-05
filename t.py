print("test OK")
a="bbb"

import os

# Retrieve the environment variable
api_key = os.getenv("MY_API_KEY")

if api_key:
	print("API Key successfully loaded!")
	# Use your key here
else:
	print("Error: API Key not found.")
