from datetime import datetime
from Models.Movies.Movie import Movie


def test_movie_properties_and_methods():
    # Create an instance of the Movie class
    movie = Movie()

    # Test the title property and setter
    movie.title = "Test Movie"
    assert movie.title == "Test Movie"

    # Test the description property and setter
    movie.description = "A test movie description."
    assert movie.description == "A test movie description."

    # Test the duration_mins property and setter
    movie.duration_mins = 120
    assert movie.duration_mins == 120

    # Test the language property and setter
    movie.language = "English"
    assert movie.language == "English"

    # Test the release_date property and setter
    release_date = datetime(2023, 1, 1).date()
    movie.release_date = release_date
    assert movie.release_date == release_date

    # Test the country property and setter
    movie.country = "USA"
    assert movie.country == "USA"

    # Test the genre property and setter
    movie.genre = "Action"
    assert movie.genre == "Action"

    # Test the screening_list property and getSscreenings method
    assert movie.screening_list == []
    assert movie.getSscreenings() == []

    # Test the to_dict method
    movie_dict = movie.to_dict()
    assert movie_dict == {
        "title": "Test Movie",
        "description": "A test movie description.",
        "duration_mins": 120,
        "language": "English",
        "release_date": release_date,
        "country": "USA",
        "genre": "Action"
    }

    # Test the string representation
    movie_str = str(movie)
    assert movie_str == "Movie: title=Test Movie, description=A test movie description., duration_mins=120, language=English, release_date=2023-01-01, country=USA, genre=Action, screening_list=[]"

# Run the test if this script is executed
if __name__ == "__main__":
    test_movie_properties_and_methods()
