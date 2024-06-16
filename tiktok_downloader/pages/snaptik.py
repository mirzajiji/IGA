import json
import os
import random
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base.base import Base


def random_sleep(sleep_time):
    sleep_duration = random.uniform(1, sleep_time)
    sleep(sleep_duration)


class SnipTik(Base):
    __url = "https://snaptik.app/"

    __input_url = (By.XPATH, '(//input[@id="url"])')

    __download_button = (By.XPATH, '//button[@type="submit"]')

    __confirm_download = (By.XPATH, "/html/body/section/div/div[2]/div/div[2]/a[1]")
    __download_another_video = (By.XPATH, '/html/body/section/div/div[2]/div/div[2]/a[3]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def open(self, url):
        super()._open_url(url)

    def click_with_exception_handling(self, locator):
        try:
            super()._click(locator, 1)
        except Exception as e:
            print(e)

    def download_from_tiktok_by_snip(self):

        file_path = os.path.join('..', 'data', 'data.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
        data_len = len(data['videos'])
        print(f"size: {len(data['videos'])}")
        count = 0
        for video in data['videos']:
            try:
                super()._open_url(self.__url)

                self.driver.switch_to.window(self.driver.window_handles[0])

                super()._type(self.__input_url, video)

                super()._click(self.__download_button, 2)

                sleep(1)

                super()._click(self.__confirm_download, 10)
                count += 1
                if count > data_len - 2:
                    sleep(4)

            except Exception as e:
                print(f"skipped {video}\n reason: {e}")
