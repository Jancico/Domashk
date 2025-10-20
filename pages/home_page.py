# pages/home_page.py
from selenium.webdriver.common.by import By
from core import BasePage, Locator
from selenium.webdriver.support.ui import Select
import time


# здесь храним локаторы и «атомарные» действия.
# Каждый шаг — это простая функция, которую легко вставить в тест.

# Примерные локаторы для демонстрации (поменяешь на свои):
SEARCH_INPUT: Locator = (By.XPATH, "input[name='q']")         # поле поиска
SEARCH_BUTTON: Locator = (By.CSS_SELECTOR, "button[type='submit']")  # кнопка поиска
TITLE: Locator = (By.TAG_NAME, "h1")                                  # заголовок на странице
CALCULATE_BUTTON: Locator = (By.XPATH, "//*[@id='credit-data-form']/div/form/div/div[4]/button") # кнопка РАСЧИТАТЬ
ADVANCED_CALCULATE_BUTTON: Locator = (By.XPATH, "//*[@id='credit-short-result-form']/div[2]/div[2]/a")# кнопка заполните анкету

# ===== Короткий расчёт (верхняя форма) =====
CALC_AMOUNT_INPUT: Locator = (By.XPATH, "//*[@id='credit-data-form']//input[@type='text' or @type='number'][1]")  # поле 'Желаемая сумма кредита'
CALC_DOWNPAYMENT_INPUT: Locator = (By.XPATH, "//*[@id='credit-data-form']/div/form/div/div[2]/input")  # поле 'Первоначальный взнос'
CALC_TERM_INPUT: Locator = (By.XPATH, "//*[@id='credit-data-form']/div/form/div/div[3]/input")  # поле 'Срок кредита'
CALCULATE_BUTTON: Locator = (By.XPATH, "//*[@id='credit-data-form']//button[.//text()[contains(.,'РАССЧИТАТЬ')]]")  # кнопка РАССЧИТАТЬ  :contentReference[oaicite:0]{index=0}

# ===== Краткий результат =====
SHORT_RESULT_SECTION: Locator = (By.XPATH, "//*[@id='credit-short-result-form' or //*[contains(.,'Результат рассчета')]]")  # секция результата
SHORT_MONTHLY_PAYMENT_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Ежемесячный платеж')]/following::*[self::div or self::span][1]")  # значение ежемес. платежа
ADVANCED_CALCULATE_BUTTON: Locator = (By.XPATH, "//*[@id='credit-short-result-form']//a | //a[.//text()[contains(.,'заполните анкету')]]")  # кнопка 'заполните анкету'  :contentReference[oaicite:1]{index=1}
SHORT_NOTE_FILL_FORM: Locator = (By.XPATH, "//*[contains(.,'Расчет является примерным') and contains(.,'заполните анкету')]")  # примечание

# ===== Расширенная анкета (Данные заемщика) =====
BORROWER_FORM: Locator = (By.XPATH, "//*[@id='credit-digital-form' or //*[contains(.,'Данные заемщика')]]")  # контейнер анкеты

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

# ===== Итог расчёта (в анкете) =====
DIGITAL_RESULT_SECTION: Locator = (By.XPATH, "//*[contains(.,'Результат расчета')][1]/ancestor::*[self::section or self::div][1]")
RATE_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Процентная ставка')]/following::*[self::div or self::span][1]")
MONTHLY_PAYMENT_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Ежемесячный платеж')]/following::*[self::div or self::span][1]")
OVERPAYMENT_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Переплата по кредиту')]/following::*[self::div or self::span][1]")
TOTAL_PAYMENT_VALUE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Выплаты за весь срок кредита')]/following::*[self::div or self::span][1]")  # :contentReference[oaicite:2]{index=2}

