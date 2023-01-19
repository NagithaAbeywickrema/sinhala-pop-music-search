import json
from mtranslate import translate

def translation(to_translate):
    return translate(to_translate, 'si', 'en')

# Open the JSON file
with open('extracts/translated.json', 'r') as f:
    # Load the JSON file into a Python dictionary
    songs = json.load(f)

# Access the values in the dictionary
for song in songs:
    metaphors = song["metaphors"]
    genres = song["genre"]
    for i in range(3):
        metaphor = ""
        metaphor_mean = ""
        genre = ""
        if i < len(metaphors):
            metaphor = metaphors[i]["source"]
            metaphor_mean = metaphors[i]["target"]
        if i < len(genres):
            genre = genres[i]
        song["genre_"+str(i)] = genre
        song["metaphor_"+str(i)] = metaphor
        song["metaphor_"+str(i)+"_mean"] = metaphor_mean

    del song["genre"]
    del song["metaphors"]

with open("corpus.json", "w") as f:
    json.dump(songs, f, ensure_ascii=False)
