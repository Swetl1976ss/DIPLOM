iimport pytest
import allure
from config.settings import settings
from config.test_data import test_data
from utilities.api_client import ApiClient

@allure.feature("API Тесты Читай-город")
class TestAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api = ApiClient(settings.API_URL)

    @allure.story("API Книги")
    @allure.title("Поиск книги через API")
    def test_search_books(self):
        response = self.api.search_books(test_data.BOOKS[0])
        assert response.status_code == 200
        assert len(response.json()["items"]) > 0

    @allure.story("API Авторизация")
    @allure.title("Успешная авторизация через API")
    def test_auth(self):
        response = self.api.login(test_data.VALID_USER)
        assert response.status_code == 200
        assert "token" in response.json()

    @allure.story("API Корзина")
    @allure.title("Добавление в корзину через API")
    def test_add_to_cart(self):
        # Предварительная авторизация
        auth = self.api.login(test_data.VALID_USER)
        book_id = self.api.search_books(test_data.BOOKS[1]).json()["items"][0]["id"]

        response = self.api.add_to_cart(book_id)
        assert response.status_code == 200

    @allure.story("API Профиль")
    @allure.title("Получение данных профиля")
    def test_user_profile(self):
        self.api.login(test_data.VALID_USER)
        response = self.api.get_user_profile()
        assert response.status_code == 200
        assert response.json()["email"] == test_data.VALID_USER["email"]

    @allure.story("API Каталог")
    @allure.title("Получение списка категорий")
    def test_categories(self):
        response = self.api.get_categories()
        assert response.status_code == 200
        assert len(response.json()["categories"]) > 5