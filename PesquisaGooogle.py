from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from time import sleep

nav = Firefox()

nav.get('http://google.com.br/')


campo_busca = nav.find_element_by_name('q')
sleep(3.0)

campo_busca.send_keys('Youtube')
sleep(3.0)

campo_busca.send_keys(Keys.ENTER)
sleep(2.0)


campo_busca = nav.find_element_by_class_name('r')
print(campo_busca.text)




