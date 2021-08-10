from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import os

link = "http://suninjuly.github.io/file_input.html"  # Адрес тестового говна

chrome_cfg = Options()
chrome_cfg.add_argument('--no-sandbox')  # Bypass OS security model
chrome_cfg.add_argument('--disable-gpu')  # applicable to windows os only
chrome_cfg.add_argument('start-maximized')
browser = webdriver.Chrome(
    chrome_options=chrome_cfg, executable_path=r'C:\chromedriver\chromedriver.exe')
browser.get(link)

try: 
    fname = browser.find_element_by_xpath('//*[@name="firstname"]')
    fname.send_keys("Vitaliy")
    lname = browser.find_element_by_xpath('//*[@name="lastname"]')
    lname.send_keys("Test")
    email = browser.find_element_by_xpath('//*[@name="email"]')
    email.send_keys("test@test.com")
    upload_button = browser.find_element_by_xpath('//*[@id="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')   
    upload_button.send_keys(file_path)
    fin = browser.find_element_by_xpath("/html/body/div/form/button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()