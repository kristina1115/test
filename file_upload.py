from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:

    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1=browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Kristina')
    
    input1=browser.find_element(By.NAME, 'lastname')
    input1.send_keys('Artemenko')
    
    input1=browser.find_element(By.NAME, 'email')
    input1.send_keys('Kristina_1651@mail.ru')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    file=browser.find_element(By.ID, 'file')
    file.send_keys(file_path)
    
    button=browser.find_element(By.TAG_NAME, 'button')
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    