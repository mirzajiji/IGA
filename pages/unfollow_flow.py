import re
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.base import Base


class UnfollowFLow(Base):
    __unfollow_button = (By.XPATH,
                         "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button/div/div[1]")
    __unfollow_confirm_button = (
        By.XPATH, "//div[@tabindex='0'][5]")
    __follower_count = (By.XPATH,
                        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/a")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def open_following_page(self, url):
        super()._open_url(url)

    def follow_shop(self):
        if super()._check_if_followed(self.__unfollow_button):
            print("followed")
            pass
        else:
            super()._click(self.__unfollow_button)

    def unfollow(self):
        status = super()._get_text(self.__unfollow_button)
        if status == 'Following':
            super()._click(self.__unfollow_button)
            super()._click(self.__unfollow_confirm_button)
            sleep(0.5)
        else:
            pass

    def unfollow_under_hundred(self):
        status = super()._get_text(self.__unfollow_button)
        followers_count = super()._get_text(self.__follower_count)

        # count = count.replace(' followers', '')
        followers_count = ''.join(re.findall(r'\d+', followers_count))
        followers_count = int(followers_count)
        if status == 'Following' and followers_count <= 100:
            super()._click(self.__unfollow_button)
            super()._click(self.__unfollow_confirm_button)
            sleep(0.5)
        else:
            pass
