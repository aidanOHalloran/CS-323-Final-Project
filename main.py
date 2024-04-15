from Classes.Movie import Movie
from Classes.UserPreferences import UserPreferences
from Classes.APIClient import APIClient
from Classes.RecommendationEngine import RecommendationEngine

import os
from dotenv import load_dotenv

def GetGenre():
    print("Select a genre: ")
    print("1. Action")
    print("2. Comedy")
    print("3. Drama")
    print("4. Horror")
    print("5. Romance")
    genre = input("Enter your choice: ")
    if genre == "1":
        return "28"
    elif genre == "2":
        return "35"
    elif genre == "3":
        return "18"
    elif genre == "4":
        return "27"
    elif genre == "5":
        return "10749"
    else:
        print("Invalid choice. Please try again.")
        GetGenre()
        
def GetReleaseYear():
    release_year = input("Enter the release year (ex: 2000): ")
    if release_year.isdigit():
        return release_year
    else:
        print("Invalid year. Please try again.")
        GetReleaseYear()

def GetMinRating():
    min_rating = input("Enter the minimum rating (1-10): ")
    if min_rating.isdigit() and 1 <= int(min_rating) <= 10:
        return min_rating
    else:
        print("Invalid rating. Please try again.")
        GetMinRating()
        
def AllowAdultRating():
    print("Allow adult content?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        return "true"
    elif choice == "2":
        return "false"
    else:
        print("Invalid choice. Please try again.")
        AllowAdultRating()

def SetPreferences():
    genre = GetGenre()
    release_year = GetReleaseYear()
    min_rating = GetMinRating()
    adult_rating = AllowAdultRating()
    app.user_preferences.set_preferences(genre, release_year, min_rating, adult_rating)
    ClearScreen()
    print("Preferences set successfully.")
    input("Press enter to continue.")
    ClearScreen()
    
def GetRecommendations():
    if app.user_preferences.genre is None or app.user_preferences.release_year is None or app.user_preferences.min_rating is None:
        ClearScreen()
        print("ERROR: Preferences not set...\n")
        print("Please set your preferences first.")
        input("Press enter to continue.")
        ClearScreen()
        return
    
    movies = app.api_client.fetch_movies(app.user_preferences.genre, app.user_preferences.release_year, app.user_preferences.min_rating, app.user_preferences.adult_rating)
    recommendations = RecommendationEngine.recommend(movies)
    
    if recommendations is None:
        print("No recommendations found. Please adjust your preferences.")
        input("Press enter to continue.")
        ClearScreen()
        return
    
    print("Recommended Movies:")
    for movie in recommendations:
        print(f"Title: {movie.title}, Year: {movie.year}, Genre: {movie.genre}, Rating: {movie.rating}")
    input("Press enter to continue.")
    ClearScreen()

def ShowMenu():
    while True:
        ClearScreen()
        print("Movie Recommendation System!\n")
        print("1. Set Movie Preferences")
        print("2. Get Movie Recommendations")
        print("3. Exit\n")
        choice = input("Enter menu choice: ")

        if choice == "1":
            ClearScreen()
            SetPreferences()
            app.user_preferences.get_preferences()
            input("Press enter to continue...")
            ClearScreen()
        elif choice == "2":
            GetRecommendations()
        elif choice == "3":
            print("Exiting the program...")
            break  # This exits the while loop and thus ends the program
        else:
            print("Invalid choice.")
            input("Press enter try again...")
            ClearScreen()  # Clear the screen and show the menu again


def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Application:
    def __init__(self, api_key):
        self.api_client = APIClient(api_key)
        self.user_preferences = UserPreferences()

    def run(self):
        ShowMenu()

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv('API_KEY')
    app = Application(api_key)
    app.run()
