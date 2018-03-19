# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import paramiko
from django.shortcuts import HttpResponse
from django.shortcuts import render
from dwebsocket import accept_websocket, require_websocket
from cmdb import models


# Create your views here.
from cmdb.connCRT import exec_command


def index(request):
    if request.method=="POST":
        hostname=request.POST.get("hostname",None)
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        addresss=request.POST.get("address",None)
        print(hostname,username,password,addresss)
        models.queryLog.objects.create(ip=hostname,user=username,pwd=password,add=addresss)
    query_list=models.queryLog.objects.all()
    return render(request,"add_hosts.html",{"data":query_list})
   # return HttpResponse("你好，世界！")

def exec_command(comm,hostname):
 #   hostname = '192.168.8.210'
    username = 'root'
    password = 'jiong1226##'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,port=22, username=username, password=password)
#    ssh.upload('manage.py','/')
    stdin, stdout, stderr = ssh.exec_command(comm)
    result = stdout.read()
    ssh.close()
    return result


@accept_websocket
def echo_once(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'index.html')
    else:
        for message in request.websocket:
            message = message.decode('utf-8')
            if message == 'backup_all':#这里根据web页面获取的值进行对应的操作
                command = 'tail -f /web/logs/passport.dmall.com/server8011/passport_web.log'
                request.websocket.send(exec_command(command,'192.168.8.210'))  # 发送消息到客户端
            else:
                request.websocket.send('没权限!!!'.encode('utf-8'))

def flower(request):
    return render(request,"flower.html")