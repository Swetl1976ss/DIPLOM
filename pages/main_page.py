from selenium.webdriver.common.by import By
from .base_page import BasePage
from config.settings import settings
import allure


class MainPage(BasePage):
    """
    Класс для работы с главной страницей 'Читай-город'.
    Наследует базовые методы от BasePage.
    """

    URL = settings.BASE_URL

    # Локаторы элементов
    LOGO = (By.CSS_SELECTOR, "header .logo")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-btn")
    CART_ICON = (By.CSS_SELECTOR, ".header-cart")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".header__login")
    MAIN_MENU = (By.CSS_SELECTOR, "nav.main-menu")
    MENU_LINKS = (By.CSS_SELECTOR, "nav.main-menu a")
    PROMO_BANNERS = (By.CSS_SELECTOR, ".promo-slider")
    NEW_ARRIVALS = (By.CSS_SELECTOR, ".new-arrivals")

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    @allure.step("Поиск книги по запросу '{query}'")
    def search_book(self, query):
        """Поиск книги на сайте"""
        self.type(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """Переход в корзину"""
        self.click(self.CART_ICON)
        from pages.cart_page import CartPage  # Импорт здесь чтобы избежать циклического импорта
        return CartPage(self.browser)

    @allure.step("Переход на страницу авторизации")
    def go_to_login(self):
        """Переход на страницу авторизации"""
        self.click(self.LOGIN_BUTTON)
        from pages.auth_page import AuthPage
        return AuthPage(self.browser)

    @allure.step("Переход в раздел '{section_name}'")
    def go_to_section(self, section_name):
        """Навигация по разделам сайта"""
        link_locator = (By.LINK_TEXT, section_name)
        self.click(link_locator)

    @allure.step("Проверка отображения промо-баннеров")
    def check_promo_banners(self):
        """Проверка видимости промо-баннеров"""
        return self.is_visible(self.PROMO_BANNERS)

    @allure.step("Проверка отображения новинок")
    def check_new_arrivals(self):
        """Проверка видимости блока новинок"""
        return self.is_visible(self.NEW_ARRIVALS)

    @allure.step("Получение количества элементов в меню")
    def get_menu_items_count(self):
        """Получение количества пунктов в главном меню"""
        return len(self.browser.find_elements(*self.MENU_LINKS))