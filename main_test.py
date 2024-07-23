from main import MoviesLibrary


def test_add_movie():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])
    library.add_movie('Комедия', 'Весёлый питонист')
    recommendations = library.recommend('Комедия')
    assert 'Весёлый питонист' in recommendations, "Ошибка: Фильм не добавлен в Комедию."


def test_recommend():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])
    library.add_movie('Комедия', 'Три разраба и тестировщик')
    recommendations = library.recommend('Комедия')
    assert recommendations == ['Три разраба и тестировщик'], "Ошибка: Рекомендации неверны."


def test_shared_movies_list():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])
    library.add_movie('Ужасы', 'Страшный фильм')
    library.add_movie('Комедия', 'Весёлый питонист')
    assert 'Страшный фильм' in library.recommend('Ужасы'), "Ошибка: Фильм 'Страшный фильм' не найден в Ужасах."
    assert 'Весёлый питонист' in library.recommend('Комедия'), "Ошибка: Фильм 'Весёлый питонист' не найден в Комедии."
    assert 'Весёлый питонист' not in library.recommend('Ужасы'), "Ошибка: Фильм 'Весёлый питонист' найден в Ужасах."
    assert 'Страшный фильм' not in library.recommend('Комедия'), "Ошибка: Фильм 'Страшный фильм' найден в Комедии."


def test_add_movie_to_nonexistent_genre():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])
    try:
        library.add_movie('Драма', 'Драматичный фильм')
        assert False, "Ошибка: Добавление фильма в несуществующий жанр должно вызвать ошибку."
    except KeyError:
        pass


def test_recommend_nonexistent_genre():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])
    try:
        library.recommend('Драма')
        assert False, "Ошибка: Получение рекомендаций для несуществующего жанра должно вызвать ошибку."
    except KeyError:
        pass
    