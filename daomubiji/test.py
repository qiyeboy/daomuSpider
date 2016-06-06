#coding:utf-8
from pymongo import  MongoClient
client = MongoClient()#'mongodb://localhost:27017/'///'localhost', 27017
db = client.daomu
infor = db.books
book={'title':'fan','age':10}
infor.insert(book)