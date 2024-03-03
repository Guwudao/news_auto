from abc import ABC, abstractmethod
from core.string_utils import StringUtils
from core.config import configer
from core.file_utils import FileUtils
import os
import requests
from markdownify import markdownify as md


class Downloader(ABC):

    def __init__(self):
        self.title = ''
        self.html_str = ''
        self.text = ''
        self.image_links = []

    @abstractmethod
    def get_content(self, url: str):
        pass

    def store_data(self):
        if self.html_str and self.text and self.image_links:
            legal_title = StringUtils.legitimate_page_title(self.title)
            markdown_text = md(self.html_str)

            paper_dir = os.path.join(configer.config['outputDir'], legal_title)
            paper_html_path = os.path.join(paper_dir, 'paper.html')
            paper_text_path = os.path.join(paper_dir, 'paper.txt')
            paper_md_path = os.path.join(paper_dir, 'paper.md')

            FileUtils.create_dir_if_not_exist(paper_dir)

            with open(paper_html_path, 'w', encoding='utf-8') as file:
                file.write(self.html_str)

            with open(paper_md_path, 'w', encoding='utf-8') as file:
                file.write(markdown_text)

            with open(paper_text_path, 'w', encoding='utf-8') as file:
                file.write(self.text)

            for index, img_link in enumerate(self.image_links):
                image_url = self._get_image_base_url(img_link)
                image_type_str = self._get_image_type(image_url)
                image_dir = os.path.join(paper_dir, 'images')
                FileUtils.create_dir_if_not_exist(image_dir)
                image_path = os.path.join(image_dir, str(index) + image_type_str)

                print('image url: ', image_url)
                response = requests.get(image_url, stream=True)
                # 检查请求是否成功
                if response.status_code == 200:
                    # 将图片内容写入到本地文件
                    with open(image_path, 'wb') as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)
                else:
                    print(f"请求失败，状态码：{response.status_code}")
        else:
            print('[error] self.html_str is empty')

    def _get_image_base_url(self, url):
        base_url = StringUtils.get_base_url(url)
        if not base_url.endswith('/'):
            return base_url
        else:
            params = StringUtils.get_url_params(url)
            if 'url' in params.keys():
                urls = params['url']
                if len(urls) > 0:
                    return urls[0]
                else:
                    return ''
            return ''

    def _get_image_type(self, url):
        base_url = StringUtils.get_base_url(url)
        if not base_url.endswith('/'):
            return base_url[base_url.rfind('.'):]
        else:
            params = StringUtils.get_url_params(url)
            if 'url' in params.keys():
                urls = params['url']
                if len(urls) > 0:
                    return self._get_image_type(urls[0])
                else:
                    return ''
            return ''

