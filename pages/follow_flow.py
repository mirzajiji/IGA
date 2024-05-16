from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.base import Base


class FollowFLow(Base):
    __follow_button = (By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']")
    __likes = (By.XPATH,
               "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/section[2]/div/div/span/a")

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

    def follow_from_post_likes(self, url):
        super()._open_url(url)
        sleep(1)
        count = super()._get_text(self.__likes)
        super()._click(self.__likes)
        count = count.replace(' likes', '')
        count = count.replace(',', '')
        count = int(count)
        return count
