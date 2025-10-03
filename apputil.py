import requests
import os
import pandas as pd

# Exercise 1 and 2

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
        self.genius_url = "https://api.genius.com"
        
    def get_artist(self, search_term):

        search_url = f"{self.genius_url}/search?q={search_term}"
        response = requests.get(search_url, headers = self.headers)
        
        search_data = response.json()

        if not search_data['response']['hits']:
            return None

        artist_id = search_data['response']['hits'][0]['result']['primary_artist']['id']
        artist_url = f"{self.genius_url}/artists/{artist_id}"

        response = requests.get(artist_url, headers = self.headers)
        response.raise_for_status()

        return response.json()

    def get_artists(self, search_terms):
        
        artist_data = []
        
        for term in search_terms:
            try:

                artist_json = self.get_artist(term)

                if artist_json is None:
                    print(f"Warning: No artist for: '{term}'")
                    continue
                
                artist = artist_json['response']['artist']

                data = {
                    'search_term':term,
                    'artist_name':artist.get('artist_name'),
                    'artist_id':artist.get('artist_id'),
                    'followers_count':artist.get('followers_count')
                    }

            artist_data.append(data)

        return pd.DataFrame(artist_data)