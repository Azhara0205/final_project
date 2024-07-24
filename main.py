class MoviesLibrary:
    def __init__(self, genres):
        self.data = {genre: [] for genre in genres}

    def add_movie(self, genre, title):
        if genre in self.data:
            self.data[genre].append(title)
        else:
            raise KeyError(f"Жанр '{genre}' не найден.")

    def recommend(self, genre):
        if genre in self.data:
            return self.data[genre]
        else:
            raise KeyError(f"Жанр '{genre}' не найден.")


if __name__ == '__main__':
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    library.add_movie('Комедия', 'Весёлый питонист')
    library.add_movie('Комедия', 'Три разраба и тестировщик')

    print(library.recommend('Комедия'))

