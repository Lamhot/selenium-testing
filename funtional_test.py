from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://modalku.co.id")
assert "Investasi Menguntungkan dan Pinjaman Modal Usaha Kecil" in driver.titlew
elem = driver.find_element_by_name("SIGN IN").click()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

