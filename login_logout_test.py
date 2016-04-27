import unittest
from selenium import webdriver

class PythonLoginForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_logout_form_in_python(self):
        driver = self.driver
        driver.get("https://modalku.co.id/membership/login")
        element = driver.find_element_by_id("ContentPlaceHolder1_botemail")
        element.send_keys("lamhotjmsiagian94@gmail.com")
        element = driver.find_element_by_id("ContentPlaceHolder1_botpw")
        element.send_keys("QA@2016lamhot")
        content = driver.find_element_by_css_selector('div.form-input > img')
        content.click()
        assert "Lamhot JM Siagian" in driver.page_source
        element = driver.find_element_by_link_text('LOGOUT')
        element.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
