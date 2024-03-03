import os.path
import datetime
import hashlib
import re
from urllib.parse import urljoin, urlparse, parse_qs


class StringUtils:

    @staticmethod
    def get_base_url(url):
        return urljoin(url, urlparse(url).path)

    @staticmethod
    def get_url_params(url):
        parsed_url = urlparse(url)
        query_string = parsed_url.query
        params_dict = parse_qs(query_string)
        return params_dict

    @staticmethod
    def get_project_root_path():
        project_dir_name = 'NewsCrawler'
        current_dir = os.path.abspath(os.path.dirname(__file__))
        index = current_dir.find(project_dir_name)
        return current_dir[0: index + len(project_dir_name)]

    @staticmethod
    def get_date_time():
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        return formatted_time

    @staticmethod
    def get_date():
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d")
        return formatted_time

    @staticmethod
    def format_file_name(file_name):
        name = file_name
        if file_name.startswith('~$'):
            name = file_name.replace('~$', '')
        return name

    @staticmethod
    def string_to_md5(string):
        # 使用一行代码完成
        md5_value = hashlib.md5(string.encode('utf-8')).hexdigest()
        return md5_value

    @staticmethod
    def legitimate_page_title(page_title):
        if not page_title:
            return ''
        title = page_title
        # Length of title should short then 80
        if len(title) > 55:
            title = page_title[0: 55]
        # Remove . in end
        title = re.sub('[\.]+$', '', title)
        # Remove / in title
        title = title.replace('/', '-')
        # Remove number at start.
        # title = re.sub('^(\.?(\d+(\.\d+)*))', '', title).strip()
        title = title.strip()
        # Special symbal
        # 在Windows 10 系统中，文件夹的名称有一些限制和规定。以下是一些要求：
        #
        # 长度限制： 文件夹名字的总长度不能超过260个字符。这包括文件夹名本身以及它的路径。
        #
        # 禁止的字符： 文件夹名字中不能包含以下字符：
        #
        # < (小于)
        # > (大于)
        # : (冒号)
        # " (双引号)
        # / (正斜杠)
        # \ (反斜杠)
        # | (管道)
        # ? (问号)
        # *(星号)
        # 保留关键字： Windows系统中有一些保留的关键字，不能用作文件夹名字，比如
        # CON, PRN, AUX, NUL, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, LPT9。
        special_symbal = ['<', '>', '：', ':', '\"', '/', '\\', '|', '?', '？', '*']
        for s_symbal in special_symbal:
            title = title.replace(s_symbal, '-')
        while title.startswith('\n'):
            title = title[1:]
        while title.endswith('\n'):
            title = title[0:-1]
        title = title.replace('\n', '-')
        title = title.replace('▶', '')
        return title

