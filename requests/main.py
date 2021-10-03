import requests, json

api_url = "https://pokeapi.co/api/v2/pokemon/charizard"

response = requests.get(api_url)

pretty_json_response = json.loads(response.text)
print(json.dumps(pretty_json_response, indent=2))