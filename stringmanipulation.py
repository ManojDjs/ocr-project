import pymongo
import pandas as pd
from pymongo import MongoClient, DESCENDING
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

client = pymongo.MongoClient("mongodb://localhost:27017/")
if (client):
    print("connected")
client2 = pymongo.MongoClient("mongodb://ocr:ocr123@cluster0-shard-00-00-vyttn.mongodb.net:27017,cluster0-shard-00-01-vyttn.mongodb.net:27017,cluster0-shard-00-02-vyttn.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
if (client):
    print("connected")
db = client2.text
collections= db.folder4
db = client.localtext
collection = db.folder4
doc=collection.find({})
doc2=collections.find({})
for i in doc:
    for j in doc2:
        if i['_id']==j['_id']:
            print('done')

# for i in doc:
#     print(i['_id'])
#     img=i['image_name']
#     form=i['form_no']
#     def man(s):
#         s = s.title()
#         s = s.split(' ')
#         l = 0
#         for i in s:
#             i = str(i)
#             if i.isalpha() == True:
#                 pass
#             else:
#                 s[l] = i.upper()
#             if len(i) == 2:
#                 s[l] = i.upper()
#             l = l + 1
#         print(' '.join(s))
#         return (' '.join(s))
#     print(i['address'])
#     newaddress=man(i['address'])
#     print(newaddress)
#     print(i['email'])
#     email=i['email'].lower()
#     print(email)
#     imglis=img.split('_')
#     print(imglis)
#     if len(str(form))==1:
#             imgno=str(imglis[0])+'_'+str(imglis[1])+'000'+str(form)
#             print(imgno)
#     else :
#         imgno = str(imglis[0]) + '_' + str(imglis[1]) +"00"+ str(form)
#         print(imgno)
#     print(imgno)
#     consstring = 'TC_vd - Sdi - IB - BtunVp-'
#     sidsplit = i['sid'].split('-')
#     le = len(sidsplit)
#     sidno = sidsplit[le - 1]
#     newsid = consstring + str(sidno)
#     print(newsid)
#     model = ''
#     if '-' in i['modelnumber']:
#         modelsplit = i['modelnumber'].split('-')
#         nextmodel = modelsplit[1:]
#         print(nextmodel)
#         n = ''
#         for k in nextmodel:
#             n = n + '-' + k
#         print(n)
#         print(n)
#         model = modelsplit[0].title() + n
#         # model=modelsplit[0].title()+''+join(map(str, lnextmodel))
#         print(model)
#     else:
#         model = i['modelnumber'].title()
#         print(model)
#     print(model)
#     collection.update_one({'_id': i['_id']}, {'$set': {
#         'id': imgno,
#         'sid': newsid,
#         'modelnumber': model,
#         'email': i['email'].lower(),
#         'address': newaddress, 'status': 1
#     }
#     })
