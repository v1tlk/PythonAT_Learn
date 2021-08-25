import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

chrome_cfg = Options()
chrome_cfg.add_argument('--disable-gpu')  # applicable to windows os only
chrome_cfg.add_argument('start-maximized')

# Инициализация браузера и сборка мусора
@pytest.fixture
def browser():
    print("\nStart browser for case..")
    global browser
    browser = webdriver.Chrome(options=chrome_cfg, executable_path=r'C:\chromedriver\chromedriver.exe')
    yield browser
    print("\nExit browser for case..")
    browser.quit()

# Расчёт функции для получения ответа
@pytest.fixture
def answer():
    answer = math.log(int(time.time()))
    return answer

# Основной класс
class TestMainPage1():
    @pytest.mark.parametrize('link', [ #Список ссылок для проверки
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
        ])
    def test1(self, browser, answer, link):                                 #Сам кейс
        browser.implicitly_wait(10)
        browser.get(link)
        WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "ember-text-area")))
        browser.find_element_by_class_name('ember-text-area').send_keys(str(answer))
        WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
        browser.find_element_by_class_name('submit-submission').click()
        WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        assert (browser.find_element_by_class_name('smart-hints__hint').text == 'Correct!'), 'Тут что то не так'