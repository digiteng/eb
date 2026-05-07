import os
import requests
# SRC = os.environ.get('SOURCE')

# exec(str(SRC), globals())

api_key = os.environ.get('API_KEY')

if api_key:
	print(f"Secret successfully retrieved! {api_key}")
	# Use your secret here
else:
	print("Secret not found.")
