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
    Home.Input_Simple_calculator(page)
    Home.Input_Name(page)
    Home.Input_Pasport_info(page)
    Home.Input_Work_edukation(page)
    Home.Input_Other_information(page)
    Home.click_CALCULATE_BUTTON(page)

    Home.Resoult_check(
    page,
    expected_decidion = "Кредит предварительно одобрен",
    expected_rate     = "28.61 %",   
    expected_mounthly = "16 165 Р",  
    expected_overpaymant = "9 680 Р",
    expected_total    = "116 165 Р",
)

    
