import eyed3
import mutagen
from mutagen.mp3 import MP3
import os
import random

stick_folder = "F:\Temp\Stick Setup MP3s"
mp3_files = os.listdir(stick_folder)
mp3_files = [f for f in mp3_files if f[-4:] == ".mp3"]
char_set = set()

def dosify_string(a_string):
    '''
    Make a string a safe file name for a 2012 Hyundai Santa Fe
    '''


    kill_words = ['The ', 'the ', ' ']
    clean_string = "".join(x for x in a_string if x not in '\'<>:"/|?*')
    clean_string = clean_string.title()

    if len(clean_string) > 16:
        for word in kill_words:
            clean_string = clean_string.replace(word, "")

    return clean_string

prefix_list = [i for i in range(len(mp3_files))]

random.shuffle(prefix_list)


for i, file in enumerate(mp3_files):
    prefix = f"{prefix_list[i]:02x}"[-2:] + " "

    x = mutagen.File(os.path.join(stick_folder,file), easy=True)
    # print(x.keys())
    # print(prefix, file)
    # print(dir(x))
    # print(x.keys())
    title = x['title'][0]
    artist = x['artist'][0]
    new_file_name = dosify_string(title)
    new_file_name = prefix + new_file_name[:16] + ".mp3"
    os.rename(os.path.join(stick_folder, file), os.path.join(stick_folder, new_file_name))
    # print(file, "\n", new_file_name, "\n\n")

  

    # char_set = char_set | {x for x in title}
        # print(x['title'], title)
    # print(x['TOWN'])
    # y = eyed3.load(os.path.join(stick_folder, file))
    # x = eyed3.load(os.path.join(stick_folder, file))
    # if x and x.tag.title:
    #     try:
    #         new_name = prefix + x.tag.title + ".mp3"
    #         # print(new_name)
    #     except: 
    #         pass
    # print(x.tag.title, x.tag.artist, x.tag.album)
    # break

# char_list = list(char_set)
# char_list.sort()
# print(char_list)

# for i, file in enumerate(mp3_files):
#     prefix = f"{i:02x}"[-2:] + " "
#     x = eyed3.load(os.path.join(stick_folder, file))
#     if x and x.tag.title:
#         try:
#             new_name = prefix + x.tag.title + ".mp3"
#             # print(new_name)
#         except: 
#             pass
#     # print(x.tag.title, x.tag.artist, x.tag.album)
#     # break

# new_names = [f"{i:02x}"[-2:] + " " + file for i, file in enumerate(mp3_files)]

# print(new_names)
# for i in range(258):
#     print(f"{i:02x}"[-2:])