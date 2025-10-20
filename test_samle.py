# test_sample.py
import pytest
import time
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

    page.open("/")

    Home.click_CALCULATE_BUTTON(page)
    Home.click_ADVANCED_CALCULATE_BUTTON(page)
    Home.Simple_calculator_input(page)
    Home.Name_input(page)
    Home.Pasport_info_input(page)
    Home.Work_edukation_input(page)
    Home.Other_information(page)
    Home.click_CALCULATE_BUTTON(page)

    time.sleep(30)
