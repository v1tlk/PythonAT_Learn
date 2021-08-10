import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_cfg = Options()
chrome_cfg.add_argument('--no-sandbox')  # Bypass OS security model
chrome_cfg.add_argument('--disable-gpu')  # applicable to windows os only
chrome_cfg.add_argument('start-maximized')
browser = webdriver.Chrome(
    chrome_options=chrome_cfg, executable_path=r'C:\chromedriver\chromedriver.exe')

class TestAbs(unittest.TestCase):

    def test1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group first_class"]/input')
        input1.send_keys("Vitaly")
        input2 = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group second_class"]/input')
        input2.send_keys("Nepochatyh")
        input3 = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group third_class"]/input')
        input3.send_keys("leedno@gmail.com")
        input4 = browser.find_element_by_xpath('//div[@class="second_block"]/div[@class="form-group first_class"]/input')
        input4.send_keys("89099099090")
        input5 = browser.find_element_by_xpath('//div[@class="second_block"]/div[@class="form-group second_class"]/input')
        input5.send_keys("ul.Pushkina d.Kolotushkina")
            # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" , welcome_text)

    def test2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group first_class"]/input')
        input1.send_keys("Vitaly")
        input2 = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group second_class"]/input')
        input2.send_keys("Nepochatyh")
        input3 = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group third_class"]/input')
        input3.send_keys("leedno@gmail.com")
        input4 = browser.find_element_by_xpath('//div[@class="second_block"]/div[@class="form-group first_class"]/input')
        input4.send_keys("89099099090")
        input5 = browser.find_element_by_xpath('//div[@class="second_block"]/div[@class="form-group second_class"]/input')
        input5.send_keys("ul.Pushkina d.Kolotushkina")
            # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" , welcome_text)

if __name__ == "__main__":
    unittest.main()