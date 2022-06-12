from . import es


def is_index_exists(index='vse-index'):
    return es.indices.exists(index=index).raw


def create_index(index='vse-index'):
    es.indices.create(index=index)


def insert_document(video_uuid, index='vse-index', document: str = ''):
    body = {
        "content": document
    }
    es.index(index=index, document=body, id=video_uuid)


def search(query, index="vse-index"):
    result = es.search(index=index, query={"match": {"content": query}})
    return list(map(
        lambda node: {
            "video_uuid": node['_id'],
            "score": node["_score"],
            "content": node["_source"]["content"]
        },
        result['hits']['hits']
    ))
