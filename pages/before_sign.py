from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.base import Base


class BeforeSign(Base):
    __url = "https://www.instagram.com/"
    __allow_all_cookies = (By.XPATH, "//button[@class='_a9-- _ap36 _a9_0']")
    __not_now = (By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']")
    __not_now2 = (By.XPATH, "//div[@class='_ac8f']")
    __user_name_field = (By.XPATH, "//input[@aria-label='Phone number, username, or email']")
    __password_field = (By.XPATH, "//input[@aria-label='Password']")
    __login_button = (By.XPATH,
                      "//button[@class=' _acan _acap _acas _aj1- _ap30']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_before_login(self, credentials):
        try:
            super()._click(self.__allow_all_cookies)
            sleep(3)
            super()._type(self.__user_name_field, credentials['username'])
            super()._type(self.__password_field, credentials['password'])
            # super()._click(self.__login_button)


        except NoSuchElementException as e:
            print(e)
        sleep(2)
        super()._click(self.__login_button)
        sleep(5)
        sleep(50)
        try:
            super()._click(self.__not_now2)
        except NoSuchElementException as e:
            sleep(5)
        try:
            super()._click(self.__not_now)
        except NoSuchElementException as e:
            sleep(5)
        sleep(5)
