
from selenium.webdriver.common.by import By
from core import BasePage, Locator
from selenium.webdriver.support.ui import Select
import time




# Короткий расчёт
CALC_AMOUNT_INPUT: Locator = (By.XPATH, "//*[@id='credit-data-form']//input[@type='text' or @type='number'][1]")  # поле 'Желаемая сумма кредита'
CALC_DOWNPAYMENT_INPUT: Locator = (By.XPATH, "//*[@id='credit-data-form']/div/form/div/div[2]/input")  # поле 'Первоначальный взнос'
CALC_TERM_INPUT: Locator = (By.XPATH, "//*[@id='credit-data-form']/div/form/div/div[3]/input")  # поле 'Срок кредита'
CALCULATE_BUTTON: Locator = (By.XPATH, "//*[@id='credit-data-form']//button[.//text()[contains(.,'РАССЧИТАТЬ')]]")  # кнопка РАССЧИТАТЬ  :contentReference[oaicite:0]{index=0}

# Краткий результат
SHORT_RESULT_SECTION: Locator = (By.XPATH, "//*[@id='credit-short-result-form' or //*[contains(.,'Результат рассчета')]]")  # секция результата
SHORT_MONTHLY_PAYMENT_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Ежемесячный платеж')]/following::*[self::div or self::span][1]")  # значение ежемес. платежа
ADVANCED_CALCULATE_BUTTON: Locator = (By.XPATH, "//*[@id='credit-short-result-form']//a | //a[.//text()[contains(.,'заполните анкету')]]")  # кнопка 'заполните анкету'  :contentReference[oaicite:1]{index=1}
SHORT_NOTE_FILL_FORM: Locator = (By.XPATH, "//*[contains(.,'Расчет является примерным') and contains(.,'заполните анкету')]")  # примечание

# Данные заемщика
BORROWER_FORM: Locator = (By.XPATH, "//*[@id='credit-digital-form' or //*[contains(.,'Данные заемщика')]]")  

# ФИО
LAST_NAME_INPUT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Фамилия')]/following::input[1]")
FIRST_NAME_INPUT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Имя')]/following::input[1]")
MIDDLE_NAME_INPUT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Отчество')]/following::input[1]")

# Паспорт
PASSPORT_NUMBER_INPUT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Серия и номер паспорта')]/following::input[1]")
PASSPORT_ISSUED_BY_INPUT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Кем выдан')]/following::input[1]")
PASSPORT_ISSUE_DATE: Locator = (By.XPATH, "//*[@name='issued-date']")


# Образование
EDUCATION_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Образование')]/following::select[1]")
EDUCATION_OPTION_VYSSHEE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Образование')]/following::select[1]/option[contains(.,'Высшее')]")

# Стаж, работа
WORK_EXPERIENCE_TOTAL_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Общий трудовой стаж')]/following::select[1]")
WORK_EXPERIENCE_LASTJOB_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Срок работы на последнем месте')]/following::select[1]")
INCOME_DOC_2NDFL_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'2НДФЛ')]/following::select[1]")
WORK_REGION_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Место работы в регионе')]/following::select[1]")

# Доход
NET_INCOME_INPUT: Locator = (By.XPATH, "//*[@id='credit-data-user-form']/div[2]/form/div[8]/div[2]/input")

# Регистрация/судимость/имущество
REGISTRATION_REGION_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Место прописки в регионе')]/following::select[1]")
CRIMINAL_RECORD_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'судимость')]/following::select[1]")
HAS_CAR_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'в собственности автомобиль')]/following::select[1]")
HAS_PROPERTY_SELECT: Locator = (By.XPATH, "//*[contains(normalize-space(),'недвижимость')]/following::select[1]")

# Итог расчёта 
DIGITAL_RESULT_SECTION: Locator = (By.XPATH, "//*[@id=\"credit-message\"]")
RATE_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Процентная ставка')]/following::*[self::div or self::span][1]")
MONTHLY_PAYMENT_VALUE: Locator = (By.XPATH, "//*[@id='credit-monthly-payment-full']")
OVERPAYMENT_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Переплата по кредиту')]/following::*[self::div or self::span][1]")
TOTAL_PAYMENT_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Выплаты за весь срок кредита')]/following::*[self::div or self::span][1]")  # :contentReference[oaicite:2]{index=2}



def Open_base_page(page: BasePage):
    """Открыть главную страницу сайта."""
    page.open("/")  # относительный путь от base_url

    """нажать РАССЧИТАТЬ."""
