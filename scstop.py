# -*- coding: utf-8 -*-

import json
import sys
import subprocess

import fsp_smd_pb2 as smd
import fsp_common_pb2 as pb_common

def json_to_protobuf(json_config):
    pb_config = smd.ServiceStop()

    pb_config.service_name = json_config["service_name"]
    pb_config.smd_name = json_config["smd_name"]

    return pb_config.SerializeToString()

def post_to_server(pb_data, url):
    p = subprocess.Popen(["curl", "-v", "--data", pb_data, url],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    stdout = p.stdout.read()
    if not stdout:
        print "Something is wrong. Please check if CCS server is running"
        print stdout
        sys.exit(1)
    else:
        return stdout

def output_response(response):
    rsp = smd.ServiceStopRsp()
    rsp.ParseFromString(response)

    r = rsp.response
    print "response code: {0}, message: {1}".format(r.response_code, r.response_msg)

for filename in sys.argv[1:]:
    with open(filename) as fileobj:
        print "====== loading config ======"
        json_config = json.load(fileobj)
        print "{0}".format(json.dumps(json_config, indent=4))
        print "============================"

        request_url = json_config["request_url"]
        pb_data = json_to_protobuf(json_config)

        response = post_to_server(pb_data, request_url)
        output_response(response)
