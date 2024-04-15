import requests

class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3/discover/movie"  # Replace with the actual API URL

    def fetch_movies(self, genre, year, rating,  adult_rating):
        url = self.base_url + f"?include_adult={adult_rating}&include_video=false&language=en-US&page=1&primary_release_year={year}&sort_by=popularity.desc&with_genres={genre}"
        
        
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            movies = response.json()
            return movies
        else:
            print(f"Failed to fetch movies. Error code: {response.status_code}")
            return None