# ===== Действия (кнопки) =====
SUBMIT_APPLICATION_BUTTON: Locator = (By.XPATH, "//button[.//text()[contains(.,'ОТПРАВИТЬ ЗАЯВКУ')]]")
SEND_TO_EMAIL_BUTTON: Locator = (By.XPATH, "//button[.//text()[contains(.,'ОТПРАВИТЬ РАСЧЕТ НА EMAIL')]]")
BACK_TO_SHORT_RESULT_LINK: Locator = (By.XPATH, "//a[.//text()[contains(.,'ВЕРНУТЬСЯ К КРАТКОМУ РАСЧЕТУ')]]")  # :contentReference[oaicite:3]{index=3}

# ===== Диалог «Обработка запроса» =====
PROCESSING_MODAL: Locator = (By.XPATH, "//*[contains(normalize-space(),'Обработка запроса')]/ancestor::*[contains(@class,'modal')][1]")
PROCESSING_CLOSE: Locator = (By.XPATH, "//*[contains(normalize-space(),'Обработка запроса')]/following::button[normalize-space()='×'][1]")
PROCESSING_TEXT: Locator = (By.XPATH, "//*[contains(normalize-space(),'Ваш запрос обрабатывается')]")
PROCESSING_CANCEL_BUTTON: Locator = (By.XPATH, "//button[.//text()[contains(.,'Отмена')]]")  # :contentReference[oaicite:4]{index=4}

# ===== Шапка/навигация/партнёры =====
LOGIN_LINK: Locator = (By.XPATH, "//a[normalize-space()='Вход для сотрудников']")
NAV_LOGO: Locator = (By.XPATH, "//img[contains(@src,'creditcalculator')]")
PARTNERS_BLOCK: Locator = (By.XPATH, "//*[contains(normalize-space(),'Наши парт')]/following::*[self::ul or self::div][1]")
PARTNER_LINKS: Locator = (By.XPATH, "//*[contains(normalize-space(),'Наши парт')]/following::*[self::ul or self::div][1]//a")  # список ссылок партнёров  :contentReference[oaicite:5]{index=5}

# ===== Поля email (если открывается форма отправки расчёта) — предполагаемая разметка =====
EMAIL_INPUT: Locator = (By.XPATH, "//input[@type='email' or @name='email' or @placeholder[contains(.,'email')]]")
EMAIL_SEND_BUTTON: Locator = (By.XPATH, "//button[.//text()[contains(.,'Отправить')]]")


def Open_base_page(page: BasePage):
    """Открыть главную страницу сайта."""
    page.open("/")  # относительный путь — приклеится к base_url

    """нажать РАССЧИТАТЬ."""
def click_CALCULATE_BUTTON(page: BasePage): 
    page.click(CALCULATE_BUTTON) 


    """ нажать заполните анкету."""
def click_ADVANCED_CALCULATE_BUTTON(page: BasePage): 
    page.click(ADVANCED_CALCULATE_BUTTON) 


    """Упрощенный калькулятор"""
def Simple_calculator_input (
    page: BasePage, 
    Amount:      int = 100000, 
    Downpaymant: int = 0, 
    Term:        int = 12): 

    page.type(CALC_AMOUNT_INPUT, Amount)
    page.type(CALC_DOWNPAYMENT_INPUT, Downpaymant)
    page.type(CALC_TERM_INPUT, Term)


    """Поля имени фамилии и отчества"""
def Name_input(
    page: BasePage, 
    First_name:  str = "Злата", 
    Last_name:   str = "Ярцова", 
    Middle_name: str = "Васильевна"):

    page.type(FIRST_NAME_INPUT, First_name)
    page.type(LAST_NAME_INPUT, Last_name)
    page.type(MIDDLE_NAME_INPUT, Middle_name)


    """Данные поспорта"""
def Pasport_info_input(
    page: BasePage, 
    Passport_number: str = "4300 542277", 
    Issued_by:       str = "Нижегородское ГОВД", 
    Issued_date:     str = "11.11.2011"):

    page.type(PASSPORT_NUMBER_INPUT, Passport_number)
    page.type(PASSPORT_ISSUED_BY_INPUT, Issued_by)
    page.type(PASSPORT_ISSUE_DATE, Issued_date)


    """Образование и работа клиента"""
def Work_edukation_input(
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
def Other_information(
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
    
    
