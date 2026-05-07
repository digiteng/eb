import os

# Fetch the secret from environment variables
# api_key = os.environ.get("API_KEY")
api_key = os.getenv('API_KEY')

if api_key:
	print("Secret successfully loaded!")
	# Use your key here
else:
	print("Secret not found.")
