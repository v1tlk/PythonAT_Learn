from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import math

link = "http://suninjuly.github.io/math.html"  # Адрес тестового говна

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
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    calc_res = browser.find_element_by_xpath('//*[@id="answer"]')
    calc_res.send_keys(y)
    checkbox = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    checkbox.click()
    ra = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    ra.click()
    btn = browser.find_element_by_xpath('//div/form/button')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()