import datetime
import random
import re
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.base import Base


def random_sleep(sleep_time):
    sleep_duration = random.uniform(1, sleep_time)
    sleep(sleep_duration)


def detect_url_parse(iteration_count):
    current_day = datetime.date.today(), datetime.time()
    print("ends: ", current_day)
    print("followed ", iteration_count, "accounts")


def get_path(count):
    return (By.XPATH,
            f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[{count}]/div/div/div/div[3]/div/button")


class FollowFLow(Base):
    like = 1
    __follow_button = (By.XPATH,
                       f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[{like}]/div/div/div/div[3]/div/button")
    __likes = (By.XPATH,
               "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/section[2]/div/div/span/a")
    __follower_count = (By.XPATH,
                        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/a")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def open_shop_page(self, url):
        super()._open_url(url)

    def follow_from_post_likes(self, url):
        super()._open_url(url)
        count = super()._get_text(self.__likes)
        super()._click(self.__likes)
        count = ''.join(re.findall(r'\d+', count))
        count = int(count)
        return count

    def follow_from_post_likes_upper_hundred(self, url):
        super()._open_url(url)
        count = super()._get_text(self.__likes)
        followers_count = super()._get_text(self.__follower_count)
        super()._click(self.__likes)
        count = ''.join(re.findall(r'\d+', count))
        count = int(count)
        return count

    def check_if_followed(self, path):
        status = super()._get_text(path)
        if status == 'Following' or status == 'Requested':
            return True
        else:
            return False

    def follow_click(self, follow_path):
        super()._click(follow_path)

    def scroll_down(self, follow_path):
        super()._send_keys(follow_path, Keys.DOWN)
        super()._send_keys(follow_path, Keys.DOWN)
