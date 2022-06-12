import os
from elasticsearch import Elasticsearch

if 'ELASTICSEARCH_HOST' in os.environ:
    ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST')
else:
    ELASTICSEARCH_HOST = 'http://localhost'

if 'ELASTICSEARCH_PORT' in os.environ:
    ELASTICSEARCH_PORT = os.getenv('ELASTICSEARCH_PORT')
else:
    ELASTICSEARCH_PORT = '9200'

es = Elasticsearch(f"{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}")
