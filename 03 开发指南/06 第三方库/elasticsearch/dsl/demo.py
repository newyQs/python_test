from elasticsearch import Elasticsearch

client = Elasticsearch("http://127.0.0.1:9200/")

response = client.search(
    index="my-index",
    body={
        "query": {
            "bool": {
                "must": [{"match": {"title": "python"}}],
                "must_not": [{"match": {"description": "beta"}}],
                "filter": [{"term": {"category": "search"}}]
            }
        },
        "aggs": {
            "per_tag": {
                "terms": {"field": "tags"},
                "aggs": {
                    "max_lines": {"max": {"field": "lines"}}
                }
            }
        }
    }
)

for hit in response['hits']['hits']:
    print(hit['_score'], hit['_source']['title'])

for tag in response['aggregations']['per_tag']['buckets']:
    print(tag['key'], tag['max_lines']['value'])
