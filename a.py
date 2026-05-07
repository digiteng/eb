import os
import requests

# API_KEY = os.environ.get('API_KEY')
# apiKey = os.getenv('api_key')

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
# API_KEY="edd1f597c6e64095cbed56dcac471f49"
lat="36.9"
lon="30.7"
lang="en"



def main():
	# API_KEY = os.getenv('API_KEY')
	ENV_KEY = os.getenv('APIKEY')
	url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={ENV_KEY}&units=metric&lang={lang}"
	data = requests.get(url, stream=True, allow_redirects=True, headers=header).json()
	print(data)

if __name__ == "__main__":
	main()




