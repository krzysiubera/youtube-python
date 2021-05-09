import pytube
import exceptions


class PytubeActions:
    """
    A class to represent actions conducted using Pytube
    """

    def __init__(self, app_gui):
        """
        Constructor of PytubeAction class gets AppGui() instance where information should be shown
        Youtube() class instance is also initialized
        """

        self.app_gui = app_gui
        self.yt = None

    def get_title_video(self):
        """
        This function gets the link from link entry box, passes it to Youtube() instance class,
        retreives title of the video and then updates the title entry box
        """

        link = self.app_gui.link_entry.get()
        self.yt = pytube.YouTube(link)
        self.app_gui.title_entry.insert(0, self.yt.title)
        
    def download_video(self):
        """
        This function is responsible for downloading the video
        """
        
        if self.app_gui.format_combobox.get() == "Video":
            self.yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        elif self.app_gui.format_combobox.get() == "Audio":
            self.yt.streams.filter(only_audio=True).first().download()
        else:
            raise exceptions.FormatNotProvided