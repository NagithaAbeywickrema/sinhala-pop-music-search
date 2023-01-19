import json


def multi_match(query, fields, operator="or"):
    q = {
        "size": 500,
        "explain": True,
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
            }
        },
        "aggs": {
            "Singer Filter": {"terms": {"field": "v_singer.keyword"}},
            "Composer Filter": {"terms": {"field": "v_composer.keyword"}},
            "Lyricist Filter": {"terms": {"field": "v_lyricist.keyword"}},
        },
    }

    q = json.dumps(q)
    return q


def metaphor_search(query, fields, operator="or"):
    q = {
        "size": 500,
        "explain": True,
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["v_metaphor_0", "v_metaphor_1", "v_metaphor_2"],
                "operator": "or",
            }
        },
        "aggs": {
            "Singer Filter": {"terms": {"field": "v_singer.keyword"}},
            "Composer Filter": {"terms": {"field": "v_composer.keyword"}},
            "Lyricist Filter": {"terms": {"field": "v_lyricist.keyword"}},
        },
    }

    q = json.dumps(q)
    return q
