import os
import requests
# api_key = os.environ.get("API_KEY")
api_key = os.getenv('API_KEY')
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
# api_key="edd1f597c6e64095cbed56dcac471f49"
lat="36.9"
lon="30.7"
lang="en"
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang={lang}"
data = requests.get(url, stream=True, allow_redirects=True, headers=header).json()
print(data)
