import pytest

from tests.pages.settings_page import SettingsPage
from tests.test_base import BaseTest


class TestSettings(BaseTest):

    @classmethod
    def setup_class(cls):
        print("\nSetup class ...")

    def test_distiller_login(self, driver):
        settings_page = SettingsPage(driver)
        settings_page.toggle_airplane_mode()
