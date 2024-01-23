class Movie:
    
    def __init__(self, index, title, year, genre):
        self.index = index
        self.title = title
        self.year = year
        self.genre = genre
        self._play_counter = 0

    @property
    def play_counter(self):
        return self._play_counter
    
    @play_counter.setter
    def play_counter(self, value):
        if value > self.play_counter:
            self.play_counter = value
        else:
            raise ValueError(f"Value {value} lower than actual play_counter {self.play_counter}")
       
    def play(self):
        self.play_counter += 1
       
    def __str__(self):
        return (f"{self.title} year {self.year}")
       
    def __repr__(self):
        return (f"Index: {self.index}\n"
                f"Title: {self.title.title()}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.genre.title()}\n"
                f"Played: {self._play_counter} times\n")
        
    def __eq__(self, other):
        return all (
            (
                (self.title).strip().lower() == (other.title).strip().lower(),
                self.year == other.year,
            )
        )
        