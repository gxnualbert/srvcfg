#!/bin/bash

# 查询所有的 SMD 节点
python scquery.py -A http://192.168.7.74:1114/api/v1.0/service_query_req

# 查询所有活跃的 SMD 节点
python scquery.py -t http://192.168.7.74:1114/api/v1.0/service_query_req

# 查询 smd107a 上可以提供的服务
python scquery.py -a smd107a http://192.168.7.74:1114/api/v1.0/service_query_req

# 查询 smd107a 上已经安装的服务
python scquery.py -i smd107a http://192.168.7.74:1114/api/v1.0/service_query_req

# 查询 ss 服务分布在哪些 smd 节点
python scquery.py -d ss http://192.168.7.74:1114/api/v1.0/service_query_req
