import os

# Access the secret mapped in the YAML 'env' section
API_KEY = os.environ.get('API_KEY')
print(f"Using key: {API_KEY[:2]}***") # Masking for safety
