class UserPreferences:
    def __init__(self):
        self.genre = None
        self.release_year = None
        self.adult_rating = None

    def set_preferences(self, genre, release_year, rating, adult_rating):
        self.genre = genre
        self.release_year = release_year
        self.min_rating = rating
        self.adult_rating = adult_rating

    def get_preferences(self):
        return print(f'Current User Preferences: \n\nGenre: {self.genre}\nRelease Year: {self.release_year}\nInclude Adult Ratings: {self.adult_rating}\n')