# core.py
from dataclasses import dataclass
from typing import Optional, Tuple
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ----------------------------
# Конфиг: тут укажем базовый URL
# ----------------------------
@dataclass
class Config:
    base_url: str = "https://creditcalculator.pointschool.ru/credit"  # поменяешь на адрес своего сайта
    timeout: int = 10                       # сек. ожидания элементов


# -----------------------------------------------------
# Фабрика драйвера: поднимаем Chrome с автозагрузкой драйвера
# -----------------------------------------------------
def make_driver(headless: bool = False) -> WebDriver:
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


# -----------------------------------------------------
# База: удобные методы с явными ожиданиями
# -----------------------------------------------------
Locator = Tuple[str, str]  # например: (By.CSS_SELECTOR, "input[name='q']")

class BasePage:
    """Базовая страница для Page Object: хранит драйвер, ожидания и конфиг."""

    def __init__(self, driver: WebDriver, cfg: Config):
        # Сохраняем драйвер и конфиг, настраиваем явные ожидания
        self.driver = driver
        self.wait = WebDriverWait(driver, cfg.timeout)
        self.cfg = cfg

    def open(self, path: str = "/"):
        """Открыть страницу: абсолютный URL или относительный к base_url."""
        # Если путь — полный URL, едем прямо по нему
        if path.startswith("http"):
            self.driver.get(path)
        else:
            # Иначе собираем URL из base_url и относительного пути
            self.driver.get(self.cfg.base_url.rstrip("/") + "/" + path.lstrip("/"))

    def find(self, locator: Locator):
        """Дождаться присутствия элемента в DOM и вернуть его (может быть невидим)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible(self, locator: Locator):
        """Дождаться видимости элемента и вернуть его."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: Locator):
        """Дождаться кликабельности элемента и кликнуть по нему."""
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def type(self, locator: Locator, text: str, clear: bool = True):
        """Ввести текст в видимый элемент; по умолчанию предварительно очистить поле."""
        el = self.visible(locator)
        el.click()
        
        if clear:
            el.clear()  # Очистка инпута перед вводом
        el.send_keys(text)

    def text(self, locator: Locator) -> str:
        """Получить видимый текст элемента."""
        return self.visible(locator).text

    def exists(self, locator: Locator) -> bool:
        """Проверить, что элемент присутствует в DOM (без падения теста)."""
        try:
            self.find(locator)
            return True
        except Exception:
            return False

    def url_contains(self, fragment: str):
        """Дождаться, что текущий URL содержит заданный фрагмент."""
        self.wait.until(EC.url_contains(fragment))

