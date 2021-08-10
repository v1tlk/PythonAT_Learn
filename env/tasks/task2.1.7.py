from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import math

link = "http://suninjuly.github.io/selects1.html"  # Адрес тестового говна

chrome_cfg = Options()
chrome_cfg.add_argument('--no-sandbox')  # Bypass OS security model
chrome_cfg.add_argument('--disable-gpu')  # applicable to windows os only
chrome_cfg.add_argument('start-maximized')
browser = webdriver.Chrome(
    chrome_options=chrome_cfg, executable_path=r'C:\chromedriver\chromedriver.exe')
browser.get(link)

try: 
    x_element = browser.find_element_by_xpath('//*[@id="num1"]')
    y_element = browser.find_element_by_xpath('//*[@id="num2"]')
    calcul = str(int(x_element.text) + int(y_element.text))
    res = browser.find_element_by_xpath('//*[@id="dropdown"]/option[@value=' + calcul + ']').click()
    browser.find_element_by_xpath("//div/form/button").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()