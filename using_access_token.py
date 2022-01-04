from base_API_class import access_token
import requests

# Using api
endpoint = 'https://api.spotify.com/v1/search'
header = {'Authorization': f'Bearer {access_token}'}

data = {'q': 'stay in the dark', 'type': 'track'}
r = requests.get(endpoint, headers=header, params=data)
print(r.json())
