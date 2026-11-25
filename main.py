import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API-KEY')
if not API_KEY:
    raise ValueError("API-KEY not found in environment variables. Please set it in the .env file.")


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

def call_scale_serp_api(params):
    # make the http GET request to Scale SERP
    api_result = requests.get('https://api.scaleserp.com/search', params )
    
    # print the JSON response from Scale SERP
    #print(json.dumps(api_result.json()))
    
    save_results_to_json_file(api_result.json(), "resultats.json")

def save_results_to_json_file(results, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)
    print(f"Results saved to {filename}")

def main():
    call_scale_serp_api(params)

if __name__ == "__main__":
    main()