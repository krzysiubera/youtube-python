import pytube
import pytube.exceptions
from exceptions import WrongLinkProvidedError, VideoUnavailableError


def download_video(link_video, file_path):
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

