import json
import random
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from configuration.conftest import credentials, driver
from pages.before_sign import BeforeSign
from pages.message_page import MessagePage
from pages.follow_flow import FollowFLow

from selenium.webdriver.support import expected_conditions as EC


# rules
# 200 follow per day
# 150 unfollow per day


class TestMessageSteps:
    username_list = ["genosstore_", "mirzz_X"]
    total = 0
    last_day = None
    text = "Hii You look great. We would love to promote you on our Page. Are you interested? Please direct message at @v1_usr. Give my reference 'dh'. Send message 'dh' to @v1_usr.\n"

    def test_follow_from_post_likes_url(self, driver, credentials):
        authorised = True
        url = "https://www.instagram.com/p/CrQcpOwPOYg/?img_index=1"

        follow_flow = FollowFLow(driver)
        before_sign_page = BeforeSign(driver)
        # message_flow = MessagePage(driver)
        before_sign_page.open()

        if authorised:
            before_sign_page.logged_in()
            sleep(2)

            likes = follow_flow.follow_from_post_likes(url)
            iteration_count = 0

            for like in range(1, likes):
                sleep(2)
                follow_path = f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[{like}]/div/div/div/div[3]/div/button"
                element_locator = (By.XPATH, follow_path)
                follow_button = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(element_locator)
                )
                follow_status = follow_button.text

                if follow_status == "Following":
                    follow_button.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)
                    pass
                else:
                    follow_button.click()
                    follow_button.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)
                    iteration_count += 1

                sleep_duration = random.uniform(1, 5)
                sleep(sleep_duration)
                if iteration_count % 8 == 0:
                    print("Sleeping for 1 hour...")
                    sleep(3600)
                    print("Resuming actions...")



        else:
            before_sign_page.execute_login(credentials)
