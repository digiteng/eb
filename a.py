import os
import requests

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
# API_KEY="edd1f597c6e64095cbed56dcac471f49"
lat="36.9"
lon="30.7"
lang="en"

def main():
	API_KEY = os.getenv('API_KEY')
	url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang={lang}"
	data = requests.get(url, stream=True, allow_redirects=True, headers=header).json()
	print(data)
	open("H:\tmp\aa.txt", "w").write("eeeeeeeeeeeeeeeeeeee")

if __name__ == "__main__":
	main()
