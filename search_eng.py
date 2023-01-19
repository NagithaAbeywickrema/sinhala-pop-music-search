from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json
import configparser
import queries

config = configparser.ConfigParser()
config.read("config.ini")

es = Elasticsearch(
    cloud_id=config["ELASTIC"]["cloud_id"],
    http_auth=(config["ELASTIC"]["user"], config["ELASTIC"]["password"]),
)

INDEX = "sin-pop-met"


def isEnglish(s):
    try:
        s.encode(encoding="utf-8").decode("ascii")
    except UnicodeDecodeError:
        return False
    else:
        return True


def boost(boost_array):

    term1 = "v_song^{}".format(boost_array[0])
    term2 = "v_lyricist^{}".format(boost_array[1])
    term3 = "v_singer^{}".format(boost_array[2])
    term4 = "v_composer^{}".format(boost_array[3])
    term5 = "v_title_sin^{}".format(boost_array[4])
    term6 = "v_title_eng^{}".format(boost_array[5])
    term7 = "v_genre_0^{}".format(boost_array[6])
    term8 = "v_metaphor_0^{}".format(boost_array[7])
    term9 = "v_metaphor_0_mean^{}".format(boost_array[8])
    term10 = "v_genre_1^{}".format(boost_array[9])
    term11 = "v_metaphor_1^{}".format(boost_array[10])
    term12 = "v_metaphor_1_mean^{}".format(boost_array[11])
    term13 = "v_genre_2^{}".format(boost_array[12])
    term14 = "v_metaphor_2^{}".format(boost_array[13])
    term15 = "v_metaphor_2_mean^{}".format(boost_array[14])

    return [
        term1,
        term2,
        term3,
        term4,
        term5,
        term6,
        term7,
        term8,
        term9,
        term10,
        term11,
        term12,
        term13,
        term14,
        term15,
    ]


def search(phrase):
    flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    fields = boost(flags)
    query_body = queries.multi_match(phrase, fields)
    res = es.search(index=INDEX, body=query_body)

    return res


def search_met(phrase):
    flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    fields = boost(flags)
    query_body = queries.metaphor_search(phrase, fields)
    res = es.search(index=INDEX, body=query_body)
    return res
