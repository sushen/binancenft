from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

args = ["hide_console"]
driver = webdriver.Chrome("../Driver/chromedriver.exe", service_args=args)

driver.get("https://www.binance.com/en/nft/goods/detail?productId=23684237&isProduct=1")

# allow_button = driver.find_element(By.XPATH, "//button[@class=' css-lolz04']").is_displayed()

element2 = driver.find_element_by_xpath("//button[contains(text(),'Buy Now')]").is_displayed()
print(element2)
allow_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Buy Now')]"))).is_displayed()
print(allow_button)
element = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(text(),'have enough crypto')]"))).is_enable()
print(element)

