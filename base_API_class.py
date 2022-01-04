import base64
import datetime
import requests

from main import client_secret, client_id


class SpotifyAPI(object):
    access_token = None
    access_token_expires = None
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_creds(self):
        '''
        Returns a base64 encoded string
        '''
        # updating credentials
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_secret == None:
            raise Exception('Please provide client_id and client_secret!')
        # encoding credentials
        client_creds = f'{client_id}:{client_secret}'
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_header(self):
        client_creds_b64 = self.get_client_creds()
        return {'Authorization': f'Basic {client_creds_b64}', 'Content-Type': 'application/x-www-form-urlencoded'}

    def get_token_data(self):
        return {'grant_type': 'client_credentials'}

    def perform_auth(self):

        token_url = self.token_url
        header = self.get_token_header()
        token_data = self.get_token_data()
        req = requests.post(token_url, headers=header, data=token_data)
        # expires in
        if req.status_code not in range(200, 299):
            return False
        now = datetime.datetime.now()
        data = req.json()
        access_token = data.get('access_token')
        expires_in = data.get('expires_in')
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

client = SpotifyAPI(client_id, client_secret)

client.perform_auth()
access_token = client.access_token
