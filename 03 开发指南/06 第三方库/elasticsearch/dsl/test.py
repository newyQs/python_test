from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200/")  # 默认连接本地elasticsearch

print(es.index(index='py2', doc_type='doc', id=1, body={'name': "张开", "age": 18}))
print(es.get(index='py2', doc_type='doc', id=1))
