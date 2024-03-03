from .string_utils import StringUtils
from .file_utils import FileUtils
import os


class Config:

    def __init__(self):
        self.config = {}
        self._load_config()

    def _load_config(self):
        config_path = os.path.join(StringUtils.get_project_root_path(), 'config', 'config.json')
        self.config = FileUtils.read_json_file(config_path)


configer = Config()
