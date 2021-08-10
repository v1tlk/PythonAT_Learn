from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import math

link = "http://suninjuly.github.io/alert_accept.html"  # Адрес тестового говна

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
    browser.find_element_by_xpath('//*[@type="submit"]').click()
    alert = browser.switch_to_alert()
    alert.accept()
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    result = calc(x_element.text)
    keys = browser.find_element_by_xpath('//*[@id="answer"]')
    keys.send_keys(result)
    browser.find_element_by_xpath('/html/body/form/div/div/button').click()
finally:
    time.sleep(10)
    browser.quit()