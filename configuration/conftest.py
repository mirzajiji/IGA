import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def environment() -> bool:
    return False


@pytest.fixture(scope="module")
def credentials():
    return {'username': 'vertex1jiji@gmail.com', 'password': 'rtuliparoli.123$'}
    # return {'username': 'vertex2jiji@gmail.com', 'password': 'paroliparoli'}


@pytest.fixture()
def driver():
    options = Options()
    # options.binary_location = "C:\\Users\\Documents\\chromedriver.exe"

    chrome_driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
    options.binary_location = chrome_driver_path

    my_driver = webdriver.Chrome(options=options)
    yield my_driver
