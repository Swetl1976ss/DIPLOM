import pytest
import allure
import requests

API_URL = "https://web-gate.chitai-gorod.ru/api/v2/search"
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxODk4OTQ2LCJpYXQiOjE3NDU5MDExMjQsImV4cCI6MTc0NTkwNDcyNCwidHlwZSI6MjB9.dkW-pSrpVLO6c6qLO40WLsRQcl6ndiZrhdMDuNBiroE'
header = {
    'authorization': f'Bearer {token}',
'content-type': 'application/json'
}


@allure.story("API Книги")
@allure.title("Поиск книги по названию")
def test_search_book():
    response = requests.get(
        API_URL + '/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=Волшебник',
        headers=header)
    assert response.status_code == 200


@allure.story("API Книги")
@allure.title("Поиск книги по автору")
def test_search_book2():
    response = requests.get(
        API_URL + '/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=%D0%9F%D1%83%D1%88%D0%BA%D0%B8%D0%BD&include=products%2Cauthors%2CbookCycles%2CpublisherSeries%2Cpublishers%2Ccategories',
        headers=header)
    assert response.status_code == 200


@allure.story("API Книги")
@allure.title("Поиск книги по жанру")
def test_search_book3():
    response = requests.get(
        API_URL + '/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F&include=products%2Cauthors%2CbookCycles%2CpublisherSeries%2Cpublishers%2Ccategories',
        headers=header)
    assert response.status_code == 200


@allure.story("API Книги")
@allure.title("Поиск книги negative")
def test_search_book4():
    response = requests.get(
        API_URL + '/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=%E2%88%87%20%E2%84%B5%20%E2%84%91%20%E2%84%98%20%E2%84%9C&include=products%2Cauthors%2CbookCycles%2CpublisherSeries%2Cpublishers%2Ccategories',
        headers=header)
    assert response.status_code == 422


@allure.story("API Книги")
@allure.title("missing auth")
def test_search_book5():
    response = requests.get(
        API_URL + '/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=%E2%88%87%20%E2%84%B5%20%E2%84%91%20%E2%84%98%20%E2%84%9C&include=products%2Cauthors%2CbookCycles%2CpublisherSeries%2Cpublishers%2Ccategories')
    assert response.status_code == 403