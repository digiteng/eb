import os

# Get the secret from the environment variable
clientsecret = os.getenv("client_secret")

if clientsecret is None:
    print("Error: API_KEY not found in environment!")
else:
    print("Successfully retrieved API key.")
    # Use your key here...
