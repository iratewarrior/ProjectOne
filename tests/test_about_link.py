import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_Page
from pages.client_information_page import Client_Information_Page
from pages.finish_page import Finish_Page
from pages.login_page import Login_Page
from pages.main_page import Main_Page
from pages.payment_page import Payment_Page


def test_about_link(set_up):
    driver = webdriver.Chrome(executable_path='/Users/iratewarrior/PycharmProjects/resources/chromedriver')

    print("Start Test")

    login = Login_Page(driver)
    login.autorization()

    mp = Main_Page(driver)
    mp.select_menu_about()

    print("Finish Test")

    time.sleep(10)
