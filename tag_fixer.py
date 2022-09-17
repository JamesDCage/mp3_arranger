from mutagen.easyid3 import EasyID3
import os
import tkinter as tk
from tkinter import filedialog


def main():
    folder = select_folder(initialdir=r"F:\Temp\Music Working Files\0 Stars")

    # Obtain a list of mp3 files in the specified directory
    mp3_files = get_files(folder)

    for file in mp3_files:
        y = EasyID3(os.path.join(folder, file))  # Get the tag

        # Save the tag info you want to keep
        date = y["date"][0]
        album = y["album"][0]
        title = y["title"][0]
        genre = y["genre"][0]
        artist = y["artist"][0]  # Restore this if the title does not parse

        # Delete the tag, which includes unwanted information
        y.delete()

        # Add back tag info saved earlier
        y["date"] = date
        y["album"] = album
        y["albumartist"] = "Jimmy"
        y["genre"] = genre

        # Obtain the correct artist name and track title from the podcast title tag
        if x := parse_title(title, file):  # I love the walrus operator.
            y["artist"], y["title"] = x
            y.save()
        else:
            y["title"] = title
            y["artist"] = artist
            y.save()
            dump_file(file, folder)


def dump_file(file_name, folder_name):
    """Move a problem file to a sub-directory"""

    dump_folder = os.path.join(folder_name, "Problem Files")

    # Create folder if necessary
    if not os.path.isdir(dump_folder):
        os.makedirs(dump_folder)

    # Move file to folder
    source = os.path.join(folder_name, file_name)
    dest = os.path.join(dump_folder, file_name)
    os.rename(source, dest)

    return


def select_folder(initialdir=None):
    # Provide window to browse files. First, supress tkinter base window
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(initialdir=initialdir)
    return folder


def get_files(folder):
    # Obtain a list of mp3 files in the specified directory
    mp3_files = os.listdir(folder)
    mp3_files = [f for f in mp3_files if f[-4:] == ".mp3"]
    return mp3_files


def get_titles(folder, file_list):

    title_list = [EasyID3(os.path.join(folder, file))["title"][0] for file in file_list]

    return title_list


def clip(string):
    """
    Some podcast titles includes the featured (not main) artist(s) with the track name.
    Fortunately, the featured artist is at the end of the string. If this is the case,
    remove the featured artist information. If not, just return the virgin string.
    """
    clip_string = " (feat."

    if clip_string in string.lower():
        return string[: string.lower().find(clip_string)]

    return string


def parse_title(string, filename):
    """
    Song-a-day podcasts put their own names in the 'artist' field, and cram
    the artist name + song title into the 'title' field. Unpack the artist name
    and song title.
    """

    string = clip(string)  # Get rid of featured artists if present.

    # These are the characters that separate artist name from song title
    # in the podcasts I subscribe to.
    # I order the delimiters in the list so that the most unusual are first, to
    # (hopefully) reduce problems with delimeters found multiple times.
    delimiters = [": ‘", ": “", " - ", ": "]

    for d in delimiters:

        if x := string.count(d):  # If the delimeter is found at least once ...

            if x > 1:  # If the delimeter is found more than once, you have a problem.
                print(f"Error with {filename}. Delimiter '{d}' found {x} times.")
                return None
            else:
                result = string.split(d)

                # One podcast puts the track name in fancy quotes. The opening quote is
                # removed as part of the delimeter. If the closing quote exists, remove it
                if result[1][-1] in ["’", "”"]:
                    result[1] = result[1][:-1]

                return result

    print(f"Error with {filename}. No delimeters found.")
    return None


if __name__ == "__main__":
    main()
