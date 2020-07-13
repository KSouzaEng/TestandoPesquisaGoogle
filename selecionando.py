from selenium.webdriver import  Firefox
from selenium.webdriver.support.ui import  Select
from time import sleep

navegar = Firefox()

navegar.get('file:///C:/Users/KAREM%20&%20LUCAS%20SZ/Documents/Selenium/Testes%20com%20Selenium/Estudando%20Selenium/select.html')

estados = Select(navegar.find_element_by_name('estados'))

sleep(2.0)

estados.select_by_visible_text('MG')

estados.select_by_value('rj')
