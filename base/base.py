from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple):
        self._find(locator).clear()
        # self._driver.execute_script("arguments[0].value = '';", locator)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _send_tab_multiple_times(self, locator: tuple, count, time: int = 10):
        for x in range(count):
            self._wait_until_element_is_visible(locator, time)
            self._find(locator).send_keys(Keys.TAB)

    def _get_log(self):
        full_log = []
        logs = self._driver.get_log('browser')
        print(logs)

        # for follower in logs:
            # full_log.append(f"Timestamp: {log['timestamp']}, Level: {log['level']}, Message: {log['message']}")
            # full_log.append((f"Username: {follower['username']}, Full Name: {follower['full_name']}"))

        return full_log

    def _send_space_multiple_times(self, locator: tuple, count, time: int = 10):
        for x in range(count):
            self._wait_until_element_is_visible(locator, time)
            self._find(locator).send_keys(Keys.SPACE)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(EC.visibility_of_element_located(locator))

    def _wait_until_element_is_invisible(self, locator: tuple, time: int = 300):
        wait = WebDriverWait(self._driver, time)
        wait.until(EC.invisibility_of_element_located(locator))

    @property
    def current_url(self):
        return self._driver.current_url

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _input_player_match_in_grid(self, locator: tuple, player, time=10) -> bool:
        if self._get_text(locator, time) == player:
            return True
        else:
            return False

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            if self._find(locator).is_displayed():
                return self._find(locator).is_displayed()

        except NoSuchElementException as e:
            print("An error occurred:", str(e))
            return False

    def _return_html(self):
        return self._driver.page_source

    def _check_if_followed(self, locator, followed="Follow", time=10) -> bool:
        if self._get_text(locator, time) == followed:
            return True
        else:
            return False

    def _open_new_tab(self):
        self._driver.execute_script("window.open('');")
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def _get_cookies(self):
        self._driver.get_cookies()

    def _add_cookie(self, cookie):
        self._driver.add_cookie(cookie)

    def _refresh(self):
        self._driver.refresh()
