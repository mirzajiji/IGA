import pickle
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.base import Base


class BeforeSign(Base):
    __url = "https://www.tiktok.com/"
    __allow_all_cookies = (By.XPATH, "//button[@class='_a9-- _ap36 _a9_0']")
    __not_now = (By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']")
    __not_now2 = (By.XPATH, "//div[@class='_ac8f']")
    __dismiss = (By.XPATH, "//div[@aria-label='Dismiss']")
    __user_name_field = (By.XPATH, "//input[@aria-label='Phone number, username, or email']")
    __password_field = (By.XPATH, "//input[@aria-label='Password']")
    __login_button = (By.XPATH,
                      "//button[@class=' _acan _acap _acas _aj1- _ap30']")
    __guest_login_button = (By.XPATH,)

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
        sleep(3)

    def open_as_guest(self):
        super()._open_url(self.__url)
        sleep(3)

    def open_by_username(self,link):
        super()._open_url(link)

    def execute_login(self, credentials):
        try:

            super()._type(self.__user_name_field, credentials['username'])
            super()._type(self.__password_field, credentials['password'])


        except NoSuchElementException as e:
            print(e)
        sleep(2)
        super()._click(self.__login_button)
        sleep(10)
        state = self._driver.get_cookies()

        pickle.dump(state, open("auth.pkl", "wb"))
        print("cookie", state)
        self._driver.quit()

    def execute_before_login(self, credentials):
        try:

            super()._type(self.__user_name_field, credentials['username'])
            super()._type(self.__password_field, credentials['password'])

        except NoSuchElementException as e:
            print(e)
        sleep(2)
        super()._click(self.__login_button)
        sleep(5)
        sleep(10)
        try:
            super()._click(self.__dismiss)
            sleep(2)
        except Exception:
            pass
        try:
            super()._click(self.__not_now)
            sleep(2)
        except Exception:
            pass
        try:
            super()._click(self.__not_now2)
            sleep(2)
        except Exception:
            pass
        sleep(5)
        # with open('cookies.pkl', 'wb') as file:
        #     pickle.dump(super()._get_cookies(), file)
        #     # pickle.dump(driver.get_cookies(), file)

    def execute_cooked_login(self, credentials):

        with open('cookies.pkl', 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                super()._add_cookie(cookie)

        super()._refresh()
        sleep(10)

    def execute_after_login(self):
        super()._get_log()

    def logged_in(self):
        self._driver.get("https://www.instagram.com/")
        cookies = pickle.load(open("auth.pkl", "rb"))
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        super()._refresh()
        sleep(10)
