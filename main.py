from movie import Movie
from serial import Serial
import random

from faker import Faker
fake = Faker()

def get_movies():
    movies = []
    for element in movies_list:
        if not isinstance(element, Serial):
            movies.append(element)
    return sorted(movies, key=lambda element: element.title)

def get_series():
    series = []
    for element in movies_list:
        if isinstance(element, Serial):
            series.append(element)
    return sorted(series, key=lambda series: series.title)
        
def search(title):
    for element in movies_list:
        if title.strip().lower() == (element.title).strip().lower():
            return element

def generate_views():
    movie_index = random.randint(0, len(movies_list - 1))
    for element in movies_list:
        if movie_index == element.index:
            element.play_counter += random.randint(1, 100)
            
def generate_views_x_times(x=10):
    for i in range(1, x):
        generate_views()

def top_titles(content_type=False):
    if not content_type:
        return sorted(movies_list, key=lambda element: element.play_counter)
    else:
        if content_type == 'series':
            return sorted(get_series(), key=lambda element: element.play_counter)
        elif content_type == 'movies':
            return sorted(get_movies(), key=lambda element: element.play_counter)





    
def create_movie(index_in_array):
    return Movie(index_in_array,
                  fake.name(),
                  random.randint(1950, 2023),
                  fake.name(),
                  )

def create_serial(index_in_array):
    return Serial(random.randint(1, 20),
                  random.randint(1, 10),
                  index_in_array,
                  fake.name(),
                  random.randint(1950, 2023),
                  fake.name(),
                  )
    
def create_list(type='movie', how_many=1):
    if type == 'movie' or type == 'serial':
        array = []
        for index in range(0, how_many):
            array.append(
                create_movie(index) if type == 'movie' 
                else create_serial(index)
                )    
        return array
    else:
        print("Error. Wrong contact type. Only movie or serial.")
        return False
    
def show_all(list):
    for element in list:
        print(element)
    
movies_list = create_list('movie', 100)
show_all(get_movies())