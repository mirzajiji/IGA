import datetime
import random
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration.conftest import credentials, driver
from pages.before_sign import BeforeSign
from pages.follow_flow import FollowFLow, detect_url_parse, get_path, random_sleep


# rules
# 200 follow per day
# 150 unfollow per day


class TestMessageSteps:
    total = 0
    last_day = None

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
        follow_path = f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[8]/div/div/div/div[3]/div/button"
        follow_flow = FollowFLow(driver)
        before_sign_page = BeforeSign(driver)
        # message_flow = MessagePage(driver)
        before_sign_page.open()
        total_count = 1
        iteration_count = 1
        if authorised:
            before_sign_page.logged_in()
            sleep(2)
            for url in urls:
                likes = follow_flow.follow_from_post_likes(url)
                current_day = datetime.date.today(), datetime.time().hour, datetime.time().minute
                print("start: ", current_day)
                for like in range(1, likes):
                    if total_count > 8:
                        follow_path = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[9]/div/div/div/div[3]/div/button"
                    else:
                        follow_path = f"/html/body/div[6]/div[1]/div/div[2]/div/di v/div/div/div/div[2]/div/div/div[{like}]/div/div/div/div[3]/div/button"
                    element_locator = (By.XPATH, follow_path)
                    sleep(3)
                    status = follow_flow.check_if_followed(element_locator)
                    if status:
                        follow_flow.scroll_down(element_locator)
                    else:
                        follow_flow.follow_click(element_locator)
                        follow_flow.scroll_down(element_locator)
                        random_sleep(8)
                        iteration_count += 1
                        total_count += 1

            detect_url_parse(iteration_count)
            sleep(200)

        else:
            before_sign_page.execute_login(credentials)
