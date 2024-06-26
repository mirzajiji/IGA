import datetime
import random
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration.conftest import credentials, driver
from pages.before_sign import BeforeSign
from pages.follow_flow import FollowFLow


# rules
# 200 follow per day
# 150 unfollow per day


class TestMessageSteps:
    total = 0
    last_day = None
    text = "Hii You look great. We would love to promote you on our Page. Are you interested? Please direct message at @v1_usr. Give my reference 'dh'. Send message 'dh' to @v1_usr.\n"

    def test_follow_from_post_likes_url(self, driver, credentials):
        global like, follow_status, follow_button, element_locator
        authorised = True
        urls = ["https://www.instagram.com/p/C6hHkbNvRAv/?img_index=1",
                "https://www.instagram.com/p/C6PHNuyvYnD/?img_index=1"
            , "https://www.instagram.com/p/C6CH39Jv-NN/?img_index=1"
            , "https://www.instagram.com/p/C5ys-aePGqJ/?img_index=1"
            , "https://www.instagram.com/p/C5EejYtSbsL/?img_index=1"
            , "https://www.instagram.com/p/C4_NWjTvjFY/?img_index=1"
            , "https://www.instagram.com/p/C4ga7x6PZee/?img_index=1"
            , "https://www.instagram.com/p/C4a5-DoLHX3/?img_index=1"
            , "https://www.instagram.com/p/C3RKetCRBKy/?img_index=1"
            , "https://www.instagram.com/p/C3BPFu_SCSf/?img_index=1"
            , "https://www.instagram.com/p/C6xHN4XOQm_/?img_index=1"
                ]

        follow_flow = FollowFLow(driver)
        before_sign_page = BeforeSign(driver)
        # message_flow = MessagePage(driver)
        before_sign_page.open()

        if authorised:
            before_sign_page.logged_in()
            sleep(2)
            for url in urls:
                likes = follow_flow.follow_from_post_likes(url)
                total_count = 1
                iteration_count = 1
                current_day = datetime.date.today(), datetime.time()
                print("start: ", current_day)
                for like in range(1, likes):
                    sleep(2)

                    index = like
                    follow_path = f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[8]/div/div/div/div[3]/div/button"

                    if total_count > 8:

                        follow_path = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[9]/div/div/div/div[3]/div/button"
                        element_locator = (By.XPATH, follow_path)

                    else:
                        follow_path = f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[{like}]/div/div/div/div[3]/div/button"
                        element_locator = (By.XPATH, follow_path)
                        follow_button = WebDriverWait(driver, 10).until(
                            EC.visibility_of_element_located(element_locator))
                        follow_button.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)

                    follow_button = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(element_locator))
                    follow_status = follow_button.text

                    if follow_status == "Following" or follow_status == "Requested":
                        follow_button.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)

                    elif follow_status != "Following" or follow_status != "Requested":

                        follow_button.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)
                        follow_button.click()
                        sleep_duration = random.uniform(1, 8)
                        iteration_count += 1
                        total_count += 1
                        sleep(sleep_duration)
                    else:
                        print("skipped")

                current_day = datetime.date.today(), datetime.time()
                print("=ends: ", current_day)
                print("followed ", iteration_count, "accounts")
            sleep(300)

        else:
            before_sign_page.execute_login(credentials)
