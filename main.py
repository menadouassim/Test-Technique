import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API-KEY')
# set up the request parameters
params = {
  'api_key': API_KEY,
  'q': 'domino’s pizza',
  'location': "Paris,Paris,Ile-de-France,France",
  'page': "1",
  'num': "20",
  'device': "mobile"
}
#Apparently the num parameter is not working to set the number of results 
#A workaround is to set max_page to 2 



# make the http GET request to Scale SERP
api_result = requests.get('https://api.scaleserp.com/search', params)

# print the JSON response from Scale SERP
print(json.dumps(api_result.json()))

with open("resultats.json", "w", encoding="utf-8") as file:
    json.dump(api_result.json(), file, indent=4, ensure_ascii=False)