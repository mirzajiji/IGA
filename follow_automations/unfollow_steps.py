import json
from time import sleep

from configuration.conftest import credentials, driver
from pages.before_sign import BeforeSign
from pages.message_page import MessagePage
from pages.unfollow_flow import UnfollowFLow


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
        with open('unfollow_list.json', encoding='utf-8') as f:
            data = json.load(f)

        # Extract usernames
        usernames = [entry['username'] for entry in data]

        # Print the list of usernames
        print("Usernames:", usernames)

        before_sign_page = BeforeSign(driver)
        unfollow_flow = UnfollowFLow(driver)
        before_sign_page.open()

        if authorised:
            before_sign_page.logged_in()
            sleep(2)
            for username in usernames:
                unfollow_flow.open_following_page(f"https://www.instagram.com/{username}")

                # unfollow_flow.unfollow()
                unfollow_flow.unfollow_under_hundred()

                sleep(1)
        else:
            before_sign_page.execute_login(credentials)
