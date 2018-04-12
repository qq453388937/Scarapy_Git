# -*- coding:utf-8 -*-
from pymongo import MongoClient
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 客户端对象 MongoClient链接数据库后产生的对象，
# 数据库对象 使用客户端选择数据库后产生的对象，
# 集合对象 有数据库对象后选择集合产生的对象，
# 游标对象 查找之后产生的对象


# 创建客户端对象
mongo_client = MongoClient(host="127.0.0.1", port=27017)
# 权限认证		db.authenticate(user,pwd)

# # 查看数据库的链接信息,所有数据库
print(mongo_client.database_names())
# # 查看链接的地址ip信息
# print(mongo_client.address)
# # 选择数据库形式2
# db2 = mongo_client["python"]
# print(db2.name) # 查看db当前数据库的名称

# 选择数据库形式1
db = mongo_client.python
print(db.name)  # 查看db当前数据库的名称
print(db.collection_names())  # 查看集列表
print(db.userinfo)  # 直接数据库点出来集合
print(db.collection_names())
# db.create_collection("goods") # 手动创建集合（一般不这么做，直接创建数据就可以创建集合）
# db.drop_collection("goods") # 手动删除集合

print(db.collection_names())

user_collection = db.user
print(user_collection.name)  # 集合名
print(user_collection.full_name)  # python.user 数据库名.集合名
# 注意在 pymongo 中db.user.find() 不是返回数据而是返回一个可迭代的Cursor对象
print(user_collection.find())  # <pymongo.cursor.Cursor object at 0x7f599fbf8510>
cursor_user = user_collection.find()
# print(list(cursor_user)) # list 强转游标对象 推荐不适用游标对象直接遍历!!!!
for item in user_collection.find({"name": "ddd"}):  # cursor_user
    print item

# one_model = user_collection.find_one({"name": "ddd"}, {"_id": 0})  # 直接返回的就是字典!
# print(one_model)
# # 插入One
# user_collection.insert_one({"name": "insertOne"})
# # 插入多个
# user_collection.insert_many([{"name": "many_One"}, {"name": "many_One"}

# 更新数据
# user_collection.update({"name": "pxd"}, {"name": "666"},upsert=True)  # 一次改一个默认,相当于覆盖 $set

# user_collection.delete_one(query)
# user_collection.delete_many(query)

# 默认删除所有,multi=False
user_collection.remove({"name": "many_One"}, multi=False)

for item in user_collection.find():  # cursor_user
    print item
# 手动关闭数据库
mongo_client.close()
