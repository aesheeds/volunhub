import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("JSEARCH_API_KEY")

def send_query(string, location=None, employment_types=None, job_requirements=None):
    headers = { 'x-api-key': api_key }
    response = requests.request(
        'GET', 
        'https://api.openwebninja.com/jsearch/search-v2',
        params={"query":string},
        headers=headers
    )

    data = response.json()

    if response.statuscode != 200:
        print("Jsearch error:")
        print(data)
        return None

    return response.json()

if __name__ == "__main__":
    send_query('graphics programming')