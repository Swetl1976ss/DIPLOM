class Settings:
    """Конфигурация тестового окружения"""

    # Базовые URL
    BASE_URL = "https://www.chitai-gorod.ru"
    API_URL = "https://api.chitai-gorod.ru/v1"

    # Таймауты
    UI_TIMEOUT = 10
    API_TIMEOUT = 5

    # Настройки браузера
    BROWSER = "chrome"
    HEADLESS = False
    WINDOW_SIZE = "1920x1080"

    # Пути
    ALLURE_RESULTS = "allure-results"
    SCREENSHOTS = "screenshots"


settings = Settings()