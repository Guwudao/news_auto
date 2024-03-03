from enum import Enum, auto

from downloader.downloader import Downloader
from downloader.news_163_downloader import News163Downloader
from downloader.sohu_downloader import SohuDownloader
from downloader.sina_downloader import SinaDownloader
from downloader.the_paper_downloader import ThePaperDownloader


class DownloaderType(Enum):
    N163 = auto()
    SOHU = auto()
    SINA = auto()
    THE_PAPER = auto()

    @staticmethod
    def from_string(s: str):
        try:
            return DownloaderType[s.upper()]
        except KeyError:
            raise ValueError(f"Invalid string '{s}' for conversion to DownloaderType")


class DownloaderFactory:

    @staticmethod
    def get_downloader(d_type: DownloaderType):
        match d_type:
            case DownloaderType.N163:
                return News163Downloader()
            case DownloaderType.SOHU:
                return SohuDownloader()
            case DownloaderType.SINA:
                return SinaDownloader()
            case DownloaderType.THE_PAPER:
                return ThePaperDownloader()
            case _:
                return Downloader()