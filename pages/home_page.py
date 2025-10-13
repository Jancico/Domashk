# pages/home_page.py
from selenium.webdriver.common.by import By
from core import BasePage, Locator

# здесь храним локаторы и «атомарные» действия.
# Каждый шаг — это простая функция, которую легко вставить в тест.

# Примерные локаторы для демонстрации (поменяешь на свои):
SEARCH_INPUT: Locator = (By.XPATH, "input[name='q']")         # поле поиска
SEARCH_BUTTON: Locator = (By.CSS_SELECTOR, "button[type='submit']")  # кнопка поиска
TITLE: Locator = (By.TAG_NAME, "h1")                                  # заголовок на странице

def open_home(page: BasePage):
    """Открыть главную страницу сайта."""
    page.open("/")  # относительный путь — приклеится к base_url

def type_in_search(page: BasePage, text: str):
    """Ввести текст в поле поиска."""
    page.type(SEARCH_INPUT, text)

def submit_search(page: BasePage):
    """Нажать кнопку поиска."""
    page.click(SEARCH_BUTTON)

def should_see_title_contains(page: BasePage, expected: str):
    """Проверить, что заголовок содержит ожидаемый текст."""
    got = page.text(TITLE)
    assert expected.lower() in got.lower(), f"Ожидали в заголовке '{expected}', а получили '{got}'"
