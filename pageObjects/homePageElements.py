from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

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

