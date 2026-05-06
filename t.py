import os

# Get the secret from the environment variable
api_key = os.getenv("MY_API_KEY")

if api_key is None:
    print("Error: API_KEY not found in environment!")
else:
    print("Successfully retrieved API key.")
    # Use your key here...
