import json
import os

from configuration.conftest import credentials, driver
from tiktok_downloader.pages.snaptik import SnipTik


class TestDownloadSteps:
    def test_download_by_list(self, driver):

        downloader = SnipTik(driver)
        try:
            downloader.download_from_tiktok_by_snip()
        except Exception as e:
            print(e)
