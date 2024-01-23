from movie import Movie

class Serial(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        
    def __str__(self):
        return (f"{self.title} S{self.season}E{self.episode}")
        
    def __repr__(self):
        return (f"Index: {self.index}\n"
                f"Title: {self.title.title()}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.genre.title()}\n"
                f"Season: {self.season}\n"
                f"Episode: {self.episode}\n"
                f"Played: {self._play_counter} times\n")