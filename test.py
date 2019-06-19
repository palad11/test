from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'10000 RUR'))
button = browser.find_element_by_tag_name("button")
button.click()

a = browser.find_element_by_id('input_value').text
y = calc(a)
browser.find_element_by_id('answer').send_keys(y)
button = browser.find_element_by_id("solve")
button.click()
assert True