def click_CALCULATE_BUTTON(page: BasePage): 
    page.click(CALCULATE_BUTTON) 


    """ нажать заполните анкету."""
def click_ADVANCED_CALCULATE_BUTTON(page: BasePage): 
    page.click(ADVANCED_CALCULATE_BUTTON) 


    """Упрощенный калькулятор"""
def Input_Simple_calculator (
    page: BasePage, 
    Amount:      int = 100000, 
    Downpaymant: int = 0, 
    Term:        int = 12): 

    page.type(CALC_AMOUNT_INPUT, Amount)
    page.type(CALC_DOWNPAYMENT_INPUT, Downpaymant)
    page.type(CALC_TERM_INPUT, Term)


    """Поля имени фамилии и отчества"""
def Input_Name(
    page: BasePage, 
    First_name:  str = "Злата", 
    Last_name:   str = "Ярцова", 
    Middle_name: str = "Васильевна"):

    page.type(FIRST_NAME_INPUT, First_name)
    page.type(LAST_NAME_INPUT, Last_name)
    page.type(MIDDLE_NAME_INPUT, Middle_name)


    """Данные поспорта"""
def Input_Pasport_info(
    page: BasePage, 
    Passport_number: str = "4300 542277", 
    Issued_by:       str = "Нижегородское ГОВД", 
    Issued_date:     str = "11.11.2011"):

    page.type(PASSPORT_NUMBER_INPUT, Passport_number)
    page.type(PASSPORT_ISSUED_BY_INPUT, Issued_by)
    page.type(PASSPORT_ISSUE_DATE, Issued_date)


    """Образование и работа клиента"""
def Input_Work_edukation(
    page: BasePage, 
    Education:  int | str = 1, 
    Work_total: int | str = 3, 
    Last_job:   int | str = 4, 
    NDFL:       int | str = 1, 
    Region:     int | str = 1, 
    Income:     int | str = 35000):
    
    Education  = str(Education)
    Work_total = str(Work_total)
    Last_job   = str(Last_job)
    NDFL       = str(NDFL)
    Region     = str(Region)
    Income     = str(Income)
    
    # выбор по атрибуту value, выпадаюший список нумеруется с единицы
    Select(page.visible(EDUCATION_SELECT)).select_by_value(Education)   
    Select(page.visible(WORK_EXPERIENCE_TOTAL_SELECT)).select_by_value(Work_total)   
    Select(page.visible(WORK_EXPERIENCE_LASTJOB_SELECT)).select_by_value(Last_job) 
    Select(page.visible(INCOME_DOC_2NDFL_SELECT)).select_by_value(NDFL) 
    Select(page.visible(WORK_REGION_SELECT)).select_by_value(Region)
    page.visible(NET_INCOME_INPUT)
    page.type(NET_INCOME_INPUT, Income)
    

    """Прочая информация"""
def Input_Other_information(
    page: BasePage, 
    Registration_region: int | str = 1, 
    Criminal:            int | str = 3, 
    Has_car:             int | str = 1, 
    Has_property:        int | str = 1):

    Registration_region  = str(Registration_region)
    Criminal             = str(Criminal)
    Has_car              = str(Has_car)
    Has_property         = str(Has_property)

    Select(page.visible(REGISTRATION_REGION_SELECT)).select_by_value(Registration_region) 
    Select(page.visible(CRIMINAL_RECORD_SELECT)).select_by_value(Criminal) 
    Select(page.visible(HAS_CAR_SELECT)).select_by_value(Has_car) 
    Select(page.visible(HAS_PROPERTY_SELECT)).select_by_value(Has_property) 

    """Тест результата"""  
def expect_equal(page: BasePage, locator: Locator, expected: str, label: str):
    actual = page.text(locator).strip()
    exp = str(expected).strip()
    assert actual == exp, f"{label}: ожидали '{exp}', получили '{actual}'"

def Resoult_check(
    page:BasePage, 
    expected_decidion: str,
    expected_rate: str,
    expected_mounthly: str,
    expected_overpaymant: str,
    expected_total: str):
    
    checks = [
    ("Решение", DIGITAL_RESULT_SECTION, expected_decidion),
    ("Ставка", RATE_VALUE, expected_rate),
    ("Ежемес. платёж", MONTHLY_PAYMENT_VALUE, expected_mounthly),
    ("Переплата", OVERPAYMENT_VALUE, expected_overpaymant),
    ("Итого", TOTAL_PAYMENT_VALUE, expected_total),
    ]

    
    for label, loc, expected in checks:
        expect_equal(page, loc, expected, label)

    print("[calc] Всё ОК — все значения совпали.")


    



