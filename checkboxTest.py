from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time


class CkeckboxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        self.driver.get("http://blog.csssr.ru/qa-engineer/")

        continue_link = self.driver.find_element_by_link_text('НАХОДИТЬ НЕСОВЕРШЕНСТВА')
        continue_link.click()
        time.sleep(3)
        checkbox = self.driver.find_element_by_id("beautiful")
        state = checkbox.get_property("checked")
        label = self.driver.find_element_by_xpath("//label[@for='beautiful']")

        label.click()
        label.click()

        updated_state = checkbox.get_property("checked")
        assert updated_state == state, "checkbox wasn't returned to origin state after double click"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
