# -*- coding: utf-8 -*-

import sys
import subprocess

import fsp_smd_pb2 as smd
import fsp_common_pb2 as pb_common

def make_protobuf(args):
    pb_config = smd.ServiceQuery()

    if args.smd_available_services is not None:
        pb_config.query_type = smd.EnumAvailableServices
        pb_config.query_argument = args.smd_available_services
    elif args.smd_installed_services is not None:
        pb_config.query_type = smd.EnumInstalledServices
        pb_config.query_argument = args.smd_installed_services
    elif args.service_distribution is not None:
        pb_config.query_type = smd.EnumServiceDistribution
        pb_config.query_argument = args.service_distribution
    elif args.active_smds:
        pb_config.query_type = smd.EnumActiveSmds
    else: # args.all_smds
        pb_config.query_type = smd.EnumAllSmds

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
    query_type = {
        smd.EnumAvailableServices: "smd_available_services",
        smd.EnumInstalledServices: "smd_installed_services",
        smd.EnumServiceDistribution: "service_distribution",
        smd.EnumActiveSmds: "active_smds",
        smd.EnumAllSmds: "all_smds"
    }

    rsp = smd.ServiceQueryRsp()
    rsp.ParseFromString(response)

    print "query type: {0}, query_input: {1}, result:".format(
        query_type[rsp.query_type], rsp.query_argument)

    for result in rsp.query_result:
        print "\t{0}".format(result)


import argparse
parser = argparse.ArgumentParser(
    description="query smd or service state from CCS"
)

parser.add_argument("query_url", help="CCS query URL")

exclusive_group = parser.add_mutually_exclusive_group(required=True)
exclusive_group.add_argument("-a", "--smd_available_services",
                    help="available services on SMD node")
exclusive_group.add_argument("-i", "--smd_installed_services",
                    help="installed services on SMD node")
exclusive_group.add_argument("-d", "--service_distribution",
                    help="service was installed on which SMD nodes")
exclusive_group.add_argument("-t", "--active_smds",
                    action="store_true",
                    help="SMD nodes was in active state")
exclusive_group.add_argument("-A", "--all_smds",
                    action="store_true",
                    help="all SMD nodes known by CCS")
args = parser.parse_args()

pb_data = make_protobuf(args)
response = post_to_server(pb_data, args.query_url)
output_response(response)
