class UserPreferences:
    def __init__(self):
        self.genre = None
        self.min_year = None
        self.min_rating = None

    def set_preferences(self, genre, min_year, min_rating):
        self.genre = genre
        self.min_year = min_year
        self.min_rating = min_rating
