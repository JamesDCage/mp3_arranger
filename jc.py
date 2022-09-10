from tag_fixer import select_folder, get_files, parse_title, get_titles

print(folder:=select_folder(r'F:\Temp\Music Working Files\0 Stars'))

files = get_files(folder)

title_list = get_titles(folder, files)

for title in title_list:
    print(title, parse_title(title, "bubba"))


test_strings = [
    r"Fred again.. & The Blessed Madonna - Marea (We’ve Lost Dancing)",
    r"Elohim - Strut (feat. Big Freedia)",
    r"La Luz - In the Country",
    r"Left at London - there is a place for you here.",
    r"Lightning Bug - The Right Thing Is Hard To Do",
    r"Lionel Boy - I'm Not Afraid",
    r"Little Simz - I Love You, I Hate You",
    r"Little Simz - Woman (feat. Cleo Sol)",
    r"Mac - McCaughan - Circling Around",
    r"Mac McCaughan - Dawn Bends",
    r"MACK Fire Among Us (feat. Akua Naru)",
    r"Ambar Lucid: ‘Get Lost In The Music’",
]


# for i in range(10):
#     print(f"{i+230:02x}")

# for string in test_strings:
#     print(string)
#     print(clip(string), '\n')

# for string in test_strings:
#     print(string)
#     print(parse_title(string, string), '\n')
