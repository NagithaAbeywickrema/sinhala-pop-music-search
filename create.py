from elasticsearch_dsl import Index
import json, re
from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

es = Elasticsearch(
    cloud_id=config["ELASTIC"]["cloud_id"],
    http_auth=(config["ELASTIC"]["user"], config["ELASTIC"]["password"]),
)

INDEX = "sin-pop-met"


def createIndex():
    index = Index(INDEX, using=es)
    res = index.create()


def read_all_songs():
    with open("final-corpus/corpus.json", "r") as f:
        all_songs = json.loads(f.read())
        res_list = [i for n, i in enumerate(all_songs) if i not in all_songs[n + 1 :]]
        return res_list


def genData(song_array):
    for song in song_array:
        v_song = song.get("song", None)
        v_lyricist = song.get("lyricist", None)
        v_singer = song.get("singer", None)
        v_composer = song.get("composer", None)
        v_title_sin = song.get("title_sin", None)
        v_title_eng = song.get("title_eng", None)
        v_genre_0 = song.get("genre_0", None)
        v_metaphor_0 = song.get("metaphor_0", None)
        v_metaphor_0_mean = song.get("metaphor_0_mean", None)
        v_genre_1 = song.get("genre_1", None)
        v_metaphor_1 = song.get("metaphor_1", None)
        v_metaphor_1_mean = song.get("metaphor_1_mean", None)
        v_genre_2 = song.get("genre_2", None)
        v_metaphor_2 = song.get("metaphor_2", None)
        v_metaphor_2_mean = song.get("metaphor_2_mean", None)

        yield {
            "_index": INDEX,
            "_source": {
                "v_song": v_song,
                "v_lyricist": v_lyricist,
                "v_singer": v_singer,
                "v_composer": v_composer,
                "v_title_sin": v_title_sin,
                "v_title_eng": v_title_eng,
                "v_genre_0": v_genre_0,
                "v_metaphor_0": v_metaphor_0,
                "v_metaphor_0_mean": v_metaphor_0_mean,
                "v_genre_1": v_genre_1,
                "v_metaphor_1": v_metaphor_1,
                "v_metaphor_1_mean": v_metaphor_1_mean,
                "v_genre_2": v_genre_2,
                "v_metaphor_2": v_metaphor_2,
                "v_metaphor_2_mean": v_metaphor_2_mean,
            },
        }


createIndex()
all_songs = read_all_songs()
helpers.bulk(es, genData(all_songs))
