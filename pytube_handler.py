import pytube
import pytube.exceptions
from exceptions import WrongLinkProvidedError, VideoUnavailableError


class PytubeHandler:
    """ Class for handling Pytube"""

    def __init__(self) -> None:
        self.last_video_title: str = ""
        self.last_video_author: str = ""

    def download_video(self, link_video: str, file_path: str):
        """ Downloading video """
        try:
            youtube = pytube.YouTube(link_video)
        except pytube.exceptions.RegexMatchError:
            raise WrongLinkProvidedError
        except pytube.exceptions.VideoUnavailable:
            raise VideoUnavailableError
        else:
            youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().\
                download(file_path)
            self.last_video_title = youtube.title
            self.last_video_author = youtube.author

    def get_last_video_title(self) -> str:
        """ Get latest downloaded video name"""
        return self.last_video_title

    def get_last_video_author(self) -> str:
        """ Get latest downloaded video author """
        return self.last_video_author



