import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# db_list = myclient.database_names()
# database_names 在最新版本的 Python 中已废弃，Python3.7+ 之后的版本改为了 list_database_names()。
db_list = client.list_database_names()
if "mongo_db" in db_list:
    print("数据库已存在！")

db = client["mongo_db"]

# collect_list = mydb.collection_names()
collect_list = db.list_collection_names()
if "sites" in collect_list:
    print("集合已存在！")

collect = db["sites"]
