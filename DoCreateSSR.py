#-*- coding:utf-8 -*-
import json
import socket
import base64

import os
import time

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def DoBase64(str):
    return base64.b64encode(str.encode("utf-8")).replace('=','') #去掉等号

def UnBase64(str):
    return base64.b64decode(str+ b'=' * 3).decode("utf-8") #加上三个等号

#print socket.gethostbyname(socket.gethostname())
vps_ip = get_host_ip()

def DoBase64(str):
    return base64.b64encode(str.encode("utf-8")).replace('=','') #去掉等号
def UnBase64(str):
    return base64.b64decode(str+ b'=' * 3).decode("utf-8") #加上三个等号
#print socket.gethostbyname(socket.gethostname())
vps_ip = get_host_ip()

filename = "/usr/local/shadowsocksr/mudb.json"
#filename = "F:\\mudb.json"
file_obj = open(filename,"r")
ssrs = json.load(file_obj)
#print ssrs
for ssr in ssrs:
    #print ssr
    user = str( ssr['user'] )
    method = str( ssr['method'] )
    obfs = str( ssr['obfs'] )
    port = str( ssr['port'] )
    protocol = str( ssr['protocol'] )

    passwd = str( DoBase64(ssr['passwd']) )
    if 'obfs_param' in ssr:
        obfs_param = str( DoBase64( ssr['obfs_param'] ) )
    else:
        obfs_param = str( DoBase64( '' ) )
    protocol_param = str( DoBase64( ssr['protocol_param'] ) )

    params_base64 = 'obfsparam=' + obfs_param + '&protoparam=' + protocol_param + '&remarks=' + DoBase64('HOSTWIND_VPS') + '&group=' + DoBase64(user) 

#    ssr_url = vps_ip + ':' + port + ':' + protocol + ':' + method + ':' + obfs  + ':' + passwd + '/?' + 'obfsparam=' + obfs_param  + '&remarks=' + DoBase64('HOSTWIND_VPS') + '&group=' + DoBase64(user)
    ssr_url = vps_ip + ':' + port + ':' + protocol + ':' + method + ':' + obfs  + ':' + passwd + '/?' + params_base64

    ssr_url = 'ssr://'+DoBase64(ssr_url)
    print ssr_url
    print DoBase64( ssr_url )

    file_r = open('/root/MyVPS/' + user + '.txt', 'w+')
    file_r.write( DoBase64(ssr_url ) )
#    file_r.write( '\n\n\n\n')
#    file_r.write( ssr_url )
    file_r.close()

file_obj.close()

############################################################################################################################
os.system("rm -rf .git")
os.system("git init")

#os.system("git remote add origin https://github.com/HR4912/MyVPS.git")
os.system("git remote add origin git@github.com:HR4912/MyVPS.git")

os.system("git pull --rebase origin master")

os.system("git add /root/MyVPS")
os.system("git commit -m \" 更新时间: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\"")
os.system("git push -u origin master")
##################################################################################
os.system("rm -rf .git")
os.system("git init")

#os.system("git remote add origin https://gitee.com/leeherry/MyVPS.git")
os.system("git remote add origin git@gitee.com:leeherry/MyVPS.git")

os.system("git pull --rebase origin master")

os.system("git add /root/MyVPS")
os.system("git commit -m \" 更新时间: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\"")
os.system("git push -u origin master")
##################################################################################
