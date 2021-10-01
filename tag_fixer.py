'''
I subscribe to 2-3 podcasts that distribute free songs. The mp3 files for these podcasts have several 
problems that make them difficult to use as songs long term. For example, there are 
tags that identify them as podcasts, which causes iTunes to treat them differently. The
artist and track names are also assigned incorrectly. This script fixes the tags to 
make it easier to keep the song permanently and find it easily in music players.
'''

from mutagen.easyid3 import EasyID3
import os
folder = r"F:\Temp\Music Working Files\2 Stars"

def clip(string):
    '''
    Some podcast titles includes the featured (not main) artist(s) with the track name.
    Fortunately, the featured artist is at the end of the string. If this is the case, 
    remove the featured artist information. If not, just return the virgin string.
    '''
    clip_string = ' (feat.'

    if clip_string in string.lower():
        return(string[:string.lower().find(clip_string)])

    return string
    

def parse_title(string, filename):
    '''
    Song-a-day podcasts put their own names in the 'artist' field, and cram
    the artist name + song title into the 'title' field. Unpack the artist name
    and song title.
    '''

    string = clip(string) # Get rid of featured artists if present.

    # These are the characters that separate artist name from song title 
    # in the podcasts I subscribe to.
    # I order the delimiters in the list so that the most unusual are first, to
    # (hopefully) prevent problems with delimeters found multiple times.
    delimiters = [': ‘', ': “', ' - ', ': '] 

    for d in delimiters:

        if x := string.count(d): # If the delimeter is found at least once ...

            if x > 1:  # If the delimeter is found more than once, you have a problem.
                print(f"Error with {filename}. Delimiter '{d}' found {x} times.")
                return None
            else:
                result = string.split(d)

                # One podcast puts the track name in fancy quotes. The opening quote is 
                # removed as part of the delimeter. If the closing quote exists, remove it
                if result[1][-1] in ['’', '”']:
                    result[1] = result[1][:-1]

                return result
    
    print(f"Error with {filename}. No delimeters found.")
    return None


# Obtain a list of mp3 files in the specified directory
mp3_files = os.listdir(folder)
mp3_files = [f for f in mp3_files if f[-4:] == ".mp3"]

for file in mp3_files:
    y = EasyID3(os.path.join(folder,file)) # Get the tag

    # Save the tag info you want to keep
    date = y['date'][0]
    album = y['album'][0]
    title = y['title'][0]
    genre = y['genre'][0]

    # Delete the tag, which includes unwanted information
    y.delete()

    # Obtain the correct artist name and track title from the podcast title tag
    if x := parse_title(title, file):  # I love the walrus operator. 
        y['artist'], y['title'] = x
    else:
        y['title'] = title

    # Add back tag info saved earlier
    y['date'] = date
    y['album'] = album
    y['albumartist'] = "Jimmy"
    y['genre'] = genre
  
    y.save() # Save the new tag