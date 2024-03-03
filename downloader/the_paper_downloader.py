from .downloader import Downloader
from core.web_driver import w_driver


class ThePaperDownloader(Downloader):

    def get_content(self, url: str):
        print(url)
        w_driver.open_url(url)

        self.title = w_driver.get_title()
        self.html_str = w_driver.get_html_with_xpath("//div[contains(@class, 'index_wrap__')]")
        self.text = w_driver.get_text_with_xpath("//div[contains(@class, 'index_wrap__')]")
        self.image_links = w_driver.get_image_links_with_xpath("//div[contains(@class, 'index_wrap__')]")
        self.store_data()
