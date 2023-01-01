import csv
import os
from datetime import datetime
from mutagen.mp3 import MP3

# Set the directory to search
directory = r'h:/'

# Initialize lists to store the data
artists = []
titles = []
dates = []

# Walk through the directory tree and find all MP3 files
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.mp3'):
            # Extract the artist and title from the file metadata
            audio = MP3(os.path.join(root, file))
            artist = audio.tags.get('TPE1', [''])[0]
            title = audio.tags.get('TIT2', [''])[0]
            date = datetime.today().isoformat()
            # Add the data to the lists
            artists.append(artist)
            titles.append(title)
            dates.append(date)

# Write the data to a new CSV file
with open('song_data2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['artist', 'title', 'date'])
    writer.writeheader()
    for i in range(len(artists)):
        writer.writerow({'artist': '"' + artists[i] + '"', 'title': '"' + titles[i] + '"', 'date': dates[i]})
