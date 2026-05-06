import os

# Get the secret from environment variables
api_key = os.environ.get('API_KEY')

if api_key:
	print("Secret loaded successfully!")
	print(api_key)
else:
	print("Secret not found. Make sure it's set in the workflow .yml file.")

