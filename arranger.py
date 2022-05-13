import os
import random
import mutagen
from mutagen.mp3 import MP3

STICK_FOLDER = r"F:\Temp\Stick Source Files\3 Singles"
mp3_files = os.listdir(STICK_FOLDER)
mp3_files = [f for f in mp3_files if f[-4:].upper() == ".MP3"]
char_set = set()


def dosify_string(a_string):
    """
    Make a string a safe file name for a 2012 Hyundai Santa Fe
    """

    kill_words = ["The ", "the ", " "]
    clean_string = "".join(x for x in a_string if x not in "'<>:\"/|?*")
    clean_string = clean_string.title()

    if len(clean_string) > 19:
        for word in kill_words:
            clean_string = clean_string.replace(word, "")

    return clean_string


def name_folder(prefix, _title):
    folder_max_len = 20

    short_title = dosify_string(_title)

    return (prefix + short_title)[:folder_max_len]


prefix_list = [f"{i + 1:02x} " for i in range(len(mp3_files))]

random.shuffle(prefix_list)


for i, file in enumerate(mp3_files):

    x = mutagen.File(os.path.join(STICK_FOLDER, file), easy=True)
    title = x["title"][0]
    ## CLIP TRAILING SPACES FROM ARTIST'S NAME TO AVOID PROBLEMS
    artist = x["artist"][0].strip()

    subfolder = name_folder(prefix_list[i], artist)

    new_file_name = dosify_string(title)[:19] + ".mp3"

    source = os.path.join(STICK_FOLDER, file)

    dest = os.path.join(STICK_FOLDER, subfolder, new_file_name)

    os.mkdir(os.path.join(STICK_FOLDER, subfolder))

    os.rename(source, dest)
