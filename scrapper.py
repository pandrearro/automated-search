from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
search_box = driver.find_element_by_name("q")
search_box.clear()
search_box.send_keys("el heraldo")
search_box.send_keys(Keys.ENTER)
eh_link = driver.find_element_by_xpath(
    "//*[@id='rso']/div[1]/div/div/div[1]/a/h3")
eh_link.click()
locales_link = driver.find_element_by_link_text("LOCALES")
locales_link.click()
page_div = driver.find_element_by_id("page")
page_div.send_keys(Keys.PAGE_DOWN)
