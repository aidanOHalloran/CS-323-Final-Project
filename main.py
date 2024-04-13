from Classes.Movie import Movie
from Classes.UserPreferences import UserPreferences
from Classes.APIClient import APIClient
from Classes.RecommendationEngine import RecommendationEngine

import os

def GetGenre():
    print("Select a genre: ")
    print("1. Action")
    print("2. Comedy")
    print("3. Drama")
    print("4. Horror")
    print("5. Romance")
    genre = input("Enter your choice: ")
    if genre == "1":
        return "Action"
    elif genre == "2":
        return "Comedy"
    elif genre == "3":
        return "Drama"
    elif genre == "4":
        return "Horror"
    elif genre == "5":
        return "Romance"
    else:
        print("Invalid choice. Please try again.")
        GetGenre()
        
def GetMinYear():
    min_year = input("Enter the minimum year (ex: 2000): ")
    if min_year.isdigit():
        return min_year
    else:
        print("Invalid year. Please try again.")
        GetMinYear()

def GetMinRating():
    min_rating = input("Enter the minimum rating (1-10): ")
    if min_rating.isdigit() and 1 <= int(min_rating) <= 10:
        return min_rating
    else:
        print("Invalid rating. Please try again.")
        GetMinRating()

def SetPreferences():
    genre = GetGenre()
    min_year = GetMinYear()
    min_rating = GetMinRating()
    app.user_preferences.set_preferences(genre, min_year, min_rating)
    print("Preferences set successfully. Press enter to continue.")
    input()
    ClearScreen()
    
def GetRecommendations():
    if app.user_preferences.genre is None or app.user_preferences.min_year is None or app.user_preferences.min_rating is None:
        print("ERROR: Preferences not set...")
        print("Please set your preferences first. Press enter to continue...")
        input()
        ClearScreen()
        return
    
    movies = app.api_client.fetch_movies(app.user_preferences.genre, app.user_preferences.min_year)
    recommendations = RecommendationEngine.recommend(movies, app.user_preferences)
    
    if recommendations is None:
        print("No recommendations found. Please adjust your preferences.")
        print("Press enter to continue.")
        input()
        ClearScreen()
        return
    
    print("Recommended Movies:")
    for movie in recommendations:
        print(f"Title: {movie.title}, Year: {movie.year}, Genre: {movie.genre}, Rating: {movie.rating}")
    print("Press enter to continue.")
    input()
    ClearScreen()
    ShowMenu()

def ShowMenu():
    while True:
        print("Movie Recommendation System!\n")
        print("1. Set Preferences")
        print("2. Get Recommendations")
        print("3. Exit\n")
        choice = input("Enter menu choice: ")

        if choice == "1":
            ClearScreen()
            SetPreferences()
        elif choice == "2":
            GetRecommendations()
        elif choice == "3":
            print("Exiting the program...")
            break  # This exits the while loop and thus ends the program
        else:
            print("Invalid choice. Press enter try again...")
            input()
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
    api_key = "YOUR_API_KEY"  # Replace this with your actual API key
    app = Application(api_key)
    app.run()
