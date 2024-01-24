class Movie:
    
    def __init__(self, index, title, year, genre):
        self.index = index
        self.title = title
        self.year = year
        self.genre = genre
        self.play_counter = 0
       
    def play(self):
        self.play_counter += 1
       
    def __str__(self):
        return (f"{self.title} year {self.year}")
       
    def __repr__(self):
        return (f"Index: {self.index}\n"
                f"Title: {self.title.title()}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.genre.title()}\n"
                f"Played: {self.play_counter} times\n")
        
    def __eq__(self, other):
        return all (
            (
                (self.title).strip().lower() == (other.title).strip().lower(),
                self.year == other.year,
            )
        )