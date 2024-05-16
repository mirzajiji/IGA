from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.base import Base


class MessagePage(Base):
    # __message = (By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']")
    __message = (By.XPATH,
                 "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div")
    __input_field = (By.XPATH, "//div[@aria-label='Message']")
    __dismiss = (By.XPATH, "//div[@aria-label='Dismiss']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def open_model_page(self, url):
        super()._open_url(url)

    def open_message(self):
        super()._click(self.__message)

    def start_type(self, text):
        super()._type(self.__input_field, text)
        sleep(1)

    def check_dismiss(self):
        try:
            super()._click(self.__dismiss)
            sleep(2)
        except Exception:
            pass
