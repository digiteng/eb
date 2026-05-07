import os
import requests
# SRC = os.environ.get('SOURCE')

# exec(str(SRC), globals())

api_key = os.environ.get('API_KEY')

if api_key:
	print("Secret successfully retrieved!")
	# Use your secret here
else:
	print("Secret not found.")
