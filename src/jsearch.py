import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("JSEARCH_API_KEY")


def send_query(string, location=None,
               employment_types=None,
               job_requirements=None):

    # try three times if gemini gives an error
    for attempt in range(3):
        headers = {'x-api-key': api_key}
        response = requests.request(
            'GET',
            'https://api.openwebninja.com/jsearch/search-v2',
            params={"query": string},
            headers=headers
        )
        if response.status_code == 200:
            break
        else:
            print(f"attempt: {attempt} JSearch Query Failed retrying . . .")

    data = response.json()
    if response.status_code != 200:
        print("Jsearch error:")
        print(data)
        return None
    else:
        print("Successfully queried JSearch\n")

    return response.json()


if __name__ == "__main__":
    send_query('graphics programming')
