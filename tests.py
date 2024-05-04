from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_adds_book_to_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('гордость и предубеждение')
        collector.add_new_book('преступление и наказание')
        assert 'гордость и предубеждение' in collector.get_books_genre()
        assert 'преступление и наказание' in collector.get_books_genre()

    def test_set_book_genre_sets_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сто лет тому вперед')
        collector.set_book_genre('Сто лет тому вперед', 'Детективы')
        assert collector.get_book_genre('Сто лет тому вперед') == 'Детективы'

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сёгун')
        collector.set_book_genre('Сёгун', 'Фантастика')
        assert collector.get_book_genre('Сёгун') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_list_of_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']
        assert collector.get_books_with_specific_genre('Детективы') == ['Преступление и наказание']

    def test_get_books_genre_returns_books_genre_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Чудесный отец')
        collector.set_book_genre('Чудесный отец', 'Фантастика')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        assert collector.get_books_genre() == {'Чудесный отец': 'Фантастика', 'Преступление и наказание': 'Детективы'}

    def test_get_books_for_children_returns_books_without_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гоблинские истории')
        collector.set_book_genre('Гоблинские истории', 'Фантастика')
        collector.add_new_book('Золушка')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Гоблинские истории', 'Золушка']

    def test_add_book_in_favorites_adds_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_removes_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_list_of_favorite_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Дюна']