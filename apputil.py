# Exercise 1

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

# Exercise 2

import requests

class Genius:
    def get_artist(self, search_term):

        search_term = search_term
        genius_url = "http://api.genius.com/search?q={search_term}" \
        "&access_token={ACCESS_TOKEN}"

        resp = requests.get(genius_url, headers = {"Authorization":
                            "Bearer " + ACCESS_TOKEN})
        json_data = resp.json()

