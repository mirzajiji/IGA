import json
from time import sleep
import datetime

from selenium.webdriver.common.by import By

from base.pysnippets import *
from pages.follow_flow import FollowFLow
from base.followers_snippets import *

from pages.before_sign import BeforeSign
from configuration.conftest import credentials, driver


# rules
# 200 follow per day
# 150 unfollow per day

class TestFollowSteps:
    username_list = ["genosstore_", "mirzz_X"]
    total = 0
    last_day = None

    def test_get_usernames(self, driver, credentials):
        global followers
        before_sign_page = BeforeSign(driver)
        follow_flow = FollowFLow(driver)
        before_sign_page.open()
        before_sign_page.execute_before_login(credentials)
        # driver.quit()
        # sleep(1)
        # before_sign_page.open()
        # before_sign_page.execute_cooked_login(credentials)
        sleep(5)

        current_day = datetime.date.today()

        for username in self.username_list:
            # driver.execute_script(run_js_script(username))
            # pyscript = run_script(username)
            # print("py ", pyscript)
            #
            # scripts = run_js_script(username)
            # # run_script("genosstore_")
            # modified_script = script.replace('{username}', username)
            # driver.execute_script(scripts)
            scripts = run_js_script(username)
            followers = driver.execute_script(scripts)

            # followers_script = run_js_script(username)
            # print(followers)

            # followers_script = run_js_script(username)
            # followers = driver.execute_script(followers_script)

            # print("data1", followers, "\n")
            sleep(20)
            # r = driver.execute_script("followers")
            # print(r)
            driver.execute_script("console.log('time to print');")
            print("time to print")

            # print(followers_script)

            # print("log: ", before_sign_page.execute_after_login())

            sleep(10)
        print("return script",followers)
        print("log: ", before_sign_page.execute_after_login())
        sleep(30)
        # run_script("genosstore_")
        # sleep(10)
        # while not driver.execute_script("return followersPopulated;"):
        #     sleep(1)
        # follower_usernames = driver.execute_script("return followers.map(follower => follower.username);")
        # following_usernames = driver.execute_script("return followings.map(following => following.username);")

        # Print the retrieved values
        # print("Follower Usernames:", follower_usernames)
        # print("Following Usernames:", following_usernames)
        # start logic
        # follower_length = len(follower_usernames)
        # counter = 0
        # for follower_username in follower_usernames:
        #     if counter != follower_length:
        #         follow_flow.open_shop_page(f"https://www.instagram.com/{follower_username}")
        #         follow_flow.follow_shop()
        #         counter += 1
        #         self.total += 0
        #         if self.total == 199:
        #             sleep_duration = (datetime.datetime.now() + datetime.timedelta(days=1)).replace(0, 0, 0, 0, 0,
        #                                                                                             0,
        #                                                                                             0) - datetime.datetime.now()
        #             print(f"Total reached 199. Sleeping until next day ({sleep_duration}).")
        #             sleep(sleep_duration.total_seconds())
        #             self.total = 0
        #             self.last_day = current_day
        #         elif self.total > 199:
        #             if current_day != self.last_day:
        #                 self.total = 0
        #                 self.last_day = current_day
        #                 print("Resetting total count for the new day.")
        #             break
        #         if counter % 8 == 0 and counter != 0:
        #             sleep(3600)
        #     else:
        #         counter = 0
        #         break
