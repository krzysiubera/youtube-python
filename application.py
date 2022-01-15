import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from pytube_handler import download_video
from typing import Tuple
from configparser import ConfigParser
from pathlib import Path
from exceptions import WrongLinkProvidedError, VideoUnavailableError


class Application(tk.Tk):
    """ Class representing application """

    initial_path_to_download = r"/Users/krzysiu/Desktop"

    def __init__(self):
        super().__init__()
        self.initialize_window()
        self.link_entry = self.create_link_box()
        self.file_path_entry, self.file_path_button = self.create_file_path_box()
        self.button_download = self.create_button_download()
        self.initial_path = self.get_initial_path()

    def initialize_window(self):
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
        """ Entry for path to the file and button"""
        file_path_label_frame = tk.LabelFrame(self, text='Path to save the video')
        file_path_label_frame.pack(pady=5)

        file_path_entry = tk.Entry(file_path_label_frame, font="Helvetica, 24", width=50)
        file_path_entry.pack(pady=5)
        file_path_button = tk.Button(file_path_label_frame, text="Select file path", command=self.get_file_path)
        file_path_button.pack(pady=5)
        return file_path_entry, file_path_button

    def create_button_download(self) -> tk.Button:
        """ Button for downloading video"""
        button_download_frame = tk.Frame(self)
        button_download_frame.pack(pady=5, padx=5)

        button_download = tk.Button(button_download_frame, text="Download video", command=self.download_video)
        button_download.pack(pady=5, padx=5)
        return button_download

    def get_file_path(self):
        """ Callback when 'Select file path' button is clicked """
        self.file_path_entry.delete(0, tk.END)
        file_path = tk.filedialog.askdirectory(initialdir=self.initial_path, title='Select file path')
        self.file_path_entry.insert(0, file_path)

    def download_video(self):
        """ Callback when 'Download video' button is clicked """
        link_video = self.link_entry.get()
        file_path = self.file_path_entry.get()
        try:
            download_video(link_video, file_path)
        except WrongLinkProvidedError:
            tk.messagebox.showerror("Error", "Wrong video link provided")
        except VideoUnavailableError:
            tk.messagebox.showerror("Error", "Video unavailable")

    @staticmethod
    def get_initial_path() -> Path:
        config = ConfigParser()
        config.read('config.ini')
        initial_path = config['paths']['initial_path']
        return Path(initial_path)

    def run_application(self):
        """ Start event loop of the application """
        self.mainloop()
