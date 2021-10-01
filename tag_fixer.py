# import eyed3
import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import os
import random



def clip(string):
    clip_string = ' (feat.'
    if clip_string in string.lower():
        return(string[:string.lower().find(clip_string)])
    return string
    

def parse_title(string, filename):
    string = clip(string)

    delimiters = [
        ' - ',
        ': ‘'
    ]

    for d in delimiters:
        if x := string.count(d):
            if x > 1:
                print(f"Error with {filename}. Delimiter '{d}' found {x} times.")
                return None
            else:
                result = string.split(d)
                if result[1][-1] == '’':
                    result[1] = result[1][:-1]
                return result
    
    print(f"Error with {filename}. No delimeters found.")
    return None


folder = "F:\Temp\Music Working Files\TEST"
print(folder)
mp3_files = os.listdir(folder)
mp3_files = [f for f in mp3_files if f[-4:] == ".mp3"]
char_set = set()

for file in mp3_files:
    y = EasyID3(os.path.join(folder,file))
    # print(y)
    date = y['date']
    album = y['album']
    albumartist = y['albumartist']
    title = y['title']
    # y.delete()
    # y.save()

    if x := parse_title(title[0], file):
        y['artist'], y['title'] = x
    else:
        y['title'] = title

    y['date'] = date
    y['album'] = album
    y['albumartist'] = albumartist
  
    y.save()



# for i, file in enumerate(mp3_files):
#     # prefix = f"{prefix_list[i]:02x}"[-2:] + " "

#     # x = mutagen.File(os.path.join(folder,file), easy=True)

#     y = EasyID3(os.path.join(folder,file))
#     print(y)
#     y.delete()
#     y['title'] = ['hello']
#     y.save()
#     break
    # print(x.keys())
    # print(prefix, file)
    # print(dir(x))
    # print(x.keys())
    # print(x['title'][0])
    # artist = x['artist'][0]
    # new_file_name = dosify_string(title)
    # new_file_name = prefix + new_file_name[:16] + ".mp3"
    # os.rename(os.path.join(folder, file), os.path.join(folder, new_file_name))
    # print(file, "\n", new_file_name, "\n\n")



# def dosify_string(a_string):
#     '''
#     Make a string a safe file name for a 2012 Hyundai Santa Fe
#     '''


#     kill_words = ['The ', 'the ', ' ']
#     clean_string = "".join(x for x in a_string if x not in '\'<>:"/|?*')
#     clean_string = clean_string.title()

#     if len(clean_string) > 16:
#         for word in kill_words:
#             clean_string = clean_string.replace(word, "")

#     return clean_string

# prefix_list = [i for i in range(len(mp3_files))]

# random.shuffle(prefix_list)


# for i, file in enumerate(mp3_files):
#     prefix = f"{prefix_list[i]:02x}"[-2:] + " "

#     x = mutagen.File(os.path.join(folder,file), easy=True)
#     # print(x.keys())
#     # print(prefix, file)
#     # print(dir(x))
#     # print(x.keys())
#     title = x['title'][0]
#     artist = x['artist'][0]
#     new_file_name = dosify_string(title)
#     new_file_name = prefix + new_file_name[:16] + ".mp3"
#     os.rename(os.path.join(folder, file), os.path.join(folder, new_file_name))
#     # print(file, "\n", new_file_name, "\n\n")

  

    # char_set = char_set | {x for x in title}
        # print(x['title'], title)
    # print(x['TOWN'])
    # y = eyed3.load(os.path.join(folder, file))
    # x = eyed3.load(os.path.join(folder, file))
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
#     x = eyed3.load(os.path.join(folder, file))
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