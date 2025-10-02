import requests
import os

class Genius:
    """
    A class that stores the access token.
    """
    def __init__(self, access_token):
        """
        Initializes Genius with the access_token.

        Parameters:
        access_token (str): API access token.
        """
        self.access_token = access_token
        self.headers = {"Authorization": "Bearer " + self.access_token}
        

class Genius:
    def get_artist(self, search_term):

        ACCESS_

        search_url = f"https://api.genius.com/search?q={search_term}"
        resp = requests.get(search_url, headers = self.headers)
        
        search_data = resp.json()

        artist_id = search_data['resp']['hits'][0]['result']['primary_artist']['id']
        artist_url = f"{self.genius_url}/artists/{artist_id}"

        resp = requests.get(artist_url, headers = self.headers)
        resp.raise_for_status()

        return resp.json()

Genius.get_artist("Radiohead")