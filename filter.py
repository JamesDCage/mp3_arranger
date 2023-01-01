import csv
import os
import mutagen
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def select_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    return directory

# Read the CSV file
song_data = filedialog.askopenfilename(
    filetypes=[("CSV files", "*.csv")]
)

artists = []
titles = []
with open(song_data, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        artists.append(row["artist"].strip('"'))
        titles.append(row["title"].strip('"'))

# Let the user select the directory
directory = select_directory()

# Create the "listened" subdirectory if it doesn't exist
if not os.path.exists(directory + "/listened"):
    os.makedirs(directory + "/listened")

# Scan the selected directory for MP3 files
for file in os.listdir(directory):
    if file.lower().endswith(".mp3"):
        # Read the MP3 file's tags
        audio = mutagen.File(directory + "/" + file)
        artist = audio.get("TPE1", None)
        title = audio.get("TIT2", None)

        # Check if the song is in the CSV file
        if artist and title and artist in artists and title in titles:
            # Move the file to the "listened" subdirectory
            os.rename(directory + "/" + file, directory + "/listened/" + file)
        else:
            # Append the song to the CSV file
            with open(song_data, "a", newline='') as f:
                writer = csv.DictWriter(f, ["artist", "title", "date"])
                writer.writerow({
                    "artist": '"' + str(artist) + '"',
                    "title": '"' + str(title) + '"',
                    "date": datetime.today().strftime("%Y-%m-%d")
                })
