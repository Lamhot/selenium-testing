import unittest
from selenium import webdriver

class PythonHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_home_page_in_python(self):
        driver = self.driver
        driver.get("https://modalku.co.id")
        self.assertIn("Investasi Menguntungkan dan Pinjaman Modal Usaha Kecil", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()