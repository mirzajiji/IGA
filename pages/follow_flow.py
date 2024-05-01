from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.base import Base


class FollowFLow(Base):
    __follow_button = (By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def open_shop_page(self, url):
        super()._open_url(url)

    def follow_shop(self):
        if super()._check_if_followed(self.__follow_button):
            print("followed")
            pass
        else:
            super()._click(self.__follow_button)
