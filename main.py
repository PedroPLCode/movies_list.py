from movie import Movie
from serial import Serial
from faker import Faker
from datetime import date
import random

fake = Faker()
today = date.today()

movies_list = []
genres_list = ["Action", "Drama", "Comedy", "Sci-Fi", "Document", "Historical"]

def main(movies_list):
    print("Biblioteka filmów.\n")
    movies_list += create_movies_list('serial', 4096)
    movies_list += create_movies_list('movie', 4096)
    movies_list += create_serial_full_season('Zorro', 2024, 'Action', 2, 13)
    movies_list += create_serial_full_season('Star Trek', 2000, 'Sci-Fi', 1, 24)
    generate_views_x_times(8192)
    date_formatted = today.strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {date_formatted}\n")
    show(top_titles(3))

def get_selected_type(type):
    if type == 'movies' or type == 'series':
        series = []
        movies = []
        for element in movies_list:
            if isinstance(element, Serial):
                series.append(element)
            else:
                movies.append(element)
        series = sorted(series, key=lambda series: series.title)
        movies = sorted(movies, key=lambda movies: movies.title)
        return series if type == 'series' else movies
    else:
        print("Error. Wrong movie type. Only movies or series.")
        return False
        
def search(title):
    results = []
    for element in movies_list:
        if title.strip().lower() == (element.title).strip().lower():
            results.append(element)
    return results

def generate_views():
    min = 0
    max = len(movies_list) - 1
    movie_index = random.randint(min, max)
    for element in movies_list:
        if movie_index == element.index:
            views_to_add = random.randint(1, 100)
            element.play_counter += views_to_add
            
def generate_views_x_times(x=10):
    for i in range(1, x):
        generate_views()

def top_titles(how_many=10, content_type=False):
    selected = get_selected_type(content_type) if content_type else movies_list
    return sorted(selected, key=lambda element: element.play_counter)[-how_many:][::-1]
        
def create_serial_episode(episode, season, index_in_array, title, year, genre):
    return Serial(episode,
                  season,
                  index_in_array,
                  title,
                  year,
                  genre,
                  )        

def create_serial_full_season(title, year, genre, season, episodes):
    array = []
    for episode_index in range(1, episodes):
        index_in_array = len(movies_list)
        array.append(create_serial_episode(episode_index, season, index_in_array, title, year, genre))
    return array

def count_serial_episodes(title):
    episodes_counter = 0
    for element in movies_list:
        if title.strip().lower() == (element.title).strip().lower():
            episodes_counter += 1
    return episodes_counter
    
def get_random_genre():
    return random.choice(genres_list)

def get_random_year():
    return random.randint(1950, 2023)

def create_fake_item(type, index_in_array):
    if type == 'movie':
        return Movie(index_in_array,
                    fake.name(),
                    get_random_year(),
                    get_random_genre(),
                    )
    elif type == 'serial':
        return Serial(random.randint(1, 20),
                    random.randint(1, 10),
                    index_in_array,
                    fake.name(),
                    get_random_year(),
                    get_random_genre(),
                    )
    else:
        return False
    
def create_movies_list(type='movie', how_many=10):
    if type == 'movie' or type == 'serial':
        array = []
        for index in range(0, how_many):
            new_item = create_fake_item(type, index)
            array.append(new_item)    
        return array
    else:
        print("Error. Wrong type. Only movie or serial.")
        return False
    
def show(list):
    if not list:
        print("Error. List empty.")
        return False
    for element in list:
        print(repr(element))
    
main(movies_list)