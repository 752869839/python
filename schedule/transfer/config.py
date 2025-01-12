# -*- coding: utf-8 -*-
import pymysql
from redis import StrictRedis
from elasticsearch import Elasticsearch
from rediscluster import RedisCluster

#redis 单节点
R_HOST='172.16.30.45'
R_PORT=6379
db=0

#redis cluster
startup_nodes = [
            {'host': '172.16.30.25', 'port': '6379'},
            {'host': '172.16.30.45', 'port': '6379'},
            {'host': '172.16.30.65', 'port': '6379'},
        ]

# elasticsearch
E1_HOST='172.16.30.68'
E2_HOST='172.16.30.83'
E3_HOST='172.16.30.58'
E_PORT=9200

#mysql
MYSQL_HOST = '172.16.30.46'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'
MYSQL_DBNAME = 'anwang'

# redis_client = StrictRedis(host=R_HOST, port=R_PORT, db=db)

redis_client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

es_client = Elasticsearch(hosts=[E1_HOST,E2_HOST,E3_HOST], port=E_PORT, timeout=30, max_retries=10)

mysql_conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DBNAME, port=MYSQL_PORT)