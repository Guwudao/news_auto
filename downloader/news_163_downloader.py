from .downloader import Downloader
from core.web_driver import w_driver


class News163Downloader(Downloader):

    def get_content(self, url: str):
        print(url)
        w_driver.open_url(url)
        self.title = w_driver.get_title()
        self.html_str = w_driver.get_html_with_class('post_body')
        self.text = w_driver.get_text_with_class('post_body')
        self.image_links = w_driver.get_image_links_with_class('post_body')
        self.store_data()
