import requests

def get_apod_data(date=None):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': 'DEMO_KEY',
        'date': date
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")
