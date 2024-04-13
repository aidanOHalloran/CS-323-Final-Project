import requests

class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.example.com/"  # Replace with the actual API URL

    def fetch_movies(self, genre=None, year=None, rating=None):
        # Logic to fetch movies based on genre and year
        pass
