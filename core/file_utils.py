import json
import os


class FileUtils:

    @staticmethod
    def read_json_file(json_path):
        with open(json_path, 'r', encoding='utf-8') as file:
            content = file.read()
            json_obj = json.loads(content)
            return json_obj

    @staticmethod
    def get_all_files_by_full_path(dir_path):
        files = []
        for path, _, file in os.walk(dir_path):
            for f in file:
                file_path = os.path.join(path, f)
                files.append(file_path)
        return files

    @staticmethod
    def get_all_files(dir_path):
        files = []
        for path, _, file in os.walk(dir_path):
            for f in file:
                files.append(f)
        return files

    @staticmethod
    def create_dir_if_not_exist(dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
