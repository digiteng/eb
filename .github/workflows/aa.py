# my_script.py
import os

# Use os.environ.get to safely access the variable
API_KEY = os.environ.get('API_KEY')

if API_KEY:
	print("Secret successfully retrieved!")
	# Use your key here...
else:
	print("Secret not found.")
