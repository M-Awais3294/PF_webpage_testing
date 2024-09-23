import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.homePageElements import HomePage
from utilities.baseClass import BaseClass


class TestHomePage(BaseClass):

    # ----------------------------------- Navbar tests -----------------------------------
    def test_logo(self):

        home_page = HomePage(self.driver)

        logo = home_page.get_home_logo()
        logo.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.staleness_of(logo))
            print("Page refreshed after clicking the button.")
        except:
            print("Page did not refresh.")

    def test_about_us(self):

        home_page = HomePage(self.driver)
        home_page.get_about_us_btn().click()

        # verifying the change in URL
        assert "about-us" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_careers(self):

        home_page = HomePage(self.driver)
        home_page.get_careers_btn().click()

        # verifying the change in URL
        assert "career" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_open_positions(self):

        home_page = HomePage(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_careers_btn()).perform()
        actions.move_to_element(home_page.get_careers_dropdown_open_position()).click().perform()

        # verifying the change in URL
        assert "apply-now" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_life_at_pf(self):

        home_page = HomePage(self.driver)
        home_page.get_life_at_pf_btn().click()

        # verifying the change in URL
        assert "life-at-pf" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_expertise(self):

        home_page = HomePage(self.driver)
        home_page.get_expertise_btn().click()

        # verifying the change in URL
        assert "expertise" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_blogs(self):

        home_page = HomePage(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources_btn()).perform()
        actions.move_to_element(home_page.get_resources_dropdown_blogs()).click().perform()

        # verifying the change in URL
        assert "blogs" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_news(self):
        home_page = HomePage(self.driver)

        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources_btn()).perform()
        actions.move_to_element(home_page.get_resources_dropdown_news()).click().perform()

        # verifying the change in URL
        assert "news" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_graduate_gate_way(self):
        home_page = HomePage(self.driver)
        home_page.get_graduate_gateway_btn().click()

        # verifying the change in URL
        assert "trainee-program" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_apply_now(self):
        home_page = HomePage(self.driver)
        home_page.get_apply_now_btn().click()

        # verifying the change in URL
        assert "apply-now" in self.driver.current_url
        # Go back to Home Page
        self.driver.back()

    def test_uk_page(self):
        home_page = HomePage(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_pak_logo_dropdown()).perform()
        actions.move_to_element((home_page.get_uk_logo_btn())).click().perform()
        # Switching to child window
        self.driver.switch_to.window(self.driver.window_handles[1])

        # verifying the change in URL
        assert "https://programmersforce.co.uk/" == self.driver.current_url
        # Closing the new Tab page
        self.driver.close()
        # switching back to Parent window
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_france_page(self):
        home_page = HomePage(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_pak_logo_dropdown()).perform()
        actions.move_to_element((home_page.get_france_logo_btn())).click().perform()

        # Switching to child window
        self.driver.switch_to.window(self.driver.window_handles[1])
        # verifying the change in URL
        assert "https://programmersforce.fr/" == self.driver.current_url
        # Closing the new Tab page
        self.driver.close()
        # switching back to Parent window
        self.driver.switch_to.window(self.driver.window_handles[0])
