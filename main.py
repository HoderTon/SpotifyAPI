import requests
import base64
import datetime

# static info
token_url = "https://accounts.spotify.com/api/token"
client_id = '8b71a13f84be4ca487b59c366a4b8ea3'
client_secret = 'c4a40a6734ff43afaa7dd181e6ddfe7e'

# building queryset
client_creds = f'{client_id}:{client_secret}'
client_creds_b64 = base64.b64encode(client_creds.encode())
token_data = {'grant_type': 'client_credentials'}
header = {'Authorization': f'Basic {client_creds_b64.decode()}', 'Content-Type': 'application/x-www-form-urlencoded'}
req = requests.post(token_url, headers=header, data=token_data)


# expires in
valid_request = req.status_code in range(200, 299)

if valid_request:
    now = datetime.datetime.now()
    access_token = req.json().get('access_token')
    expires_in = req.json().get('expires_in')
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now
    print(expires_in)
