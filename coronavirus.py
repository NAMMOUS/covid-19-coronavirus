import requests
import json

def corona(code):
    url = "https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code="+code
    response = requests.request("GET", url)
    my_json=json.loads(response.text)
    print("recovered cases: ",my_json['latest']['recovered'])


corona("FR")









