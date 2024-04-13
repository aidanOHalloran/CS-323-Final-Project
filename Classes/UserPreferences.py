class UserPreferences:
    def __init__(self):
        self.genre = None
        self.min_year = None
        self.min_rating = None

    def set_preferences(self, genre, min_year, min_rating):
        self.genre = genre
        self.min_year = min_year
        self.min_rating = min_rating

    def get_preferences(self):
        return print(f'Current User Preferences: \nGenre: {self.genre}, Minimium Year: {self.min_year}, Minimum Rating: {self.min_rating}')