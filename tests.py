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
        collector.set_book_genre('Сто лет тому вперед', 'повесть')
        assert collector.get_book_genre('Сто лет тому вперед') == 'повесть'

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сёгун')
        collector.set_book_genre('Сёгуне', 'роман')
        assert collector.get_book_genre('Сёгун') == 'роман'

    def test_get_books_with_specific_genre_returns_list_of_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'фентази')
        collector.add_new_book('преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'детектив')
        assert collector.get_books_with_specific_genre('фентази') == ['Дюна']
        assert collector.get_books_with_specific_genre('детектив') == ['преступление и наказание']

    def test_get_books_genre_returns_books_genre_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Чудесный отец')
        collector.set_book_genre('Чудесный отец', 'повесть')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'детектив')
        assert collector.get_books_genre() == {'Чудесный отец': 'повесть', 'преступление и наказание': 'детектив'}

    def test_get_books_for_children_returns_books_without_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('гоблинские истории')
        collector.set_book_genre('гоблинские истории', 'фэнтези')
        collector.add_new_book('золушка')
        collector.set_book_genre('золушка', 'сказка')
        assert collector.get_books_for_children() == ['гоблинские истории', 'золушка']

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