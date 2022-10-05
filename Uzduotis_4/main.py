# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.


"""Movie class which has title, director and budget
"""

'''Movie method shows movie title
'''


class Movie:
    def __init__(self, movie_title, movie_director, movie_budget):
        self.title = movie_title
        self.director = movie_director
        self.budget = movie_budget

    def show_title(self):
        return self.title


movie1 = Movie('Star', "John Smith", 300000);
movie2 = Movie('Hi', 'Alison Lok', 50000000);
movie3 = Movie('Top 10', 'Kitty Garden', 1000);

print(movie1.show_title(), movie2.show_title(), movie3.show_title())
print('***************************')

movies = [movie1, movie2, movie3]


def was_expensive(obj):
    for item in obj:
        if item.budget > 10000000:
            print({item.show_title(): True})
        else:
            print({item.show_title(): False})


was_expensive(movies)
