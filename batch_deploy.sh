#!/bin/bash

# check root permission
if [ $UID -ne 0 ]; then
    echo "Superuser privileges are required to run this script."
    echo "e.g. \"sudo $0\""
    exit 1
fi

check_result=`yum list installed | grep expect`
if [[ -n $check_result ]]; then
    echo "INFO: expect already installed"
else
    yum install expect -y
fi

machines=$1
password=$2
version=$3
buildid=$4
echo $machines

# 校验 IP 是否有效
CheckIPAddr()
{
    # IP地址必须为全数字
    echo $1|grep "^[0-9]\{1,3\}\.\([0-9]\{1,3\}\.\)\{2\}[0-9]\{1,3\}$" > /dev/null

    if [ $? -ne 0 ]
    then
        return 1
    fi

    ipaddr=$1
    a=`echo $ipaddr | awk -F . '{print $1}'`  # 以"."分隔，取出每个列的值
    b=`echo $ipaddr | awk -F . '{print $2}'`
    c=`echo $ipaddr | awk -F . '{print $3}'`
    d=`echo $ipaddr | awk -F . '{print $4}'`

    for num in $a $b $c $d
    do
        if [ $num -gt 255 ] || [ $num -lt 0 ]; then
            return 1
        fi
    done

    return 0
}

if [ $machine_num -eq 0 ]; then
    echo "ERROR: machine info invalid"
    exit 1;
fi

id=0;
for machine in $machines
do
    CheckIPAddr $machine

    if [ $? -ne 0 ]; then
        echo "ERROR: ip addr [$machine] invalid"
        exit 1;
    else
        id=`expr $id + 1`

        # in order to avoid info expired when the machine is rebuild
        sed -i "/$ip/d" ~/.ssh/known_hosts >/dev/null 2>&1

        echo "INFO: [id] $id, [ip] $machine, [password] $password, [version] $version, [buildid] $buildid"
        ./auto.exp $machine $password $version $buildid
    fi
done

echo $?
