from pageObjects.homePageElements import HomePage
from utilities.baseClass import BaseClass


class TestFormApplyNow(BaseClass):

    def test_form(self):
        home_page = HomePage(self.driver)
        home_page.get_apply_now_btn().click()


