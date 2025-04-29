# 🏙 Автоматизация тестирования сайта "Читай-город"

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.9.0-green)](https://selenium.dev)
[![Pytest](https://img.shields.io/badge/Pytest-7.4.0-yellow)](https://pytest.org)

Проект автоматизированного тестирования ключевой функциональности интернет-магазина "Читай-город".

## 🔍 Охваченная функциональность
- Авторизация пользователя
- Поиск книг и фильтрация результатов
- Работа с корзиной
- Оформление заказа
- Личный кабинет

## 🛠 Технологии
| Компонент       | Технология       |
|----------------|------------------|
| UI-тесты       | Selenium 4 + Pytest |
| API-тесты      | Requests + Pytest   |
| Отчетность     | Allure Framework  |
| Управление браузером | WebDriver Manager |

## 🚀 Запуск тестов

### Предварительные требования
1. Установите [Python 3.9+](https://www.python.org/downloads/)
2. Установите зависимости:
```bash
pip install -r requirements.txt
Команды для запуска
bash
# Запуск всех тестов с генерацией отчета
pytest tests/ --alluredir=allure-results -v

# Запуск UI-тестов (проверка фронтенда)
pytest tests/test_ui.py -m ui

# Запуск API-тестов (проверка бэкенда)
pytest tests/test_api.py -m api

# Параллельный запуск (4 потока)
pytest -n 4 tests/
Просмотр отчета
bash
allure serve allure-results
📂 Структура проекта
text
chitai-gorod-autotests/
├── config/
│   ├── settings.py        # URL сайта, API endpoints
│   └── test_data.py       # Тестовые пользователи, книги
├── pages/
│   ├── auth_page.py       # Страница авторизации
│   ├── cart_page.py       # Корзина
│   └── search_page.py     # Поиск книг
├── tests/
│   ├── ui/
│   │   ├── test_auth.py   # Тесты авторизации
│   │   └── test_cart.py   # Тесты корзины
│   └── api/
│       ├── test_books.py  # API книг
│       └── test_orders.py # API заказов
└── utilities/            # Общие утилиты
🧪 Пример теста
UI-тест проверки поиска:

python
def test_search_popular_book():
    search_page = SearchPage(driver)
    search_page.search("Гарри Поттер")
    assert search_page.has_results()
    assert "Роулинг" in search_page.first_result_text()
API-тест корзины:

python
def test_add_to_cart(api_client):
    response = api_client.add_to_cart(
        product_id="12345", 
        quantity=1
    )
    assert response.status_code == 200
    assert response.json()["cart_items_count"] > 0
📊 Документация
Тест-кейсы в Qase.io

Postman-коллекция

Swagger API

⚠️ Известные проблемы
Периодические капчи при авторизации

Нестабильный API метода добавления в корзину

Долгая загрузка результатов поиска (>5 сек)

📌 Рекомендации
Для тестов используйте тестовый аккаунт

При частых запусках добавляйте задержки между запросами

Для UI-тестов используйте режим headless в CI

📧 Контакты
По вопросам сотрудничества: ваш.email@example.com


Ключевые особенности:
1. Специфичные для "Читай-города" разделы (известные проблемы, рекомендации)
2. Четкое разделение UI и API тестов
3. Примеры реальных тестов для книжного магазина
4. Информация о тестовых данных и окружении
5. Актуальные проблемы и обходные пути

Дополнительно можно добавить:
- Скриншоты из Allure-отчетов
- Видео прохождения тестов
- Графики стабильности тестов
- Инструкцию по тестовым данным