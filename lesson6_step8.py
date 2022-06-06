from selenium import webdriver
import time
import math

#link = 'http://suninjuly.github.io/find_xpath_form'
#link = 'http://suninjuly.github.io/registration1.html'
#link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('div:nth-child(1) input')
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys('Petrov')
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys('Smolensk')
    input4 = browser.find_element_by_id('country')
    input4.send_keys('Russia')
    button2 = browser.find_element_by_xpath('//button[@type="submit"]')
    button2.click()

finally:
    time.sleep(30)
    browser.quit()
