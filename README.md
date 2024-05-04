Реализовал 9 тестов для проверки приложения BooksCollector:

-Тест метода add_new_book: проверяем, что новая книга добавляется в books_genre, если её нет там. -Тест метода set_book_genre: проверяем, что жанр книги устанавливается правильно. -Тест метода get_book_genre: проверяем, что метод возвращает правильный жанр для заданной книги. -Тест метода get_books_with_specific_genre: проверяем, что метод возвращает список книг с заданным жанром. -Тест метода get_books_genre: проверяем, что метод возвращает словарь books_genre. -Тест метода get_books_for_children: проверяем, что метод возвращает список книг, подходящих для детей. -Тест метода add_book_in_favorites: проверяем, что книга успешно добавляется в избранное. -Тест метода delete_book_from_favorites: проверяем, что книга успешно удаляется из избранного. -Тест метода get_list_of_favorites_books: проверяем, что метод возвращает список избранных книг.


collected 9 items                                                                                                                                                                       

tests.py::TestBooksCollector::test_add_new_book_adds_book_to_books_genre PASSED                                                                                                   [ 11%]
tests.py::TestBooksCollector::test_set_book_genre_sets_correct_genre PASSED                                                                                                       [ 22%]
tests.py::TestBooksCollector::test_get_book_genre_returns_correct_genre PASSED                                                                                                    [ 33%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_returns_list_of_books PASSED                                                                                     [ 44%]
tests.py::TestBooksCollector::test_get_books_genre_returns_books_genre_dict PASSED                                                                                                [ 55%]
tests.py::TestBooksCollector::test_get_books_for_children_returns_books_without_age_rating PASSED                                                                                 [ 66%]
tests.py::TestBooksCollector::test_add_book_in_favorites_adds_book_to_favorites PASSED                                                                                            [ 77%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_removes_book_from_favorites PASSED                                                                                  [ 88%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_returns_list_of_favorite_books PASSED                                                                              [100%]


