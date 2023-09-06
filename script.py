import requests, json

#function for api call which takes energidataservice url as an argument and returns requested data or metadata
def fetch_data(data_url):
    response = requests.get(
        url=data_url)

    result = response.json()
    
    return result

#create local json-file with chosen name and fetched data
def create_local_file(filename, energidataservice_url):
    out_file = open(filename, "w")
    json.dump(fetch_data(energidataservice_url), out_file)
    out_file.close()
    print(f"Created file: {filename}")


create_local_file("dataset.json", 'https://api.energidataservice.dk/dataset/CO2Emis?start=now-P1Y&end=now&limit=7')
create_local_file("metadata.json",'https://api.energidataservice.dk/meta/dataset/CO2Emis')

#direct download example: https://api.energidataservice.dk/dataset/CO2Emis/download?format=json&limit=7