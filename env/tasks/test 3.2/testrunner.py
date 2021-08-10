import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_cfg = webdriver.ChromeOptions()
chrome_cfg.add_argument('--headless')
browser = webdriver.Chrome(
    executable_path=r'C:\chromedriver\chromedriver.exe', options=chrome_cfg)

class TestAbs(unittest.TestCase):

    def test1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group first_class"]/input').send_keys("Vitaly")
        browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group second_class"]/input').send_keys("Nepochatyh")
        browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group third_class"]/input').send_keys("leedno@gmail.com")
        browser.find_element_by_xpath('//div[@class="second_block"]/div[@class="form-group first_class"]/input').send_keys("89099099090")
        browser.find_element_by_xpath('//div[@class="second_block"]/div[@class="form-group second_class"]/input').send_keys("ul.Pushkina d.Kolotushkina")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt)

    def test2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group first_class"]/input').send_keys("Vitaly")
        browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group second_class"]/input').send_keys("Nepochatyh")
        browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group third_class"]/input').send_keys("leedno@gmail.com")
        browser.find_element_by_xpath('//div[@class="second_block"]/div[@class="form-group first_class"]/input').send_keys("89099099090")
        browser.find_element_by_xpath('//div[@class="second_block"]/div[@class="form-group second_class"]/input').send_keys("ul.Pushkina d.Kolotushkina")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt)

if __name__ == "__main__":
    unittest.main()
    browser.exit