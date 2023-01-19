import json
from mtranslate import translate

def translation(to_translate):
    return translate(to_translate, 'si', 'en')

# Open the JSON file
with open('my_json_file.json', 'r') as f:
    # Load the JSON file into a Python dictionary
    songs = json.load(f)

count = 0
# Access the values in the dictionary
for song in songs:
    count +=1
    if song["metaphors"][0]["source"] == "":
        break
print(count)
    

