import requests
import os
import pandas as pd

# Exercise 1 and 2

class Genius:
    """
    A class that accesses the Genius API.
    """

    # Exercise 1
    def __init__(self, access_token):
        """
        Initializes Genius with the access_token.

        Parameters:
        access_token (str): API access token.

        Return value:
        None
        """
        # Establish the access_token, headers and URL
        self.access_token = access_token
        self.headers = {"Authorization": "Bearer " + self.access_token}
        self.genius_url = "https://api.genius.com"

    # Exercise 2  
    def get_artist(self, search_term):
        """
        Gets the artist ID from the first
        "hit" of th search_term input.

        Parameters:
        search_term (str): The desired input for Genius.

        Return value:
        A dictionary containing the JSON object.
        """

        # Establish the search url result based on the input
        search_url = f"{self.genius_url}/search?q={search_term}"
        response = requests.get(search_url, headers = self.headers)
        
        search_data = response.json()

        if not search_data['response']['hits']:
            return None

        # Get the primary artist ID from the first "hit"
        # of the search_term input from Genius.
        artist_id = search_data['response']['hits'][0]['result']['primary_artist']['id']
        artist_url = f"{self.genius_url}/artists/{artist_id}"

        # Look up the artist using the result from the
        # lines above.
        response = requests.get(artist_url, headers = self.headers)
        response.raise_for_status()

        return response.json()

    # Exercise 3
    def get_artists(self, search_terms):
        """
        A method that provides a few pieces of relevant
        information based on the list of inputs.

        Parameters:
        search_terms (list): Multiple desired search terms.

        Return value:
        A pandas DataFrame containing a row for each search
        term and the columns: search_term, artist_name,
        artist_id and followers_count.
        """
        
        artist_data = []
        
        # Loop through each term in the list.
        for term in search_terms:
            try:
                # Running the .get_artist method from above
                # on each term in the list.
                artist_json = self.get_artist(term)

                # If there is nothing in that element of the
                # list than continue to the next element.
                if artist_json is None:
                    print(f"Warning: No artist for: '{term}'")
                    continue
                
                # Find the artist of each JSON object in the list.
                artist = artist_json['response']['artist']

                # Creating a dictionary of terms containing the 
                # information relevant to our desired DataFrame.
                data = {
                    'search_term':term,
                    'artist_name':artist.get('name'),
                    'artist_id':artist.get('id'),
                    'followers_count':artist.get('followers_count')
                    }

            # Print an error if there is an issue with the search term.
            except Exception as e:
                print(f"Error processing '{term}':{e}")
                continue
            
            # Append each pass of the loop onto the empty list
            # that we made at the start of the function.
            artist_data.append(data)

        return pd.DataFrame(artist_data)