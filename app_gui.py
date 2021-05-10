import tkinter
from tkinter import messagebox
import pytube
from pytube_actions import PytubeActions
from tkinter import ttk
import exceptions

class AppGui(tkinter.Tk):
    """
    A class representing GUI of the application
    """

    def __init__(self):
        """
        Initializing GUI window
        Initializing instance of PytubeActions class
        Initializing buttons and entry boxes
        """

        super().__init__()
        self.initialize_window()

        self.pytube_actions = PytubeActions(self)

        self.link_entry = None
        self.button_info = None
        self.title_entry = None
        self.format_label = None
        self.format_combobox = None
        self.button_download = None
        self.create_link_box()
        self.create_button_info()
        self.create_title_box()
        self.create_format_combobox()
        self.create_button_download()

    def initialize_window(self):
        """
        Initializing GUI
        """

        self.title('Python Youtube')
        self.geometry('800x800')

    def create_link_box(self):
        """
        Initializing the entry box where user pastes his link
        """

        link_label = tkinter.LabelFrame(self, text="Enter your link")
        link_label.pack(pady=10)

        self.link_entry = tkinter.Entry(link_label, font=("Helvetica", 24), width=50)
        self.link_entry.pack(pady=20, padx=20)

    def create_button_info(self):
        """
        Initializing the button, which clicking shows us information about the video
        """

        button_info_frame = tkinter.Frame(self)
        button_info_frame.pack(pady=5, padx=5)

        self.button_info = tkinter.Button(button_info_frame, text="Show info",
                                          command=self.get_title_video)
        self.button_info.pack(pady=20, padx=20)

    def create_title_box(self):
        """
        Initializing the entry box where title of the video shows up
        """

        title_label = tkinter.LabelFrame(self, text="Title of the video")
        title_label.pack(pady=5)

        self.title_entry = tkinter.Entry(title_label, font=("Helvetica", 24), width=50)
        self.title_entry.pack(pady=10, padx=10)

    def create_format_combobox(self):
        """
        Creating combobox for choosing if we want only audio or video also
        """

        self.format_label = tkinter.Label(self, text="Choose video or audio")
        self.format_label.pack(pady=5)

        self.format_combobox = tkinter.ttk.Combobox(self)
        self.format_combobox['values'] = ('Audio', 'Video')
        self.format_combobox.pack(pady=5, padx=5)

    def create_button_download(self):
        """
        Initializing the button which is responsible for downloading the video
        """

        button_download_frame = tkinter.Frame(self)
        button_download_frame.pack(pady=5, padx=5)

        self.button_download = tkinter.Button(button_download_frame, text="Download video",
                                              command=self.download_video)
        self.button_download.pack(pady=5, padx=5)

    def get_title_video(self):
        """
        Deleting what is in the title in the title entry box
        and then invoking function from PytubeAction class
        """

        self.title_entry.delete(0, tkinter.END)

        try:
            self.pytube_actions.get_title_video()
        except pytube.exceptions.RegexMatchError:
            tkinter.messagebox.showwarning("Wrong link provided")
        except:
            tkinter.messagebox.showwarning("Something else went wrong")

    def download_video(self):
        """
        This function invokes function for PytubeAction class
        """

        try:
            self.pytube_actions.download_video()
        except exceptions.FormatNotProvided:
            tkinter.messagebox.showwarning("Format of video has not been provided")
        except:
            tkinter.messagebox.showwarning("Something else went wrong")
