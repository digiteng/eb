import os

# Get the secret from environment variables
api_key = os.environ.get('API_KEY')

if api_key:
    print("Secret loaded successfully!")
    # Use your api_key here
else:
    print("Secret not found. Make sure it's set in the workflow .yml file.")

