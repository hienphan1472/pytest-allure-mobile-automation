import logging

import allure

from selenpy.support import factory
from tests.pages.home_page import HomePage
from tests.pages.profile_page import ProfilePage
from tests.pages.sign_in_page import SignInPage
from tests.test_base import TestBase
from tests.utilities import constants


class TestDemo(TestBase):

    home_page = HomePage()
    profile_page = ProfilePage()
    sign_in_page = SignInPage()

    @allure.title("Verify that the user can sign in successfully with correct account!")
    def test_sign_in(self):
        self.home_page.tap_profile()
        self.profile_page.tap_sign_in()
        self.sign_in_page.sign_in(constants.USER_EMAIL, constants.USER_PASSWORD)
        self.sign_in_page.verify_sign_in()
