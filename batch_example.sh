#!/bin/bash

# 启动一个服务
python sccli.py json/cp1.json

# 启动多个服务
python sccli.py json/ss1.json json/gs1.json

# 启动所有的服务
python sccli.py json/*
