import pytest
import allure
import requests

API_URL = "https://web-gate.chitai-gorod.ru/api/v2/search"
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxODk4OTQ2LCJpYXQiOjE3NDY4NDg5MzMsImV4cCI6MTc0Njg1MjUzMywidHlwZSI6MjB9.x59NzYNYlBQ9ea4m9x36xi-iYrdi2mlhV2YAevsF-9s'
header = {
    'authorization': f'Bearer {token}',
'content-type': 'application/json'
}


@allure.story("API Книги")
@allure.title("Поиск книги по названию")
def test_search_book():
    params = {
        "suggests[page]": 1,
        "suggests[per-page]": 5,
        "phrase": "Волшебник"
    }

    response = requests.get(API_URL, params=params)


    print(response.url)  # Выведет: https://example.com/search?q=python+requests&page=2
    print(response.status_code)
    print(response.text)


@allure.story("API Книги")
@allure.title("Поиск книги по автору")
def test_search_by_author():
    """Тест поиска книг по автору 'Пушкин'"""
    author_name = "Пушкин"

    # Правильное формирование параметров запроса
    params = {
        "suggests[page]": 1,
        "suggests[per-page]": 5,
        "phrase": author_name,
        "include": "products,authors,bookCycles,publisherSeries,publishers,categories"
    }

    response = requests.get(API_URL, params=params)

    print(response.url)  # Выведет: https://example.com/search?q=python+requests&page=2
    print(response.status_code)
    print(response.text)



@allure.story("API Книги")
@allure.title("Поиск книги по жанру")
def test_search_book3():
    """Тест поиска книг по жанру 'психология'"""
    genre = "психология"

    # Правильное формирование параметров запроса
    params = {
        "suggests[page]": 1,
        "suggests[per-page]": 5,
        "phrase": genre,
        "include": "products,authors,bookCycles,publisherSeries,publishers,categories"
    }
    response = requests.get(API_URL, params=params)

    print(response.url)  # Выведет: https://example.com/search?q=python+requests&page=2
    print(response.status_code)
    print(response.text)


@allure.story("API Книги")
@allure.title("Поиск книги negative")
def test_search_book4():
    """Тест обработки невалидных символов в поисковом запросе"""
    invalid_chars = "∆ ∑ ∏ ℜ ℑ"  # Математические символы
    expected_status = 422

    # Правильное формирование параметров
    params = {
        "suggests[page]": 1,
        "suggests[per-page]": 5,
        "phrase": invalid_chars,
        "include": "products,authors,bookCycles,publisherSeries,publishers,categories"
    }
    response = requests.get(API_URL, params=params)

    print(response.url)  # Выведет: https://example.com/search?q=python+requests&page=2
    print(response.status_code)
    print(response.text)


@allure.story("API Книги")
@allure.title("missing auth")
def test_search_book5():
    """Тест проверки доступа без токена авторизации"""
    test_phrase = "книга"
    expected_status = 403

    # Параметры запроса
    params = {
        "suggests[page]": 1,
        "suggests[per-page]": 5,
        "phrase": test_phrase,
        "include": "products,authors,bookCycles,publisherSeries,publishers,categories"
    }
    response = requests.get(API_URL, params=params)

    print(response.url)  # Выведет: https://example.com/search?q=python+requests&page=2
    print(response.status_code)
    print(response.text)



