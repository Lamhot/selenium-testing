from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://modalku.co.id")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("Investasi Menguntungkan dan Pinjaman Modal Usaha Kecil")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
