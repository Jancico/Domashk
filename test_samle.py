# test_sample.py
import pytest
from core import make_driver, Config, BasePage
from pages import home_page as Home

@pytest.fixture
def driver():
    d = make_driver(headless=False)   # можно True для запуска без окна
    yield d
    d.quit()

@pytest.fixture
def page(driver):
    cfg = Config(
        base_url=Config.base_url,  # поменяй на свой тестовый сайт
        timeout=10
    )
    return BasePage(driver, cfg)

def test_basic_flow(page):
    Home.test_01(page)
