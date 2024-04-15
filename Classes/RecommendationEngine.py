class RecommendationEngine:
    @staticmethod
    def recommend(movies):
        for movie in movies['results']:
            print(f"Recommendation #{movies['results'].index(movie) + 1}")
            print(f"Title: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            print(f"Overview: {movie['overview']}")
            print("="*50)  # Separator line for better readability
        return movies