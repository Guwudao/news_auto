from .web_common import WebCommon
import requests
from fake_headers import Headers
from lxml import etree
import json
from .website_config import sohu_crawl_list


class Sohu(WebCommon):

    def __init__(self):
        self.url = "https://www.sohu.com/"
        self.header = Headers(
                # generate any browser & os headeers
                headers=False  # don`t generate misc headers
            ).generate()
        self.host = "https://www.sohu.com"

    def run(self):
        resp = requests.get(url=self.url, headers=self.header)
        # print(resp.text)
        tree = etree.HTML(resp.text)
        navi_item_list = tree.xpath("//a[@class=\"nav-item 2\"]")
        print("&" * 100)
        news_type_list = []
        for item in navi_item_list:
            news_type = {
                "title": item.text.strip(),
                "link": item.get("href")
            }
            news_type_list.append(news_type)
        print(news_type_list)
        print("&" * 100)

        strong_navi_item_list = tree.xpath("//a[@class=\"nav-item\"]")
        for item in strong_navi_item_list:
            strong_text = item.xpath("strong/text()")[0]
            news_type = {
                "title": strong_text,
                "link": item.get("href")
            }
            news_type_list.append(news_type)

        self.get_detail_news_list(news_type_list)

        li_a_list = tree.xpath("//li/a")
        news_list = []
        for news in li_a_list:
            # print(news.get("title"))
            # print(news.get("href"))
            if news.get("title") and news.get("href"):
                news_item = {
                    "platform": "sohu",
                    "title": news.get("title"),
                    "link": self.host + news.get("href")
                }
                news_list.append(news_item)

        # print("*" * 100)
        # textarea_data = tree.xpath("//script")
        # for t in textarea_data:
        #     if t.text and "window.PcHomeClientData" in t.text:
        #         json_str = t.text.replace('window.PcHomeClientData=', '').strip()
        #         json_data = json.loads(json_str)
        #         print(json_data)
        #         print("=" * 100)
        #
        #         for data in json_data:
        #             print(data["param"])

        return news_list

    def get_detail_news_list(self, type_list):
        print("#" * 100)
        for new_type in type_list:
            if new_type["title"] in sohu_crawl_list:
                resp = requests.get(new_type["link"], headers=self.header)
                print(resp.text)
                print("=" * 100)
