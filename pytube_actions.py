import pytube


class PytubeActions:
    """
    A class to represent actions conducted using Pytube
    """

    def __init__(self, app_gui):
        """
        Constructor of PytubeAction class gets AppGui() instance where information should be shown
        Link, title of video and Youtube() class instance (from pytube) are also declared
        """

        self.app_gui = app_gui
        self.link = None
        self.title = None
        self.yt = None

    def get_title_video(self):
        """
        This function gets the link from link entry box, passes it to Youtube() instance class,
        retreives title of the video and then updates the title entry box
        """

        self.link = self.app_gui.link_entry.get()
        self.yt = pytube.YouTube(self.link)
        self.title = self.yt.title
        self.app_gui.title_entry.insert(0, self.title)
        
