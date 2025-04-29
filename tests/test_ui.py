import pytest
import allure
from config.settings import settings
from config.test_data import test_data
from pages.main_page import MainPage
from pages.auth_page import AuthPage


@allure.feature("UI Тесты Читай-город")
class TestUI:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.main_page.open()

    @allure.story("Основная функциональность")
    @allure.title("Проверка загрузки главной страницы")
    def test_main_page_load(self):
        assert "Читай-город" in self.main_page.get_title()
        assert self.main_page.is_logo_visible()

    @allure.story("Поиск")
    @allure.title("Поиск книги по названию")
    def test_book_search(self):
        search_page = self.main_page.search_book(test_data.BOOKS[0])
        assert search_page.has_results()

    @allure.story("Авторизация")
    @allure.title("Успешная авторизация")
    def test_successful_login(self):
        auth_page = self.main_page.go_to_login()
        auth_page.login(test_data.VALID_USER)
        assert auth_page.is_user_logged_in()

    @allure.story("Корзина")
    @allure.title("Добавление товара в корзину")
    def test_add_to_cart(self):
        search_page = self.main_page.search_book(test_data.BOOKS[1])
        search_page.add_first_to_cart()
        assert search_page.get_cart_count() == 1

    @allure.story("Навигация")
    @allure.title("Проверка меню навигации")
    def test_navigation_menu(self):
        sections = ["Книги", "Авторы", "Акции"]
        for section in sections:
            self.main_page.go_to_section(section)
            assert section in self.main_page.get_title()