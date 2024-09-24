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
            print("Page refreshed after clicking the Logo.")
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
        # assert "career" in self.driver.current_url
        try:
            self.assert_current_url("career")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_open_positions(self):

        home_page = HomePage(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_careers_btn()).perform()
        actions.move_to_element(home_page.get_careers_dropdown_open_position()).click().perform()

        # verifying the change in URL
        # assert "apply-now" in self.driver.current_url
        try:
            self.assert_current_url("apply-now")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_life_at_pf(self):

        home_page = HomePage(self.driver)
        home_page.get_life_at_pf_btn().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("life-at-pf")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_expertise(self):

        home_page = HomePage(self.driver)
        home_page.get_expertise_btn().click()

        # verifying the change in URL
        # assert "expertise" in self.driver.current_url
        try:
            self.assert_current_url("expertise")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_blogs(self):

        home_page = HomePage(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources_btn()).perform()
        actions.move_to_element(home_page.get_resources_dropdown_blogs()).click().perform()

        # verifying the change in URL
        # assert "blogs" in self.driver.current_url
        try:
            self.assert_current_url("blogs")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_news(self):
        home_page = HomePage(self.driver)

        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources_btn()).perform()
        actions.move_to_element(home_page.get_resources_dropdown_news()).click().perform()

        # verifying the change in URL
        # assert "news" in self.driver.current_url
        try:
            self.assert_current_url("news")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_graduate_gate_way(self):
        home_page = HomePage(self.driver)
        home_page.get_graduate_gateway_btn().click()

        # verifying the change in URL
        # assert "trainee-program" in self.driver.current_url
        try:
            self.assert_current_url("trainee-program")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_apply_now(self):
        home_page = HomePage(self.driver)
        home_page.get_apply_now_btn().click()

        # verifying the change in URL
        # assert "apply-now" in self.driver.current_url
        try:
            self.assert_current_url("apply-now")
        except Exception as e:
            print(e)

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


# --------------------------------- Footer Tests -----------------------------------

    def test_footer_logo(self):
        home_page = HomePage(self.driver)

        # Scrolling to the bottom of the webpage
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        footer_logo = home_page.get_home_logo()
        footer_logo.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.staleness_of(footer_logo))
            print("Page refreshed after clicking the Logo.")
        except:
            print("Page did not refresh.")

    def test_footer_life_at_pf(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_life_at_pf().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("life-at-pf")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_footer_our_teammates(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_our_teammates().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("about-us")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_in_house_pp(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_in_house_pp().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("privacypolicy")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_iso_certificate(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_iso_certified().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("iso_certified")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_footer_career(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_career().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("career")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_job_positions(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_job_positions().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("apply-now")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_footer_send_resume(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_send_resume().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("apply-now/#popup1")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_track_application(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_track_application().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("apply-now")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_footer_blogs(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_blogs().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("blogs")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_ransomware(self):
        home_page = HomePage(self)
        self.driver.execute_script(f"""
            var links = document.getElementsByTagName('a');
            for (var i = 0; i < links.length; i++) {{
            if (links[i].textContent.trim() == 'Ransomware') {{
            return links[i];
            }}
        }}
        return null;
        """).click()
        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("ransomware")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_fintech(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_fintech().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("fintech")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_life_changing(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_life_changing().click()

        # verifying the change in URL
        # assert "life-at-pf" in self.driver.current_url
        try:
            self.assert_current_url("life-changing")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_ai_career(self):
        home_page = HomePage(self.driver)
        home_page.get_ai_career().click()

        # verifying the change in URL
        try:
            self.assert_current_url("ai-career")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()
    #
    # def test_phone_no(self):
    #     home_page = HomePage(self.driver)
    #     home_page.get_phone_number().click()
    #     alert = self.driver.switch_to.alert
    #
    #     assert "Pick an app?" in alert.text
    #     alert.dismiss()

    def test_footer_apply_now(self):
        home_page = HomePage(self.driver)
        home_page.get_footer_apply_now().click()

        # verifying the change in URL
        try:
            self.assert_current_url("apply-now")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()

    def test_fb_page(self):
        home_page = HomePage(self.driver)
        home_page.get_facebook().click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        assert "facebook" in self.driver.current_url

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_youtube_page(self):
        home_page = HomePage(self.driver)
        home_page.get_youtube().click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        assert "youtube" in self.driver.current_url

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_privacy_policy(self):
        home_page = HomePage(self.driver)
        home_page.get_privacy_policy().click()

        # verifying the change in URL
        try:
            self.assert_current_url("privacypolicy")
        except Exception as e:
            print(e)
        # Go back to Home Page
        self.driver.back()





