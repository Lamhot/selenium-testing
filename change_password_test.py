import unittest
from selenium import webdriver

class PythonLoginForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_change_password_form_in_python(self):
        driver = self.driver
        driver.get("https://modalku.co.id/membership/login")
        element = driver.find_element_by_id("ContentPlaceHolder1_botemail")
        element.send_keys("lamhotjmsiagian94@gmail.com")
        element = driver.find_element_by_id("ContentPlaceHolder1_botpw")
        element.send_keys("QA@2016nolamhot")
        content = driver.find_element_by_css_selector('div.form-input > img')
        content.click()
        element = driver.find_element_by_link_text('PENGATURAN')
        element.click()
        element = driver.find_element_by_id("ContentPlaceHolder1_OldPass")
        element.send_keys("QA@2016nolamhot")
        element = driver.find_element_by_id("ContentPlaceHolder1_NewPass")
        element.send_keys("QA@2016lamhot")
        element = driver.find_element_by_id("ContentPlaceHolder1_ConfirmPass")
        element.send_keys("QA@2016lamhot")
        element = driver.find_element_by_id("cp")
        element.click()

if __name__ == "__main__":
    unittest.main()
