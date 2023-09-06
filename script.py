import requests

#function for api call which takes energidataservice url as an argument and returns requested data or metadata
def fetch_data(data_url):
    response = requests.get(
        url=data_url)

    result = response.json()
    
    return result