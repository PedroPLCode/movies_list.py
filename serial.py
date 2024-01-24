from movie import Movie

class Serial(Movie):
    
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        
    def __str__(self):
        return (f"{self.title} S{format_number(self.season)}E{format_number(self.episode)}")
        
    def __repr__(self):
        return (f"Index: {self.index}\n"
                f"Title: {self.title.title()}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.genre.title()}\n"
                f"Season: {format_number(self.season)}\n"
                f"Episode: {format_number(self.episode)}\n"
                f"Played: {self.play_counter} times\n")

def format_number(number):
    return f"0{number}" if number < 10 else number