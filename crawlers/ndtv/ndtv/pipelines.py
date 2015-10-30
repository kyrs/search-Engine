# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from elasticsearch import  Elasticsearch
import json
from  scrapy.exceptions import DropItem

class NdtvPipeline(object):
    def __init__(self):
        self.es = Elasticsearch()

    def process_item(self,item,spider):
        index_name = "NDTV"
        #doc_type = item["genre"]
        try:
            response_elastic = self.es.index(index=index_name,doc_type="NEWS",body=dict(item))
            #res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
            print(response_elastic['created'])
        except Exception as e:
             
            raise DropItem("Fail to extract the text:" + type(item))

        return item


    #def process_item(self, item, spider):
    #    return item
