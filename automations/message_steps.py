import json
import pickle
from time import sleep
import datetime

from selenium.webdriver.common.by import By

from base.pysnippets import *
from pages.follow_flow import FollowFLow
from base.followers_snippets import *

from pages.before_sign import BeforeSign
from configuration.conftest import credentials, driver
from pages.message_page import MessagePage


# rules
# 200 follow per day
# 150 unfollow per day


class TestMessageSteps:
    username_list = ["genosstore_", "mirzz_X"]
    total = 0
    last_day = None
    text = "Hii You look great. We would love to promote you on our Page. Are you interested? Please direct message at @v1_usr. Give my reference 'dh'. Send message 'dh' to @v1_usr.\n"

    def test_get_usernames(self, driver, credentials):
        authorised = True
        global state
        with open('list.json', encoding='utf-8') as f:
            data = json.load(f)

        # Extract usernames
        usernames = [entry['username'] for entry in data]

        # Print the list of usernames
        print("Usernames:", usernames)

        before_sign_page = BeforeSign(driver)
        message_flow = MessagePage(driver)
        before_sign_page.open()

        if authorised:
            before_sign_page.logged_in()
            sleep(2)
            for username in usernames:
                message_flow.open_model_page(f"https://www.instagram.com/{username}")

                message_flow.open_message()

                message_flow.start_type(self.text)

                sleep(1)
        else:
            before_sign_page.execute_login(credentials)
