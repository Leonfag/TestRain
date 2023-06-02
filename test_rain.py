# Implementation of Selenium test automation for this Selenium Python Tutorial
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def __init__(self, executable_path="chromedriver", port=0,
             options=None, service_args=None,
             desired_capabilities=None, service_log_path=None,
             chrome_options=None):
    executable_path = "/home/s4m4r1t4n/eclipse-workspace/RainAQA/src/test/resources/chromedriver"

def test_rain_demo():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome('./chromedriver', options=chrome_options)

    browser.get('https://www.rainapp.com/book-a-demo')
    browser.maximize_window()


    emailField = browser.find_element(By.XPATH, '//input[@type=\'email\']')
    emailField2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type=\'email\']')))
    emailField2.click()
    browser.implicitly_wait(10)

    emailField2.send_keys('leon@instaleap.io')

    browser.implicitly_wait(10)



    sleep(2)
    browser.close()