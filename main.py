import requests
import base64
import datetime

url = "https://accounts.spotify.com/api/token"

client_id = '8b71a13f84be4ca487b59c366a4b8ea3'
client_secret = 'c4a40a6734ff43afaa7dd181e6ddfe7e'

# forming auth credentials
client_creds = f'{client_id}:{client_secret}'
client_creds_b64 = base64.b64encode(client_creds.encode())

token_data = {'grant_type': 'client_credentials'}
token_head = {'Authorization': f'Basic {client_creds_b64.decode()}', 'Content-Type': 'application/x-www-form-urlencoded'}


# making a request and getting access token
req = requests.post(url, headers=token_head, params=token_data)
valid_status_code = req.status_code in range(200, 299)
if valid_status_code:
    token_response_data = req.json()
    access_token = token_response_data.get('access_token')

    # count due time to expire
    def did_expire():
        now = datetime.datetime.now()
        expires_in = token_response_data.get('expires_in')
        expire = now + datetime.timedelta(seconds=expires_in)
        if_expire = expire < now
        print(if_expire)

    did_expire()
else:
    print(req.status_code)
