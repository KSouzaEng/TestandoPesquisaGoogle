from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import  sleep


driver = webdriver.Firefox()
driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element_by_name("q")
sleep(3.0)
elem.clear()
elem.send_keys("pycon")
sleep(3.0)
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
