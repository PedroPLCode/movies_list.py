from movie import Movie
from serial import Serial
import random
from faker import Faker
from datetime import date

fake = Faker()
today = date.today()

def get_movies():
    movies = []
    for element in movies_list:
        if not isinstance(element, Serial):
            movies.append(element)
    return sorted(movies, key=lambda element: element.title)
# te dwie w jedną funkcję zrobić
def get_series():
    series = []
    for element in movies_list:
        if isinstance(element, Serial):
            series.append(element)
    return sorted(series, key=lambda series: series.title)
        
def search(title):
    search_results = []
    for element in movies_list:
        if title.strip().lower() == (element.title).strip().lower():
            search_results.append(element)
    return search_results

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
    if not content_type:
        return sorted(movies_list, key=lambda element: element.play_counter)[-how_many:]
    else:
        if content_type == 'series':
            return sorted(get_series(), key=lambda element: element.play_counter)[-how_many:]
        elif content_type == 'movies':
            return sorted(get_movies(), key=lambda element: element.play_counter)[-how_many:]
        
def create_serial_episode(episode, season, index_in_array, title, year, genre):
    return Serial(episode,
                  season,
                  index_in_array,
                  title,
                  year,
                  genre,
                  )        

def add_serial_full_season(title, year, genre, season, episodes):
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
    return random.choice(["Action", "Drama", "Comedy", "Sci-Fi", "Document", "Historical"])

def get_random_year():
    return random.randint(1950, 2023)

def create_fake_movie(index_in_array):
    return Movie(index_in_array,
                  fake.name(),
                  get_random_year(),
                  get_random_genre(),
                  )

def create_fake_serial(index_in_array):
    return Serial(random.randint(1, 20),
                  random.randint(1, 10),
                  index_in_array,
                  fake.name(),
                  get_random_year(),
                  get_random_genre(),
                  )
    
def create_list(type='movie', how_many=1):
    if type == 'movie' or type == 'serial':
        array = []
        for index in range(0, how_many):
            array.append(
                create_fake_movie(index) if type == 'movie' 
                else create_fake_serial(index)
                )    
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
    
    
print("Biblioteka filmów.\n")
movies_list = []
movies_list += create_list('serial', 2048)
movies_list += create_list('movie', 2048)
movies_list += add_serial_full_season('Zorro', 2024, 'Action', 2, 13)
movies_list += add_serial_full_season('Star Trek', 2000, 'Sci-Fi', 1, 24)
generate_views_x_times(4096)

date_formatted = today.strftime("%d.%m.%Y")
print(f"Najpopularniejsze filmy i seriale dnia {date_formatted}\n")
show(top_titles(3))