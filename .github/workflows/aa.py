# my_script.py
import os

# Use os.environ.get to safely access the variable
api_key = os.environ.get('API_KEY')

if api_key:
    print("Secret successfully retrieved!")
    # Use your key here...
else:
    print("Secret not found.")
