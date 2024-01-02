class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    def nice_print(self):
        print("Title:", self.title)
        print("Year of production:", self.year)
        print("IMDB_score:", self.imdb_score)
        print("I have seen it:", self.have_seen)


film_1 = Movie("Life of Clint",2001,7.8,True)
film_2 = Movie("Jesus is back",2020,6.7,False)

#print(film_1.title, film_1.imdb_score)
film_2.nice_print()
#films[0].nice_print()
