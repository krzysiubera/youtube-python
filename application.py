import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from typing import Tuple, List
from configparser import ConfigParser
from pathlib import Path
import datetime
from pytube_handler import PytubeHandler
from exceptions import WrongLinkProvidedError, VideoUnavailableError


class Application(tk.Tk):
    """ Class representing application """

    def __init__(self) -> None:
        super().__init__()
        self.initialize_window()
        self.link_entry = self.create_link_box()
        self.file_path_entry, self.file_path_button = self.create_file_path_box()
        self.button_download = self.create_button_download()
        self.initial_path = self.get_initial_path()
        self.video_listbox, self.clear_button = self.create_video_listbox()

        self.downloaded_videos_info: List[str] = []
        self.pytube_handler = PytubeHandler()

    def initialize_window(self) -> None:
        self.title('Python Youtube')
        self.geometry('800x800')

    def create_link_box(self) -> tk.Entry:
        """ Entry where user puts the link to the video """
        link_label = tk.LabelFrame(self, text="Enter your link")
        link_label.pack(pady=10)

        link_entry = tk.Entry(link_label, font=("Helvetica", 24), width=50)
        link_entry.pack(pady=5, padx=5)
        return link_entry

    def create_file_path_box(self) -> Tuple[tk.Entry, tk.Button]:
        """ Entry for path to the file and button for selecting the path"""
        file_path_label_frame = tk.LabelFrame(self, text='Path to save the video')
        file_path_label_frame.pack(pady=5)

        file_path_entry = tk.Entry(file_path_label_frame, font="Helvetica, 24", width=50)
        file_path_entry.pack(pady=5)
        file_path_button = tk.Button(file_path_label_frame, text="Select file path",
                                     command=self.handle_select_file_path)
        file_path_button.pack(pady=5)
        return file_path_entry, file_path_button

    def create_button_download(self) -> tk.Button:
        """ Button for downloading video"""
        button_download_frame = tk.Frame(self)
        button_download_frame.pack(pady=5, padx=5)

        button_download = tk.Button(button_download_frame, text="Download video", command=self.handle_download_video)
        button_download.pack(pady=5, padx=5)
        return button_download

    def create_video_listbox(self) -> Tuple[tk.Listbox, tk.Button]:
        """ List box for storing downloaded videos and button for clearing it """
        video_textbox_frame = tk.Frame(self)
        video_textbox_frame.pack(pady=5, padx=5)

        video_textbox = tk.Listbox(video_textbox_frame, height=10, width=100)
        video_textbox.pack(pady=20, padx=20)
        clear_button = tk.Button(video_textbox_frame, text="Clear downloaded videos",
                                 command=self.handle_clear_downloaded_videos)
        clear_button.pack(pady=5, padx=5)
        return video_textbox, clear_button

    def handle_select_file_path(self) -> None:
        """ Callback when 'Select file path' button is clicked """
        self.file_path_entry.delete(0, tk.END)
        file_path = tk.filedialog.askdirectory(initialdir=self.initial_path, title='Select file path')
        self.file_path_entry.insert(0, file_path)

    def handle_download_video(self) -> None:
        """ Callback when 'Download video' button is clicked """
        link_video = self.link_entry.get()
        file_path = self.file_path_entry.get()
        try:
            self.pytube_handler.download_video(link_video, file_path)
        except WrongLinkProvidedError:
            tk.messagebox.showerror("Error", "Wrong video link provided")
        except VideoUnavailableError:
            tk.messagebox.showerror("Error", "Video unavailable")
        else:
            self.update_list_downloaded_videos()

    def handle_clear_downloaded_videos(self) -> None:
        """ Callback when 'Clear downloaded videos' button is clicked """
        self.downloaded_videos_info = []
        self.video_listbox.delete(0, tk.END)

    def update_list_downloaded_videos(self) -> None:
        """ When the video is downloaded, the function handles putting it into list of downloaded videos """
        title = self.pytube_handler.get_last_video_title()
        author = self.pytube_handler.get_last_video_author()
        msg = f"{datetime.datetime.now().strftime('%d/%m/%y, %H:%M:%S')}: {title} by {author}"
        self.downloaded_videos_info.append(msg)
        self.video_listbox.insert(tk.END, self.downloaded_videos_info[-1])

    @staticmethod
    def get_initial_path() -> Path:
        """ Path to download files shown initially in file dialog """
        config = ConfigParser()
        config.read('config.ini')
        initial_path = config['paths']['initial_path']
        return Path(initial_path)

    def run_application(self) -> None:
        """ Start event loop of the application """
        self.mainloop()
