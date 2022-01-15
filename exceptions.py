""" Module for custom exceptions """


class WrongLinkProvidedError(Exception):
    """ Exception raised when wrong link to the video is provided """


class VideoUnavailableError(Exception):
    """ Exception raised when video is unavailable """
