#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: ma_path.py
@time: 2017/08/24/8:38 PM
"""


import paramiko





def downloadFile(host,port,user,password,remotefile_path,local_file_path):
    t = paramiko.Transport((host, port))
    t.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remotefile_path,local_file_path )
    sftp.close()


def uploadFile(host,port,user,password,local_file_path,remotefile_path):

    t = paramiko.Transport((host, port))
    t.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(local_file_path,remotefile_path)
    sftp.close()


def ssh_cmd(ip, port, cmd, user, passwd):
    result = ""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, user, passwd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        print result
        print stderr.read()
        # ssh.close()
    except:
        print "ssh_cmd err."
    return result




