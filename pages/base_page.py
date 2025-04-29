from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import settings
import allure
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы для работы с веб-элементами.
    """

    def __init__(self, browser, url=""):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, settings.DEFAULT_TIMEOUT)

    @allure.step("Открытие страницы {url}")
    def open(self):
        """Открыть страницу с заданным URL"""
        self.browser.get(self.url)
        logger.info(f"Открыта страница: {self.url}")

    @allure.step("Проверка видимости элемента {locator}")
    def is_visible(self, locator, timeout=None):
        """Ожидание видимости элемента"""
        wait = self.wait if timeout is None else WebDriverWait(self.browser, timeout)
        try:
            element = wait.until(EC.visibility_of_element_located(locator))
            logger.debug(f"Элемент {locator} виден на странице")
            return element
        except TimeoutException:
            logger.error(f"Элемент {locator} не стал видимым за {timeout or settings.DEFAULT_TIMEOUT} сек")
            raise

    @allure.step("Проверка кликабельности элемента {locator}")
    def is_clickable(self, locator, timeout=None):
        """Ожидание кликабельности элемента"""
        wait = self.wait if timeout is None else WebDriverWait(self.browser, timeout)
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            logger.debug(f"Элемент {locator} кликабелен")
            return element
        except TimeoutException:
            logger.error(f"Элемент {locator} не стал кликабельным за {timeout or settings.DEFAULT_TIMEOUT} сек")
            raise

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        """Клик по элементу с ожиданием его кликабельности"""
        element = self.is_clickable(locator)
        element.click()
        logger.info(f"Клик по элементу: {locator}")

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def type(self, locator, text):
        """Ввод текста в поле с очисткой предыдущего значения"""
        element = self.is_visible(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"Введен текст '{text}' в элемент {locator}")

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        """Получение текста элемента"""
        element = self.is_visible(locator)
        text = element.text
        logger.debug(f"Получен текст '{text}' из элемента {locator}")
        return text

    @allure.step("Проверка наличия текста '{text}' на странице")
    def text_present(self, text):
        """Проверка наличия текста на странице"""
        try:
            return text in self.browser.page_source
        except Exception as e:
            logger.error(f"Ошибка при проверке текста: {e}")
            return False

    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот и прикрепить к Allure отчету"""
        allure.attach(
            self.browser.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
        logger.info(f"Сделан скриншот: {name}")