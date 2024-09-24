from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # -------------------------------- Header Elements and getters ----------------------------

    __home_logo = (By.CLASS_NAME, "home-logo")
    __about_us = (By.XPATH, "//a[contains(text(), 'About Us')]")
    __careers = (By.XPATH, "//a[contains(text(), 'Careers')]")
    __open_positions = (By.LINK_TEXT, "Open Positions")
    __life_at_pf = (By.XPATH, "//a[contains(text(),'Life at PF')]")
    __expertise = (By.XPATH, "//a[contains(text(),'Expertise')]")
    __resources = (By.LINK_TEXT, "Resources")
    __blogs = (By.XPATH, "//li[@id='menu-item-3168']/ul/li/a[contains(text(), 'Blogs')]")
    __news = (By.XPATH, "//li[@id='menu-item-3168']/ul/li/a[contains(text(), 'News')]")
    __graduate_gateway = (By.XPATH, "//a[contains(text(),'Graduate Gateway Program')]")
    __apply_now = (By.XPATH, "//li[@id='menu-item-16']/a[contains(text(), 'Apply Now')]")
    __pak_page_btn = (By.CLASS_NAME, "imgdiv")
    __uk_page_btn = (By.CSS_SELECTOR, "div[class='contdive'] p[class*='languages-uk'] a")
    __france_page_btn = (By.XPATH, "//a[contains(text(),'FR')]")

    def get_home_logo(self):
        return self.driver.find_element(*HomePage.__home_logo)

    def get_about_us_btn(self):
        return self.driver.find_element(*HomePage.__about_us)
#       Query: If changing to about us page, usually we want the object to turn from homePage to aboutUs page
#       but when testing for Home page we don't want that but for About Us page we want to change it.

    def get_careers_btn(self):
        return self.driver.find_element(*HomePage.__careers)

    def get_careers_dropdown_open_position(self):
        return self.driver.find_element(*HomePage.__open_positions)

    def get_life_at_pf_btn(self):
        return self.driver.find_element(*HomePage.__life_at_pf)

    def get_expertise_btn(self):
        return self.driver.find_element(*HomePage.__expertise)

    def get_resources_btn(self):
        return self.driver.find_element(*HomePage.__resources)

    def get_resources_dropdown_blogs(self):
        return self.driver.find_element(*HomePage.__blogs)

    def get_resources_dropdown_news(self):
        return self.driver.find_element(*HomePage.__news)

    def get_graduate_gateway_btn(self):
        return self.driver.find_element(*HomePage.__graduate_gateway)

    def get_apply_now_btn(self):
        return self.driver.find_element(*HomePage.__apply_now)

    def get_pak_logo_dropdown(self):
        return self.driver.find_element(*HomePage.__pak_page_btn)

    def get_uk_logo_btn(self):
        return self.driver.find_element(*HomePage.__uk_page_btn)

    def get_france_logo_btn(self):
        return self.driver.find_element(*HomePage.__france_page_btn)

#     ------------------------------- Footer Elements and Getters --------------------------------

    __footer_logo = (By.CLASS_NAME, "ls-is-cached")
    __life_at_pf_footer = (By.LINK_TEXT, "Life At Programmers force")
    __our_teammates = (By.LINK_TEXT, "Our Teammates")
    __in_house_privacy_policy = (By.LINK_TEXT, "In House Privacy Policy")
    __iso_certified = (By.LINK_TEXT, "ISO Certified")
    __career_footer = (By.LINK_TEXT, "Career")
    __job_positions = (By.LINK_TEXT, "Job Positions")
    __send_resume = (By.XPATH, "//ul[@class='ulfooter careers']/li/a[contains(text(), 'Send Resume')]")
    __track_application = (By.LINK_TEXT, "Track your Application")
    __blogs_footer = (By.CSS_SELECTOR, "h2[class*='blogs'] a")
    __fintech = (By.LINK_TEXT, "FinTech")
    __life_changing = (By.LINK_TEXT, "Life-changing")
    __ai_career = (By.LINK_TEXT, "AI Career")
    __phone_number = (By.LINK_TEXT, "+92 301-588-8444")
    __apply_now_footer = (By.XPATH, "//ul[@class='ulfooter contact']/li/a[contains(text(), 'Apply Now')]")
    __facebook = (By.CSS_SELECTOR, "ul[class='social'] li a img[alt='fb']")
    __linkedin = (By.CSS_SELECTOR, "ul[class='social'] li a img[alt='link']")
    __youtube = (By.CSS_SELECTOR, "ul[class='social'] li a img[class*='youtube']")
    __privacy_policy = (By.LINK_TEXT, "Privacy Policy")

    def get_footer_logo(self):
        return self.driver.find_element(*HomePage.__footer_logo)

    def get_footer_life_at_pf(self):
        return self.driver.find_element(*HomePage.__life_at_pf_footer)

    def get_footer_our_teammates(self):
        return self.driver.find_element(*HomePage.__our_teammates)

    def get_footer_in_house_pp(self):
        return self.driver.find_element(*HomePage.__in_house_privacy_policy)

    def get_footer_iso_certified(self):
        return self.driver.find_element(*HomePage.__iso_certified)

    def get_footer_career(self):
        return self.driver.find_element(*HomePage.__career_footer)

    def get_footer_job_positions(self):
        return self.driver.find_element(*HomePage.__job_positions)

    def get_footer_send_resume(self):
        return self.driver.find_element(*HomePage.__send_resume)

    def get_footer_track_application(self):
        return self.driver.find_element(*HomePage.__track_application)

    def get_footer_blogs(self):
        return self.driver.find_element(*HomePage.__blogs_footer)

    def get_footer_fintech(self):
        return self.driver.find_element(*HomePage.__fintech)

    def get_footer_life_changing(self):
        return self.driver.find_element(*HomePage.__life_changing)

    def get_ai_career(self):
        return self.driver.find_element(*HomePage.__ai_career)

    # def get_phone_number(self):
    #     return self.driver.find_element(*HomePage.__phone_number)

    def get_footer_apply_now(self):
        return self.driver.find_element(*HomePage.__apply_now_footer)

    def get_facebook(self):
        return self.driver.find_element(*HomePage.__facebook)

    def get_youtube(self):
        return self.driver.find_element(*HomePage.__youtube)

    def get_privacy_policy(self):
        return self.driver.find_element(*HomePage.__privacy_policy)




