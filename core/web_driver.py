
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class WebDriver:

    def __init__(self):
        self.driver = None

    def open_url(self, url):
        if not self.driver:
            options = Options()
            options.add_experimental_option('extensionLoadTimeout', 60)
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=options)
            self.driver.set_page_load_timeout(60)
            self.driver.set_window_position(0, 0)
            self.driver.set_window_size(width=500, height=300)
        self.driver.get(url)

    def get_title(self):
        if self.driver:
            return self.driver.title
        else:
            return None

    def get_html(self):
        if self.driver:
            return self.driver.page_source
        else:
            return None

    def get_body_text(self):

        if self.driver:
            body_element = self.driver.find_element(By.XPATH, "//section[contains(@class,'mainContent')]") \
                if ("<section class=\"mainContent" in self.driver.page_source) \
                else self.driver.find_element(By.XPATH, '//body')
            return body_element.text
        else:
            return None

    def get_html_with_class(self, class_name):
        if self.driver:
            element = self.driver.find_element(By.CLASS_NAME, class_name)
            return element.get_attribute('outerHTML')
        else:
            return None

    def get_text_with_class(self, class_name):
        if self.driver:
            element = self.driver.find_element(By.CLASS_NAME, class_name)
            return element.text
        else:
            return None

    def get_image_links_with_class(self, class_name):
        if self.driver:
            element = self.driver.find_element(By.CLASS_NAME, class_name)
            img_elements = element.find_elements(By.XPATH, './/img')
            return [e.get_attribute('src') for e in img_elements]
        else:
            return None
        
    def get_html_with_xpath(self, xpath):
        if self.driver:
            element = self.driver.find_element(By.XPATH, xpath)
            return element.get_attribute('outerHTML')
        else:
            return None

    def get_text_with_xpath(self, xpath):
        if self.driver:
            element = self.driver.find_element(By.XPATH, xpath)
            return element.text
        else:
            return None

    def get_image_links_with_xpath(self, xpath):
        if self.driver:
            element = self.driver.find_element(By.XPATH, xpath)
            img_elements = element.find_elements(By.XPATH, './/img')
            return [e.get_attribute('src') for e in img_elements]
        else:
            return None


w_driver = WebDriver()
