"""
MongoDB 是目前最流行的 NoSQL 数据库之一，使用的数据类型 BSON（类似 JSON）。

BSON:
Binary JSON（二进制JSON）
"""
import pymongo

# 连接mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(len(
    ['address', 'arbiters', 'close', 'codec_options', 'drop_database', 'get_database', 'get_default_database',
     'is_mongos', 'is_primary', 'list_database_names', 'list_databases', 'next', 'nodes', 'options', 'primary',
     'read_concern', 'read_preference', 'secondaries', 'server_info', 'start_session', 'topology_description', 'watch',
     'write_concern']
))

# 创建数据库
db = client["mongo_db"]
print(len(['aggregate', 'client', 'codec_options', 'command', 'create_collection', 'dereference', 'drop_collection',
           'get_collection', 'list_collection_names', 'list_collections', 'name', 'next', 'read_concern',
           'read_preference', 'validate_collection', 'watch', 'with_options', 'write_concern']))

# 创建集合
collect = db["sites"]
print(len(
    ['aggregate', 'aggregate_raw_batches', 'bulk_write', 'codec_options', 'count_documents', 'create_index',
     'create_indexes', 'database', 'delete_many', 'delete_one', 'distinct', 'drop', 'drop_index', 'drop_indexes',
     'estimated_document_count', 'find', 'find_one', 'find_one_and_delete', 'find_one_and_replace',
     'find_one_and_update', 'find_raw_batches', 'full_name', 'index_information', 'insert_many', 'insert_one',
     'list_indexes', 'name', 'next', 'options', 'read_concern', 'read_preference', 'rename', 'replace_one',
     'update_many', 'update_one', 'watch', 'with_options', 'write_concern']

))

"""38
create_index
create_indexes

delete_one
delete_many

drop
drop_index
drop_indexes

insert_one
insert_many

update_one
update_many

find
find_one

find_one_and_delete
find_one_and_replace
find_one_and_update

name
rename
database
next
watch
options
"""
