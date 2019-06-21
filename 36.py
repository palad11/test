from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

import time
import math
@pytest.fixture(scope="function")
def answer():
    return str(math.log(int(time.time())))
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page', ["http://stepik.org/lesson/236895/step/1",
"http://stepik.org/lesson/236896/step/1",
"http://stepik.org/lesson/236897/step/1",
"http://stepik.org/lesson/236898/step/1",
"http://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
class TestMainPage(object):
    
    
    @pytest.mark.smoke
    def test_guest_can_login(self, browser, page, answer):
        link = page
        browser.get(link)
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Type your answer here...']"))).send_keys(
            answer())
        
        browser.find_element_by_class_name('submit-submission').click()

        assert WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text == 'Correct!', 'мимо'
