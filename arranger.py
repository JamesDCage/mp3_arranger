import os
import random
import tkinter as tk
from tkinter import filedialog

import mutagen
from mutagen.mp3 import MP3


def select_folder(initialdir=None):
    # Provide window to browse files. First, supress tkinter base window
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(initialdir=initialdir)
    return folder


def dosify_string(a_string):
    """
    Make a string a safe file name for a 2012 Hyundai Santa Fe
    """

    clean_string = "".join(x for x in a_string if x not in "'<>:\"/|?*")
    clean_string = clean_string.title()

    kill_words = ["The ", "the ", " "]
    if len(clean_string) > 19:
        for word in kill_words:
            clean_string = clean_string.replace(word, "")

    return clean_string[:19] + ".mp3"


def name_folder(prefix, _title):
    folder_max_len = 20

    short_title = dosify_string(_title)

    return (prefix + short_title)[:folder_max_len]


def main():
    stick_folder = select_folder(r"F:\Temp\Music Working Files\Stick Play")
    mp3_files = os.listdir(stick_folder)
    mp3_files = [f for f in mp3_files if f[-4:].upper() == ".MP3"]

    prefix_list = [f"{i + 1:02x} " for i in range(len(mp3_files))]

    random.shuffle(prefix_list)

    for i, file in enumerate(mp3_files):

        x = mutagen.File(os.path.join(stick_folder, file), easy=True)
        title = x["title"][0]
        ## CLIP TRAILING SPACES FROM ARTIST'S NAME TO AVOID PROBLEMS
        artist = x["artist"][0].strip()

        subfolder = name_folder(prefix_list[i], artist)

        new_file_name = dosify_string(title)

        source = os.path.join(stick_folder, file)

        dest = os.path.join(stick_folder, subfolder, new_file_name)

        os.mkdir(os.path.join(stick_folder, subfolder))

        os.rename(source, dest)


if __name__ == "__main__":
    main()
