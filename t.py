import os

# Get the secret from the environment variable
clientsecret = os.environ.get('MY_API_KEY')
print(clientsecret)
if clientsecret is None:
    print("Error: API_KEY not found in environment!")
else:
    print("Successfully retrieved API key.")
    # Use your key here...
