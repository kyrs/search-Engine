import json 
from elasticsearch import Elasticsearch


es = Elasticsearch()


def query_dsl(query):

    doc = {
    "query": {
        "multi_match": {
           "query": str(query),
           "fields": ["title","description"]
        }
    }
}
    res = es.search(index="ndtv",doc_type="news" ,body=doc)
    #print("Got %d Hits:" % res['hits']['total'])
    return res['hits']['hits']


if __name__ == "__main__":
    temp = raw_input("please give the input for the search")
    output = query_dsl(query=temp)