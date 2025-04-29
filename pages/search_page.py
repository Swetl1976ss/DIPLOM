from .base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-btn")
    RESULTS = (By.CSS_SELECTOR, ".product-card")
    ADD_TO_CART = (By.CSS_SELECTOR, ".buy-btn")

    def search(self, query):
        self.is_visible(self.SEARCH_INPUT).send_keys(query)
        self.is_visible(self.SEARCH_BUTTON).click()

    def get_results_count(self):
        return len(self.browser.find_elements(*self.RESULTS))

    def add_first_item_to_cart(self):
        self.is_visible(self.ADD_TO_CART).click()