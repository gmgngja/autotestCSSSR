# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class CheckboxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        self.driver.get("http://blog.csssr.ru/qa-engineer/")

        continue_link = self.driver.find_element_by_link_text('СОПРОВОЖДАТЬ ПРОЕКТЫ')
        continue_link.click()
        time.sleep(3)

        checkbox = self.driver.find_element_by_id("attention2")
        state = checkbox.get_property("checked")
        label = self.driver.find_element_by_xpath("//label[@for='attention2']")

        label.click()
        updated_state = checkbox.get_property("checked")
        assert updated_state != state, "Checkbox did not change state"

        label.click()
        updated_state = checkbox.get_property("checked")
        assert updated_state == state, "Checkbox did not returned to origin after double click"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
