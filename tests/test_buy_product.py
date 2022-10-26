import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_Page
from pages.main_page import Main_Page


def test_buy_product():
    driver = webdriver.Chrome(executable_path='/Users/iratewarrior/PycharmProjects/resources/chromedriver')

    print("Start Test")

    login = Login_Page(driver)
    login.autorization()

    mp = Main_Page(driver)
    mp.select_product()


    time.sleep(10)
