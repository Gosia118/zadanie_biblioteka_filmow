import random

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        
        self.number_of_plays = 0

    def play(self, step = 1):
        self.number_of_plays += step

    def __str__(self):
        return f"{self.title} ({self.year})"
    
    def __repr__(self):
        return self.title

    
class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"
    

def get_movies():
    print("Filmy:")
    list_of_movies = list(filter(lambda x: isinstance(x, Movie) and not isinstance(x, Series), library))
    movies_sorted_by_title = sorted(list_of_movies, key=lambda movie: movie.title)
    print(movies_sorted_by_title)


def get_series():
    print("Seriale:")
    list_of_series = list(filter(lambda x : isinstance(x, Series), library))
    series_sorted_by_title = sorted(list_of_series, key=lambda series: series.title)
    print(series_sorted_by_title)

def search():
    searched_title = input("Podaj tytuł: ")
    found = False
    for item in library:
        if item.title == searched_title:
            found = True
            break
    if found:        
        print(f"Znaleziono tytuł: {searched_title}")
    else:
        print(f"Nie znaleziono tytułu: {searched_title}")

def generate_views():
    item = random.choice(library)
    number_of_plays = random.randint(1, 100)
    item.play(number_of_plays)
    print (f"{item} - ilość odtworzeń {number_of_plays}")

def generate_views_10_times(generate_views):
    print("--------")
    for i in range(10):
        generate_views()

def top_titles():
    print("Najpopularniejsze tytuły z biblioteki")
    a = int(input("Podaj liczbę: "))
    sorted_titles = sorted(library, key=lambda item: item.number_of_plays, reverse=True)
    for item in sorted_titles[:a]:
        print(f"{item} - ilość odtworzeń {item.number_of_plays}")


if __name__ == "__main__":
    movie1 = Movie("Once Upon a Time in Hollywood", 2019, "comedy drama")
    movie2 = Movie("Little Women", 2019, "drama")
    movie3 = Movie("Parasite", 2019, "thriller")
    movie4 = Movie("Ford v Ferrari", 2019, "sports drama")
    movie5 = Movie("Green Book", 2018, "comedy drama")
    movie6 = Movie("Get Out", 2017, "horror")
    movie7 = Movie("Lady Bird", 2017, "comedy drama")
    movie8 = Movie("Dunkirk", 2017, "war")
    movie9 = Movie("Three Billboards Outside Ebbing, Missouri", 2017, "comedy crime")
    movie10 = Movie("Manchester by the Sea", 2016, "drama")
    movie11 = Movie("Hidden Figures", 2016, "biographical")
    movie12 = Movie("Mad Max: Fury Road", 2015, "action")
    series1 = Series(10, 3, "The Good Place", 2016, "comedy")
    series2 = Series(15, 4, "The Office", 2005, "comedy")
    series3 = Series(6, 2, "The White Lotus", 2021, "drama")
    series4 = Series(8, 4, "Succession", 2018, "drama")
    series5 = Series(8, 2, "Better Call Saul", 2015, "drama")
    series6 = Series(6, 1, "Lessons in Chemistry", 2023, "drama")

    library = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11, movie12, series1, series2, series3, series4, series5, series6]

    print("Bibliotekę filmów i seriali")
    print(movie1)
    print(series1)
    get_movies()
    get_series()
    search()
    generate_views()
    generate_views_10_times(generate_views)
    top_titles()
    