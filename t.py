print("test OK")
a="bbb"

import os

# Get the secret from environment variables
api_key = os.environ.get('MY_API_KEY')

if api_key:
    print("API Key loaded successfully!")
    # Use your key: response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
else:
    print("Error: API Key not found.")