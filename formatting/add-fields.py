import json
from mtranslate import translate

def translation(to_translate):
    return translate(to_translate, 'si', 'en')

# Open the JSON file
with open('crawled.json', 'r') as f:
    # Load the JSON file into a Python dictionary
    songs = json.load(f)

# Access the values in the dictionary
for song in songs:
    title = song["title"]
    title_eng, title_sin= title.split("-")
    title_sin = title_sin.strip()
    title_eng = title_eng.strip()
    song["lyricist"] = translation(song["lyricist"])
    song["singer"] = translation(song["singer"])
    song["composer"] = translation(song["composer"])
    song["title_sin"] = title_sin
    song["title_eng"] = title_eng
    song["metaphors"] = [{"source": "", "target": ""}]

    del song["title"]

with open("translated.json", "w") as f:
    json.dump(songs, f, ensure_ascii=False)
