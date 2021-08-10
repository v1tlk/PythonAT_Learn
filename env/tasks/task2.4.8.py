from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

link = "http://suninjuly.github.io/explicit_wait2.html"  # Адрес тестового говна

chrome_cfg = Options()
chrome_cfg.add_argument('--no-sandbox')  # Bypass OS security model
chrome_cfg.add_argument('--disable-gpu')  # applicable to windows os only
chrome_cfg.add_argument('start-maximized')
browser = webdriver.Chrome(
    chrome_options=chrome_cfg, executable_path=r'C:\chromedriver\chromedriver.exe')
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    browser.find_element_by_id('book').click()
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    result = calc(x_element.text)
    keys = browser.find_element_by_xpath('//*[@id="answer"]')
    keys.send_keys(result)
    browser.find_element_by_id('solve').click()
finally:
    time.sleep(5)
    browser.quit()