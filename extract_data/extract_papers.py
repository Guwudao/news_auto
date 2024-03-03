from downloader.downloader_factory import DownloaderType, DownloaderFactory
from .paper_model import PaperModel


class PaperExtractor:

    @staticmethod
    def extract_paper_with_list(papers: list[PaperModel]):
        for model in papers:
            downloader_type = DownloaderType.from_string(model.platform)
            downloader = DownloaderFactory.get_downloader(downloader_type)
            downloader.get_content(model.link)
