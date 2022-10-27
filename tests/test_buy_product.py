import time

import pytest
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


@pytest.mark.run(order=3)
def test_buy_product_1(set_up):
    driver = webdriver.Chrome(executable_path='/Users/iratewarrior/PycharmProjects/resources/chromedriver')

    print("Start Test 1")

    login = Login_Page(driver)
    login.autorization()

    mp = Main_Page(driver)
    mp.add_product_1()

    cp = Cart_Page(driver)
    cp.product_confirmation()

    cip = Client_Information_Page(driver)
    cip.input_info()

    p = Payment_Page(driver)
    p.payment()

    f = Finish_Page(driver)
    f.finish()

    print("Finish Test 1")

    # time.sleep(10)

@pytest.mark.run(order=1)
def test_buy_product_2(set_group):
    driver = webdriver.Chrome(executable_path='/Users/iratewarrior/PycharmProjects/resources/chromedriver')

    print("Start Test 2")

    login = Login_Page(driver)
    login.autorization()

    mp = Main_Page(driver)
    mp.add_product_2()

    cp = Cart_Page(driver)
    cp.product_confirmation()

    print("Finish Test 2")

    # time.sleep(10)

@pytest.mark.run(order=2)
def test_buy_product_3():
    driver = webdriver.Chrome(executable_path='/Users/iratewarrior/PycharmProjects/resources/chromedriver')

    print("Start Test 3")

    login = Login_Page(driver)
    login.autorization()

    mp = Main_Page(driver)
    mp.add_product_3()

    cp = Cart_Page(driver)
    cp.product_confirmation()

    print("Finish Test 3")

    # time.sleep(10)
